from src.utils import utils
from src.external_api import external_api, test_data


utils("data/operations.json")
external_api(test_data[0])
