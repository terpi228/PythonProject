import pytest
from src.widget import mask_account_card, get_date
from typing import List, Tuple


@pytest.fixture
def test_card_numbers() -> List[Tuple[str, str]]:
    """Фикстура для тестирования маскировки карт и счетов."""
    return [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
    ]


@pytest.fixture
def date() -> List[str]:
    """Фикстура для тестирования форматирования даты."""
    return ["2003-11-28T10:30:00.000000", "2020-01-01T00:00:00.000000"]


def test_mask_account_card(test_card_numbers: List[Tuple[str, str]]) -> None:
    for input_num, expected_output in test_card_numbers:
        assert mask_account_card(input_num) == expected_output


def test_get_date(date: List[str]) -> None:
    assert get_date(date[0]) == "28.11.2003"
    assert get_date(date[1]) == "01.01.2020"
