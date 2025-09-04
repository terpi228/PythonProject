import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


TEST_TRANSACTIONS = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 863064926,
        "state": "EXECUTED",
        "date": "2019-12-08T22:46:21.935582",
        "operationAmount": {"amount": "41096.24", "currency": {"name": "USD", "code": "USD"}},
        "description": "Открытие вклада",
        "from": "Счет 90424923579946435907",
        "to": "Счет 77613226829885488381",
    },
]


def test_filter_by_currency_usd():
    """Тест фильтрации по USD."""
    result = list(filter_by_currency(TEST_TRANSACTIONS, "USD"))
    assert len(result) == 2
    assert all(t["operationAmount"]["currency"]["code"] == "USD" for t in result)


def test_filter_by_currency_eur():
    """Тест фильтрации по EUR."""
    result = list(filter_by_currency(TEST_TRANSACTIONS, "EUR"))
    assert len(result) == 1
    assert result[0]["operationAmount"]["currency"]["code"] == "EUR"


def test_filter_by_currency_empty():
    """Тест фильтрации по несуществующей валюте."""
    result = list(filter_by_currency(TEST_TRANSACTIONS, "GBP"))
    assert len(result) == 0


# Тесты для print_operations

import pytest
from src.generators import transaction_descriptions


def test_transaction_descriptions_basic_functionality():
    """Тест базовой функциональности генератора описаний."""

    operations = [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Оплата услуг"},
        {"id": 3, "description": "Возврат средств"}
    ]


    result = list(transaction_descriptions(operations))


    expected = [
        "  Описание: Перевод организации",
        "  Описание: Оплата услуг",
        "  Описание: Возврат средств"
    ]
    assert result == expected


def test_transaction_descriptions_edge_cases():
    """Тест граничных случаев и ошибок."""

    assert list(transaction_descriptions([])) == []

    with pytest.raises(KeyError):
        list(transaction_descriptions([{"id": 1}]))

    # Проверяем что это генератор (ленивые вычисления)
    generator = transaction_descriptions([{"description": "Test"}])
    assert hasattr(generator, '__iter__')
    assert not isinstance(generator, list)



def test_card_number_generator_basic():
    """Тест генерации номеров карт."""
    generator = card_number_generator(1, 3)
    result = list(generator)

    expected = ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]
    assert result == expected


def test_card_number_generator_format():
    """Тест формата номеров карт."""
    result = next(card_number_generator(1234567890123456, 1234567890123456))
    assert result == "1234 5678 9012 3456"


def test_card_number_generator_large_number():
    """Тест генерации большого номера."""
    result = next(card_number_generator(9999999999999999, 9999999999999999))
    assert result == "9999 9999 9999 9999"


def test_card_number_generator_invalid_range():
    """Тест обработки неверного диапазона."""
    with pytest.raises(ValueError, match="Некорректный диапазон генерации карт"):
        list(card_number_generator(0, 5))

    with pytest.raises(ValueError):
        list(card_number_generator(10, 5))


def test_card_number_generator_too_large():
    """Тест обработки слишком большого числа."""
    with pytest.raises(ValueError):
        list(card_number_generator(1, 10000000000000000))


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
