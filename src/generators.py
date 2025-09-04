def filter_by_currency(transactions, currency):
    """Фильтрует транзакции по валюте и возвращает генератор."""
    for transactions in transactions:
        if transactions["operationAmount"]["currency"]["code"] == currency:
            yield transactions


def transaction_descriptions (operations):
    """Генератор для формирования отчёта об операциях с использованием yield."""
    for i, op in enumerate(operations, 1):
        yield f"  Описание: {op['description']}"


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
