from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card
from src.processing import sort_by_date, filter_by_state
from tests.test_processing import TEST_DATA


print(
    # get_mask_card_number(int(input("номер карты  \n"))),
    # get_mask_account(int(input("номер аккаунта  \n"))),

    # mask_account_card(input("введите номер аккаунта или карты  \n")),
    # get_date(input("введите дату\n")),

    filter_by_state(TEST_DATA),
    sort_by_date(TEST_DATA, 'date'),
)

if __name__ == "__main__":
    pass