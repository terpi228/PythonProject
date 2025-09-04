from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from data.test_opertations import operations

if __name__ == "__main__":
    # Получаем операции в USD
    usd_operations = filter_by_currency(operations, "USD")

    # Используем генератор для вывода операций
    print("Операции в USD:")
    for line in transaction_descriptions(usd_operations):
        print(line)

    # Ваш существующий код для генерации номеров карт
    print("\nНомера карт:")
    for card_number in card_number_generator(15, 22):
        print(card_number)
