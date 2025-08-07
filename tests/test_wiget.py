from src.widget import mask_account_card, get_date
from typing import List, Tuple

def test_mask_account_card(test_card_numbers: List[Tuple[str, str]]) -> None:
    for input_num, expected_output in test_card_numbers:
        assert mask_account_card(input_num) == expected_output


def test_get_date(date: List[str]) -> None:
    assert get_date(date[0]) == "28.11.2003"
    assert get_date(date[1]) == "01.01.2020"
