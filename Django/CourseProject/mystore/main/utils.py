import requests
from .models import ExchangeRate


def fetch_exchange_rates():
    url = "https://api.monobank.ua/bank/currency"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        currencies = {840: "USD"}
        base_currency = 980

        for item in data:
            currencyA_code = item.get("currencyCodeA")
            currencyB_code = item.get("currencyCodeB")

            if currencyA_code in currencies and currencyB_code == base_currency:
                ExchangeRate.objects.update_or_create(
                    currency=currencies[currencyA_code],
                    defaults={
                        "rate_buy": item.get("rateBuy"),
                        "rate_sell": item.get("rateSell"),
                    },
                )
    else:
        print("Помилка при запиті API Монобанку")
