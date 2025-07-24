def get_mask_card_number(num_card: str | int) -> str:
    """Маскирует номер карты, оставляя первые 6 и последние 4 цифры."""
    num_card = str(num_card)
    return f"номер карты: {num_card[0:4]} {num_card[4:6]}** **** {num_card[-4:]}"


def get_mask_account(num_account: str | int) -> str:
    """Маскирует номер счёта, оставляя только последние 4 цифры."""
    num_account = str(num_account)
    return f"номер аккаунта: **{num_account[-4:]}"