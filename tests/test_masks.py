from src.masks import get_mask_card_number, get_mask_account
from typing import List


def test_get_mask_card_number(card: List[str]) -> None:
    assert get_mask_card_number(card[0]) == "номер карты: 1234 56** **** 3456"
    assert get_mask_card_number(card[1]) == "номер карты: 2020 20** **** 2020"


def test_get_mask_account(number_account: List[str]) -> None:
    assert get_mask_account(number_account[0]) == "номер аккаунта: **3456"
    assert get_mask_account(number_account[1]) == "номер аккаунта: **6666"
