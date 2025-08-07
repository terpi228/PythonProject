def filter_by_state(operations, state="EXECUTED"):
    """Фильтрует операции по state"""
    return [i for i in operations if i.get("state") == state]


def sort_by_date(operations, reverse=True):
    """Сортирует операции по дате"""
    return sorted(operations, key=lambda x: x["date"], reverse=reverse)
