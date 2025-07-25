from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date

print(
    # get_mask_card_number(int(input("номер карты\n"))),
    # get_mask_account(int(input("номер аккаунта\n"))),
    mask_account_card(input("введите номер аккаунта или карты\n")),
    get_date(input()),
)
