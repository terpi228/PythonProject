def filter_by_currency(transactions, currency):
    """Фильтрует транзакции по валюте и возвращает генератор."""
    for transactions in transactions:
        if transactions["operationAmount"]["currency"]["code"] == currency:
            yield transactions


def print_operations(operations):
    """Выводит информацию об операциях в форматированном виде."""
    for i, op in enumerate(operations, 1):
        print(f"Операция #{i}:")
        print(f"  ID: {op['id']}")
        print(f"  Статус: {op['state']}")
        print(f"  Дата: {op['date']}")
        print(f"  Сумма: {op['operationAmount']['amount']} {op['operationAmount']['currency']['code']}")
        print(f"  Описание: {op['description']}")
        if "from" in op:
            print(f"  Отправитель: {op['from']}")
        print(f"  Получатель: {op['to']}")
        print("-" * 50)
    # return print("COMMAND CORRECT")


def card_number_generator(start, end):
    """Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX."""
    if start < 1 or end > 9999999999999999 or start > end:
        raise ValueError("Некорректный диапазон генерации карт")

    for number in range(start, end + 1):
        card_str = str(number).zfill(16)
        formatted_card = " ".join([card_str[0:4], card_str[4:8], card_str[8:12], card_str[12:16]])
        yield formatted_card


if __name__ == "__main__":
    transactions = input()
    print(list(filter_by_currency(transactions, "USDT")))
