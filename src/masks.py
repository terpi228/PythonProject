import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/masks.log", mode='w', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("masks")

def get_mask_card_number(num_card: str | int) -> str:
    """Маскирует номер карты, оставляя первые 6 и последние 4 цифры."""
    try:
        num_card = str(num_card)
        if len(num_card) < 10:
            raise ValueError("Слишком короткий номер карты")
        result = f"номер карты: {num_card[0:4]} {num_card[4:6]}** **** {num_card[-4:]}"
        logger.info(f"Маскирован номер карты: {result}")
        return result
    except Exception as e:
        logger.error(f"Ошибка маскировки карты ({num_card}): {e}")
        return "некорректный номер карты"

def get_mask_account(num_account: str | int) -> str:
    try:
        num_account = str(num_account)
        if len(num_account) < 4:
            raise ValueError("Слишком короткий номер счёта")
        result = f"номер аккаунта: **{num_account[-4:]}"
        logger.info(f"Маскирован номер счёта: {result}")
        return result
    except Exception as e:
        logger.error(f"Ошибка маскировки счёта ({num_account}): {e}")
        return "некорректный номер счёта"