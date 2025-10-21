from __future__ import annotations

from pathlib import Path
from typing import Dict, List

import pandas as pd


def read_csv_transactions(path: str | Path) -> List[Dict]:
    """
    Считывает транзакции из CSV-файла и возвращает список словарей.
    Каждый элемент списка — словарь с полями колонки.
    """
    df = pd.read_csv(path)
    # Приводим DataFrame к списку словарей (один dict = одна строка)
    return df.to_dict(orient="records")


def read_excel_transactions(path: str | Path, sheet_name=0) -> List[Dict]:
    """
    Считывает транзакции из Excel (xls/xlsx) и возвращает список словарей.
    Указывает openpyxl в зависимостях для xlsx.
    """
    df = pd.read_excel(path, sheet_name=sheet_name)
    return df.to_dict(orient="records")
