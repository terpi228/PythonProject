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

1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
2. Запустите основной скрипт:
    ```bash
    python main.py
    ```
3. Для фильтрации операций по умолчанию (EXECUTED):
    ```python
    from processing import filter_by_state
    filtered_data = filter_by_state(TEST_DATA)
    ```
4. Для сортировки по дате:
    ```python
    from processing import sort_by_date
    sorted_data = sort_by_date(TEST_DATA)
    ```
*так же код выводит сортировку по дате(**сначало новые**) + параметру state*

## Примеры ввода
файл имеет TEST_DATA FIle для примера

```python
TEST_DATA = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
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
├── main.py...............# Пример использования\
└── requirements.txt......# Зависимости

