from src.processing import filter_by_state, sort_by_date
from typing import List

TEST_DATA = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def test_filter_by_state_executed(sample_operations: List) -> None:
    """Тестируем фильтрацию по EXECUTED"""
    result = filter_by_state(sample_operations, "EXECUTED")
    assert len(result) == 3
    assert all(op["state"] == "EXECUTED" for op in result)
    assert {op["id"] for op in result} == {1, 3, 5}


def test_filter_by_state_canceled(sample_operations: List) -> None:
    """Тестируем фильтрацию по CANCELED"""
    result = filter_by_state(sample_operations, "CANCELED")

    assert len(result) == 1
    assert result[0]["id"] == 2
    assert result[0]["state"] == "CANCELED"


def test_filter_empty_list(empty_operations: List) -> None:
    """Тестируем фильтрацию пустого списка"""
    result = filter_by_state(empty_operations, "EXECUTED")
    assert result == []


def test_filter_invalid_data(invalid_operations: List) -> None:
    """Тестируем фильтрацию некорректных данных"""
    result = filter_by_state(invalid_operations, "EXECUTED")
    assert result == []  # Должен вернуть пустой список


def test_sort_by_date_descending(sample_operations: List) -> None:
    """тест даты от новых к старым"""
    result = sort_by_date(sample_operations, reverse=True)
    dates = [op["date"] for op in result]
    assert dates == ["2023-10-05", "2023-10-01", "2023-09-15", "2023-08-20", "2023-07-10"]


def test_sort_by_date_ascending(sample_operations: List) -> None:
    """тест даты"""
    result = sort_by_date(sample_operations, reverse=False)

    dates = [op["date"] for op in result]
    assert dates == ["2023-07-10", "2023-08-20", "2023-09-15", "2023-10-01", "2023-10-05"]


def test_sort_empty_list(empty_operations: list) -> None:
    """тест пустого списка"""
    result = sort_by_date(empty_operations, reverse=True)
    assert result == []
