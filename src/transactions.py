import json
import re
from datetime import datetime
from typing import Dict, List

import pandas as pd


def read_json(filename: str) -> List[Dict]:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Программа: файл {filename} не найден.")
        return []
    except json.JSONDecodeError as e:
        print(f"Программа: ошибка чтения JSON — {e}")
        return []


def read_csv(filename: str) -> List[Dict]:
    try:
        df = pd.read_csv(filename, sep=";", encoding="utf-8")
        return df.to_dict(orient="records")
    except FileNotFoundError:
        print(f"Программа: файл {filename} не найден.")
        return []
    except Exception as e:
        print(f"Программа: ошибка при чтении CSV — {e}")
        return []


def read_excel(filename: str) -> List[Dict]:
    try:
        data = pd.read_excel(filename)
        return data.to_dict(orient="records")
    except FileNotFoundError:
        print(f"Программа: файл {filename} не найден.")
        return []
    except Exception as e:
        print(f"Программа: ошибка при чтении Excel — {e}")
        return []


def normalize_transaction(transaction: Dict) -> Dict:
    """Приводит транзакцию к единому формату."""
    normalized = transaction.copy()

    if "operationAmount" in transaction and isinstance(transaction["operationAmount"], dict):
        normalized["amount"] = transaction["operationAmount"].get("amount", "???")
        currency_data = transaction["operationAmount"].get("currency", {})
        if isinstance(currency_data, dict):
            normalized["currency"] = currency_data.get("name", currency_data.get("code", ""))
        else:
            normalized["currency"] = str(currency_data)

    elif "currency_name" in transaction and "currency_code" in transaction:
        normalized["amount"] = transaction.get("amount", "???")
        if transaction.get("currency_name"):
            normalized["currency"] = transaction["currency_name"]
        else:
            normalized["currency"] = transaction.get("currency_code", "")

    else:
        normalized["amount"] = transaction.get("amount", "???")
        normalized["currency"] = transaction.get("currency", "")

    return normalized


def normalize_transactions(transactions: List[Dict]) -> List[Dict]:
    """Приводит все транзакции к единому формату."""
    return [normalize_transaction(t) for t in transactions]


def filter_by_status(transactions: List[Dict], status: str) -> List[Dict]:
    status = status.lower()
    return [t for t in transactions if str(t.get("state", "")).lower() == status]


def sort_transactions(transactions: List[Dict], sort_order: str) -> List[Dict]:
    reverse = sort_order == "по убыванию"

    def parse_date(date_str: str) -> datetime:
        try:
            date_str = date_str.replace("Z", "+00:00")
            return datetime.fromisoformat(date_str)
        except (ValueError, TypeError):
            return datetime(1900, 1, 1)

    return sorted(
        transactions,
        key=lambda x: parse_date(str(x.get("date", ""))),
        reverse=reverse,
    )


def filter_rub(transactions: List[Dict]) -> List[Dict]:
    """Оставляем только рублевые операции."""
    rub_indicators = {"rub", "руб", "₽", "rur", "российский рубль", "рублей"}

    filtered = []
    for t in transactions:
        currency = str(t.get("currency", "")).lower()
        if any(r in currency for r in rub_indicators):
            filtered.append(t)
    return filtered


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    return [t for t in data if pattern.search(str(t.get("description", "")))]


def print_transactions(transactions: List[Dict]) -> None:
    if not transactions:
        print("Программа: Не найдено ни одной транзакции, " "подходящей под ваши условия фильтрации.")
        return

    print(f"\nПрограмма: Всего банковских операций в выборке: {len(transactions)}\n")

    for i, t in enumerate(transactions, 1):
        date = t.get("date", "Без даты")
        desc = t.get("description", "Без описания")
        amount = t.get("amount", "???")
        currency = t.get("currency", "")
        from_acc = t.get("from", "")
        to_acc = t.get("to", "")

        print(f"{i}. {date} {desc}")
        if from_acc or to_acc:
            print(f"   {from_acc} -> {to_acc}")
        print(f"   Сумма: {amount} {currency}\n")


def main() -> None:
    print(
        """Программа: Привет! Добро пожаловать в программу работы
    с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла"""
    )

    choice = input("Пользователь: ").strip()

    if choice == "1":
        filepath = "data/transactions.json"
        transactions = read_json(filepath)
        print("Программа: Для обработки выбран JSON-файл.")
    elif choice == "2":
        filepath = "data/transactions.csv"
        transactions = read_csv(filepath)
        print("Программа: Для обработки выбран CSV-файл.")
    elif choice == "3":
        filepath = "data/transactions.xlsx"
        transactions = read_excel(filepath)
        print("Программа: Для обработки выбран XLSX-файл.")
    else:
        print("Программа: Некорректный выбор.")
        return

    if not transactions:
        print("Программа: Нет данных для обработки.")
        return

    transactions = normalize_transactions(transactions)
    valid_statuses = {"EXECUTED", "CANCELED", "PENDING"}

    while True:
        print(
            """Программа: Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING"""
        )
        status = input("Пользователь: ").strip().upper()
        if status in valid_statuses:
            filtered = filter_by_status(transactions, status)
            break
        print(f'Программа: Статус операции "{status}" недоступен.')

    if not filtered:
        print("Программа: После фильтрации по статусу не осталось транзакций.")
        return

    sort_by_date = input("Программа: Отсортировать операции по дате? (да/нет)\nПользователь: ").strip().lower()

    if sort_by_date in ("да", "д", "yes", "y", "1"):
        while True:
            sort_order = (
                input("Программа: Отсортировать по возрастанию или по убыванию?\n" "Пользователь: ").strip().lower()
            )

            if sort_order in ("по возрастанию", "возрастанию", "в"):
                filtered = sort_transactions(filtered, "по возрастанию")
                break
            if sort_order in ("по убыванию", "убыванию", "у"):
                filtered = sort_transactions(filtered, "по убыванию")
                break
            print('Программа: Введите "по возрастанию" или "по убыванию".')

    rub_only = input("Программа: Выводить только рублевые транзакции? (да/нет)\nПользователь: ").strip().lower()

    if rub_only in ("да", "д", "yes", "y", "1"):
        filtered = filter_rub(filtered)

    if not filtered:
        print("Программа: После фильтрации по валюте не осталось транзакций.")
        return

    search_filter = (
        input("Программа: Отфильтровать список транзакций по слову в описании? (да/нет)\n" "Пользователь: ")
        .strip()
        .lower()
    )

    if search_filter in ("да", "д", "yes", "y", "1"):
        keyword = input("Программа: Введите слово для поиска в описании:\nПользователь: ").strip()
        if keyword:
            filtered = process_bank_search(filtered, keyword)

    if not filtered:
        print("Программа: После поиска по описанию не осталось транзакций.")
        return

    print("Программа: Распечатываю итоговый список транзакций...")
    print_transactions(filtered)
