from src.utils import read_json
from src.masks import get_mask_card_number, get_mask_account

if __name__ == "__main__":
    read_json("data/operations.json")
    get_mask_account("1234567890")
    get_mask_card_number('1234567890')