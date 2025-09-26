import json


def utils(data_file) -> bool:
    """Ф-ия проверяет .json файл и печатает содержимое"""

    try:
        with open(f"{data_file}", encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        return True
    except FileNotFoundError:
        print("Файл operations.json не найден!")
        return False
    except json.JSONDecodeError:
        print("Ошибка в формате JSON файла!")
        return False
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return False


if __name__ == "__main__":
    utils("../data/operations.json")
