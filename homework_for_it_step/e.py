import requests
from bs4 import BeautifulSoup


class CurrencyConverter:
    def __init__(self):
        self.url = (
            "https://www.nationalbank.kz/ru/exchangerates/ezhednevnye-kursy-valyut"
        )
        self.usd_rate = self._get_usd_rate()

    def _get_usd_rate(self):
        try:
            response = requests.get(self.url)
            soup = BeautifulSoup(response.text, "html.parser")
            table = soup.find("table")
            for row in table.find_all("tr"):  # type: ignore
                cols = row.find_all("td")
                if len(cols) > 0 and "USD" in cols[1].text:
                    rate_text = cols[3].text.strip().replace(",", ".")
                    return float(rate_text)
        except Exception:
            return 450.0

    def convert(self, amount_kzt):
        return amount_kzt / self.usd_rate


if __name__ == "__main__":
    converter = CurrencyConverter()
    try:
        amount = float(input("enter num in (KZT): "))
        result = converter.convert(amount)
        print(f"sum in dollars: (USD): {result:.2f}")
    except ValueError:
        print("err value needed.")
