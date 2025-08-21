def filter_by_state(operations: list, state: str = "EXECUTED") -> list:
    """Фильтрует операции по state"""
    if not isinstance(operations, list):
        return None
    return [i for i in operations if isinstance(i, dict) and i.get("state") == state]


def sort_by_date(operations: list, reverse: bool = True) -> list:
    """Сортирует операции по дате"""
    if not isinstance(operations, list):
        return None

    def get_date(item: dict) -> str:
        # Четко указываем что возвращаем строку
        date_value = item.get("date") if isinstance(item, dict) else None
        return str(date_value) if date_value is not None else ""

    return sorted(operations, key=get_date, reverse=reverse)
