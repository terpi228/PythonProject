import json
import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/utils.log",mode='w',encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("utils")

def read_json(data_file) -> list:
    """Ф-ия проверяет .json файл и печатает содержимое"""

    try:
        with open(f"{data_file}", encoding="utf-8") as f:
            data = json.load(f)
        logger.info('Успешно!')
        return data
    except FileNotFoundError:
        logger.error("Файл operations.json не найден!")
        return []
    except json.JSONDecodeError:
        logger.error("Ошибка в формате JSON файла!")
        return []
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")
        return []


if __name__ == "__main__":
    read_json("../data/operations.json")
