import os
import json
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import time
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
if os.path.exists("env.py"):
    import env  # noqa

tickerList = []
URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

params = {
    'start': '1',
    'limit': '2000',
    'convert': 'USD'
}

headers = {
    'X-CMC_PRO_API_KEY': os.environ.get("CMC"),
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

        else:
            time.sleep(1)
            print(f"{ticker} does not exist in CoinMarketCap")
            return False


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


def display_coin_data(ticker, data):
    """
    Will display relevant data that user asks for
    """

    if ticker in tickerList:
        for x in coins:
            if x['symbol'] == ticker:
                x['quote']['USD']['price']
                print(x['symbol'],  x['quote']['USD'][data])
    else:
        print("Ticker not in List") 


def prompt_toolkit_function():
    text = ''
    answers = ['price', 'volume_24h', 'volume_change_24h', 'percent_change_1h','percent_change_24h', 'percent_change_7d', 'market_cap', 'market_cap_dominance', 'fully_diluted_market_cap']
    api_data = WordCompleter(['price', 'volume_24h', 'volume_change_24h', 'percent_change_1h', 'percent_change_24h', 'percent_change_7d', 'market_cap', 'market_cap_dominance', 'fully_diluted_market_cap'])
    while text not in answers:
        text = prompt('Enter data to research: ', completer=api_data)

        if text in answers:
            print(f'Data: {text}')
            return text

        else:
            time.sleep(0.5)
            print("----------------------------------------------------------")
            print(f"{text} is an invalid data entry")
            print("----------------------------------------------------------")


def calculate_usd_amount(amount, ticker):
    """
    Will calculate amount of USD needed for user to purchase their coin
    """
    usd_amount = 0
    price = 0
    for x in coins:
        if x['symbol'] == ticker:
            price = float((x['quote']['USD']['price']))               
            

    usd_amount =int(amount) * price
    print("Calculating...")
    time.sleep(2)
    print(f"You need ${usd_amount} in order to purchase {amount} ${ticker}")


def calculate_coin_amount(usd, ticker):
    """
    Will calculate amount of coins that can be purchased with USD amount given
    """
    amount_of_coins = 0
    price = 0
    for x in coins:
        if x['symbol'] == ticker:
            price = float((x['quote']['USD']['price']))      

    #work out % of the total price of the coin
    amount_of_coins = (float(usd) / price) 

    #divide that % of the coin the want 

    print("Calculating...")
    time.sleep(2)
    print(f"You can purchase {amount_of_coins} ${ticker} with ${usd}")



def main():
    get_ticker_list()


main()


