import json


def utils(data_file) -> list:
    """Ф-ия проверяет .json файл и печатает содержимое"""

    try:
        with open(f"{data_file}", encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        return data
    except FileNotFoundError:
        print("Файл operations.json не найден!")
        return []
    except json.JSONDecodeError:
        print("Ошибка в формате JSON файла!")
        return []
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []


if __name__ == "__main__":
    utils("../data/operations.json")
