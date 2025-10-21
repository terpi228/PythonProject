import pytest
import json
from unittest.mock import mock_open, patch, MagicMock


# Импортируем функции из твоего модуля
from src.transactions import (
    read_json,
    read_csv,
    normalize_transaction,
    normalize_transactions,
    filter_by_status,
    sort_transactions,
    filter_rub,
    process_bank_search,
    print_transactions,
)


class TestReadFunctions:
    """Тесты функций чтения файлов"""

    def test_read_json_success(self):
        test_data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
        with patch("builtins.open", mock_open(read_data=json.dumps(test_data))):
            with patch("json.load", return_value=test_data):
                result = read_json("test.json")
                assert result == test_data

    def test_read_json_file_not_found(self):
        with patch("builtins.open", side_effect=FileNotFoundError()):
            result = read_json("nonexistent.json")
            assert result == []

    def test_read_json_decode_error(self):
        with patch("builtins.open", mock_open(read_data="invalid json")):
            with patch("json.load", side_effect=json.JSONDecodeError("msg", "doc", 0)):
                result = read_json("invalid.json")
                assert result == []

    def test_read_csv_success(self):
        test_data = [{"id": "1", "amount": "100"}, {"id": "2", "amount": "200"}]
        mock_df = MagicMock()
        mock_df.to_dict.return_value = test_data

        with patch("pandas.read_csv", return_value=mock_df):
            result = read_csv("test.csv")
            assert result == test_data

    def test_read_csv_file_not_found(self):
        with patch("pandas.read_csv", side_effect=FileNotFoundError()):
            result = read_csv("nonexistent.csv")
            assert result == []


class TestNormalizeFunctions:
    """Тесты функций нормализации"""

    def test_normalize_transaction_json_format(self):
        transaction = {"operationAmount": {"amount": "100.0", "currency": {"name": "USD", "code": "USD"}}}
        result = normalize_transaction(transaction)
        assert result["amount"] == "100.0"
        assert result["currency"] == "USD"

    def test_normalize_transaction_csv_format(self):
        transaction = {"amount": "200.0", "currency_name": "Евро", "currency_code": "EUR"}
        result = normalize_transaction(transaction)
        assert result["amount"] == "200.0"
        assert result["currency"] == "Евро"

    def test_normalize_transaction_unknown_format(self):
        transaction = {"amount": "300.0", "currency": "RUB"}
        result = normalize_transaction(transaction)
        assert result["amount"] == "300.0"
        assert result["currency"] == "RUB"

    def test_normalize_transactions_multiple(self):
        transactions = [
            {"operationAmount": {"amount": "100", "currency": {"name": "USD"}}},
            {"amount": "200", "currency": "RUB"},
        ]
        result = normalize_transactions(transactions)
        assert len(result) == 2
        assert all("amount" in t and "currency" in t for t in result)


class TestFilterFunctions:
    """Тесты функций фильтрации"""

    def test_filter_by_status_executed(self):
        transactions = [{"state": "EXECUTED", "id": 1}, {"state": "CANCELED", "id": 2}, {"state": "EXECUTED", "id": 3}]
        result = filter_by_status(transactions, "EXECUTED")
        assert len(result) == 2
        assert all(t["state"] == "EXECUTED" for t in result)

    def test_filter_by_status_case_insensitive(self):
        transactions = [{"state": "executed", "id": 1}]
        result = filter_by_status(transactions, "EXECUTED")
        assert len(result) == 1

    def test_filter_rub_various_formats(self):
        transactions = [
            {"currency": "RUB", "id": 1},
            {"currency": "руб", "id": 2},
            {"currency": "USD", "id": 3},
            {"currency": "российский рубль", "id": 4},
        ]
        result = filter_rub(transactions)
        assert len(result) == 3
        assert all(any(rub in t["currency"].lower() for rub in ["rub", "руб", "российский рубль"]) for t in result)

    def test_process_bank_search(self):
        transactions = [
            {"description": "Перевод организации"},
            {"description": "Покупка в магазине"},
            {"description": "Оплата услуг"},
        ]
        result = process_bank_search(transactions, "перевод")
        assert len(result) == 1
        assert "Перевод" in result[0]["description"]


class TestSortFunctions:
    """Тесты функций сортировки"""

    def test_sort_transactions_ascending(self):
        transactions = [
            {"date": "2023-01-02T00:00:00", "id": 2},
            {"date": "2023-01-01T00:00:00", "id": 1},
            {"date": "2023-01-03T00:00:00", "id": 3},
        ]
        result = sort_transactions(transactions, "по возрастанию")
        assert [t["id"] for t in result] == [1, 2, 3]

    def test_sort_transactions_descending(self):
        transactions = [
            {"date": "2023-01-01T00:00:00", "id": 1},
            {"date": "2023-01-03T00:00:00", "id": 3},
            {"date": "2023-01-02T00:00:00", "id": 2},
        ]
        result = sort_transactions(transactions, "по убыванию")
        assert [t["id"] for t in result] == [3, 2, 1]

    def test_sort_transactions_invalid_dates(self):
        transactions = [
            {"date": "invalid_date", "id": 1},
            {"date": "2023-01-01T00:00:00", "id": 2},
            {"date": None, "id": 3},
        ]
        result = sort_transactions(transactions, "по возрастанию")
        # Должны обработаться без ошибок
        assert len(result) == 3


class TestIntegration:
    """Интеграционные тесты"""

    def test_full_normalization_pipeline(self):
        raw_transactions = [
            {
                "operationAmount": {"amount": "100.0", "currency": {"name": "USD"}},
                "state": "EXECUTED",
                "date": "2023-01-01T00:00:00",
                "description": "Test transaction",
            }
        ]

        # Нормализация
        normalized = normalize_transactions(raw_transactions)
        # Фильтрация по статусу
        filtered = filter_by_status(normalized, "EXECUTED")
        # Сортировка
        sorted_trans = sort_transactions(filtered, "по возрастанию")

        assert len(sorted_trans) == 1
        assert sorted_trans[0]["amount"] == "100.0"
        assert sorted_trans[0]["currency"] == "USD"

    def test_print_transactions_empty(self, capsys):
        print_transactions([])
        captured = capsys.readouterr()
        assert "Не найдено ни одной транзакции" in captured.out

    def test_print_transactions_with_data(self, capsys):
        transactions = [
            {
                "date": "2023-01-01",
                "description": "Test",
                "amount": "100",
                "currency": "RUB",
                "from": "Счет 1234",
                "to": "Счет 5678",
            }
        ]
        print_transactions(transactions)
        captured = capsys.readouterr()
        assert "Test" in captured.out
        assert "100" in captured.out
        assert "RUB" in captured.out


# Фикстуры для тестовых данных
@pytest.fixture
def sample_json_transactions():
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2023-01-01T00:00:00",
            "operationAmount": {"amount": "100.0", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 1234567890",
            "to": "Счет 0987654321",
        }
    ]


@pytest.fixture
def sample_csv_transactions():
    return [
        {
            "id": "2",
            "state": "CANCELED",
            "date": "2023-01-02T00:00:00",
            "amount": "200.0",
            "currency_name": "RUB",
            "currency_code": "RUB",
            "description": "Покупка в магазине",
        }
    ]


if __name__ == "__main__":

    pytest.main([__file__, "-v"])
