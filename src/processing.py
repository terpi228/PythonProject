def filter_by_state(users_information: list[dict], state: str ="EXECUTED") -> list[dict]:
    """сортировка списка по state"""
    return [t for t in users_information if t['state'] == state]


def sort_by_date(data, key)-> list[dict]:
    """вывод по дате от меньшего к большему"""
    return sorted(data, key=lambda x: x.get(key))