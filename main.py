from src.generators import filter_by_currency, print_operations, card_number_generator
from data.test_opertations import operations


conclusion = print_operations(filter_by_currency(operations, "USD"))


if __name__ == "__main__":

    for card_number in card_number_generator(1, 5):
        print(card_number)
