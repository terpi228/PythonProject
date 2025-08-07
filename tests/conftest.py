import pytest
from typing import List, Tuple

@pytest.fixture
def sample_operations() -> List:
    """Фикстура с тестовыми данными операций"""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-10-01", "amount": 100},
        {"id": 2, "state": "CANCELED", "date": "2023-09-15", "amount": 200},
        {"id": 3, "state": "EXECUTED", "date": "2023-10-05", "amount": 300},
        {"id": 4, "state": "PENDING", "date": "2023-08-20", "amount": 400},
        {"id": 5, "state": "EXECUTED", "date": "2023-07-10", "amount": 500},
    ]


@pytest.fixture
def empty_operations() -> List:
    """Фикстура с пустым списком операций"""
    return []


@pytest.fixture
def invalid_operations() -> List:
    """Фикстура с некорректными данными"""
    return ["not a dict", 123, None, {"wrong_key": "value"}]


@pytest.fixture
def test_card_numbers() -> List[Tuple[str, str]]:
    return [
        ("1234567812345678", "1234 56** **** 5678"),
        ("12345678901234567890", "**7890"),
        ("123", "123 не является номером аккаунта или карты!"),
    ]


@pytest.fixture
def date() -> List[str]:
    return [
        ("2003-11-28"),
        ("2020/01/01"),
    ]


@pytest.fixture
def card() -> List[str]:
    return [
        "1234567890123456",
        "2020202020202020",
    ]


@pytest.fixture
def number_account() -> List[str]:
    return [
        "123456",
        "666666",
    ]
