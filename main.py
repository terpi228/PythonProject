from src.masks import get_mask_card_number, get_mask_account

print(
    get_mask_card_number(int(input("номер карты\n"))),
    get_mask_account(int(input("номер аккаунта\n"))),
)
