import json
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import key
import time

tickerList = []
URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

params = {
    'start': '1',
    'limit': '2000',
    'convert': 'USD'
}

headers = {
    'X-CMC_PRO_API_KEY': key.api,
    'Accepts': 'application/json'
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(URL, params=params)
    data = json.loads(response.text)
    coins = data['data']


except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)


def get_ticker_list():
    for d in data['data']:
        ticker_from_api = d['symbol']
        tickerList.append(ticker_from_api)


def validate_ticker(ticker):
    """
    Will validate if the users ticker exits in tickerList
    """
    for x in tickerList:

        if ticker in tickerList:
            time.sleep(1)
            print(f"{ticker} exists in CoinMarketCap")
            return True
            break

        else:
            time.sleep(1)
            print(f"{ticker} does not exist in CoinMarketCap")
            return False
            break


def validate_amount(amount):
    """
    Will validate is the users coin amount to ensure only contains numbers
    """
    if amount.isnumeric():
        print("Amount entered is valid")
        return True

    else:
        print("Amount must be a number!")
        return False


def calculate_usd_amount(amount, ticker):
    """
    Will calculate amount of USD needed for user to purchase their coin
    """


def calculate_coin_amount(usd, ticker):
    """
    Will calculate amount of coins can be purchased with USD amount given
    """


def display_coin_data(ticker, data):
    """
    Will display relevant data that user asks for
    """


def main():
    get_ticker_list()

main()
