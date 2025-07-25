from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number() -> None:
    assert get_mask_card_number("1234567812345678") == "номер карты: 1234 56** **** 5678"
    assert get_mask_card_number(1234567812345678) == "номер карты: 1234 56** **** 5678"


def test_get_mask_account() -> None:
    assert get_mask_account("12345678") == "номер аккаунта: **5678"
    assert get_mask_account(12345678) == "номер аккаунта: **5678"
