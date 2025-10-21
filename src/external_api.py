import os

import requests
from dotenv import load_dotenv

load_dotenv()

test_data = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "53", "currency": {"name": "евро.", "code": "EUR"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
]


def external_api(currency) -> float:
    """Ф-ия берёт из списка денежный код и сумму и при необходимости конвертирует в рубли"""

    cash = currency["operationAmount"]["currency"]["code"]
    amount = currency["operationAmount"]["amount"]
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={cash}&amount={amount}"
    payload = {}
    headers = {"apikey": os.getenv("EXCHANGE_RATE_API_KEY")}

    response = requests.request("GET", url, headers=headers, data=payload)

    result = response.json()
    result_1 = result["result"]
    return result_1


if __name__ == "__main__":
    get_ex = external_api(test_data[0])
    print(get_ex)
