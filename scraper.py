import requests
from bs4 import BeautifulSoup

# 🔹 Dictionary containing cryptocurrencies and their corresponding Coindesk URLs
#    Key: Cryptocurrency name
#    Value: URL of the page displaying the current price

coins = {
    "Bitcoin": "https://www.coindesk.com/price/bitcoin",  # ✅ URL for Bitcoin
    "Ethereum": "https://www.coindesk.com/price/ethereum",  # ✅ URL for Ethereum
    "Solana": "https://www.coindesk.com/price/solana"  # ✅ URL for Solana
}


def get_crypto_prices():
    prices = {}

    for name, url in coins.items():
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        price = soup.find("div", {"class": "flex justify-end items-center gap-0"})

        prices[name] = price.text

    return prices

