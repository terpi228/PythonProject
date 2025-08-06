# PythonProject: Обработка финансовых данных

Проект предоставляет инструменты для работы с банковскими транзакциями:
- Маскирование номеров карт и счетов
- Форматирование дат
- Фильтрация и сортировка транзакций

## Установка
```bash
git clone https://github.com/terpi228/PythonProject.git 
```
```bash
cd PythonProject
```
## Использование

*
```python
from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card
```
* Маскирование карты (16 цифр)\
```python
print(get_mask_card_number("1234567812345678"))  # "1234 56** **** 5678"
```
* Маскирование счета (20 цифр)
```python
print(get_mask_account("12345678901234567890"))  # "**7890"
```
* Автоматическое определение типа
```python
print(mask_account_card("Visa 1234567812345678"))  # "Visa 1234 56** **** 5678"
```

## Обработка транзакций
```python
from src.widget import get_date

print(get_date("12.01.2023"))  # "2023-01-12"

from src.processing import sort_by_date, filter_by_state

transactions = [
    {"date": "2023-01-12", "state": "EXECUTED"},
    {"date": "2022-12-25", "state": "CANCELED"}
]
```

## Фильтрация по статусу
print(filter_by_state(transactions, "EXECUTED"))

## Сортировка по дате (по убыванию)
print(sort_by_date(transactions, "desc"))

PythonProject/\
├── src/\
│   ├──main.py\
│   ├── masks.py..........# Функции маскирования\
│   ├── widget.py.........# Основные инструменты\
│   ├── processing.py.....# Обработка транзакций\
│   └── __init__.py\
├── tests/\
│   ├── test_masks.py.....# Тесты масок\
│   ├── test_widget.py....# Тесты виджетов\
│   └── test_processing.py# Тесты обработки\
├── main.py...............# Пример использования

