import tests
from src.masks import get_mask_card_number, get_mask_account


def test_card_masking() -> None:
    assert get_mask_card_number("1234567890123456") == "номер карты: 1234 56** **** 3456"


def test_account_masking() -> None:
    assert get_mask_account("123456789") == "номер аккаунта: **6789"
