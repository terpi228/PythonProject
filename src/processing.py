def filter_by_state(users_information: list[dict], state: str = "EXECUTED") -> list[dict]:
    """сортировка списка по state"""
    return [t for t in users_information if isinstance(t, dict) and t.get('state') == state]

def sort_by_date(operations: list, reverse: bool = True) -> list:
    """Сортирует операции по дате"""
    if not isinstance(operations, list):
        return []

    def get_date(item: dict) -> str:
        date_value = item.get("date") if isinstance(item, dict) else None
        return str(date_value) if date_value is not None else ""

    return sorted(operations, key=get_date, reverse=reverse)  # Добавь reverse сюда!