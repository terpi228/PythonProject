# test_read_file.py
import pandas as pd
import pytest

from src.read_file import read_csv_file, read_excel_file


@pytest.fixture
def csv_path():
    return "data/transactions.csv"


@pytest.fixture
def excel_path():
    return "data/transactions.xlsx"


def test_read_csv_returns_dataframe(csv_path):
    df = read_csv_file(csv_path)
    assert isinstance(df, pd.DataFrame), "Функция должна возвращать DataFrame"
    assert not df.empty, "DataFrame не должен быть пустым"
    assert len(df.columns) > 1, "Ожидалось несколько столбцов в CSV"


def test_read_excel_returns_dataframe(excel_path):
    df = read_excel_file(excel_path)
    assert isinstance(df, pd.DataFrame), "Функция должна возвращать DataFrame"
    assert not df.empty, "DataFrame не должен быть пустым"
    assert len(df.columns) > 1, "Ожидалось несколько столбцов в Excel"


def test_csv_and_excel_have_same_columns(csv_path, excel_path):
    df_csv = read_csv_file(csv_path)
    df_excel = read_excel_file(excel_path)
    assert list(df_csv.columns) == list(df_excel.columns), "Столбцы должны совпадать"
