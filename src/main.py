import re


def clear_names(file_name: str) -> list:
    """Функция для очистки имён от лишних символов"""
    new_names_list = []

    try:
        with open("data/" + file_name, encoding="utf-8") as names_file:
            names_list = names_file.read().split()
    except UnicodeDecodeError:
        with open("data/" + file_name, encoding="cp1251") as names_file:
            names_list = names_file.read().split()

    for name_item in names_list:
        new_name = "".join([symbol for symbol in name_item if symbol.isalpha()])
        if new_name:
            new_names_list.append(new_name)

    return new_names_list


def save_to_file(file_name: str, data: list) -> None:
    """Сохранение данных в файлОВ"""
    with open("data/" + file_name, "w", encoding="utf-8") as names_file:
        names_file.write("\n".join(data))


def is_cyrillic(name_item: str) -> bool:
    """Проверка на вхождение кириллицы в строку"""
    return bool(re.fullmatch("[а-яА-Я]+", name_item))


def filter_russian_names(name_list: list) -> list:
    """Фильтр имён, написанных на русском"""
    return [name for name in name_list if is_cyrillic(name)]


def filter_english_names(name_list: list) -> list:
    """Фильтр имён, написанных на англ"""
    return [name for name in name_list if not is_cyrillic(name)]


if __name__ == "__main__":
    try:

        cleared_names = clear_names("names.txt")
        filtered_names = filter_russian_names(cleared_names)
        save_to_file("russian_names.txt", filtered_names)
        print(f"Успешно сохранено {len(filtered_names)} русских имен.")

        filtered_names = filter_english_names(cleared_names)
        save_to_file("english_names.txt", filtered_names)
        print(f"Успешно сохранено {len(filtered_names)} english имен.")

    except FileNotFoundError:
        print("Ошибка: файл names.txt не найден в папке data/")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
