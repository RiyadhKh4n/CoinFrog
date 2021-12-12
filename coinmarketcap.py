import os
import json
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import time
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
if os.path.exists("env.py"):
    import env  # noqa

C = "{:^80}".format
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
            time.sleep(2)
            print(C(
                f"{Fore.GREEN}{Style.BRIGHT}{ticker}"
                " exists in CoinMarketCap"))
            time.sleep(1)
            print(C("-------------------------------------"))
            return True

        else:
            time.sleep(2)
            print(C(f"{Fore.RED}{Style.BRIGHT}{ticker} is not a valid ticker"))
            return False


def validate_amount(amount):
    """
    Will validate is the users coin amount to ensure only contains numbers
    """
    if not(amount.isalpha()):
        print(C(f"{Fore.GREEN}{Style.BRIGHT}Amount entered is valid"))
        return True

    else:
        print(C(f"{Fore.RED}{Style.BRIGHT}Amount must be a number!"))
        return False


def display_coin_data(ticker, data):
    """
    Will display relevant data that user asks for
    """

    if ticker in tickerList:
        for x in coins:
            if x['symbol'] == ticker:
                print(x['symbol'], x['quote']['USD'][data])

    else:
        print(C(f"{Fore.RED}{Style.BRIGHT}Ticker not in List"))


def display_coin_data_extra(ticker, data):
    """
    Will display extra data from the API which follows a different route
    """

    if ticker in tickerList:
        for x in coins:
            if x['symbol'] == ticker:
                print(x['symbol'], x[data])
    else:
        print(C(f"{Fore.RED}{Style.BRIGHT}Ticker not in List"))


def prompt_toolkit_function():
    text = ''
    # other_function = 0
    answers = [
        'price', 'volume_24h', 'volume_change_24h', 'percent_change_1h',
        'percent_change_24h', 'percent_change_7d', 'market_cap',
        'market_cap_dominance', 'fully_diluted_market_cap',
        'circulating_supply', 'total_supply', 'max_supply', 'name']
    api_data = WordCompleter([
        'price', 'volume_24h', 'volume_change_24h', 'percent_change_1h',
        'percent_change_24h', 'percent_change_7d', 'market_cap',
        'market_cap_dominance', 'fully_diluted_market_cap',
        'circulating_supply', 'total_supply', 'max_supply', 'name'])

    while text not in answers:
        text = prompt('Enter data to research: ', completer=api_data)

        if text in answers:
            return text

        elif text == "Quit":
            time.sleep(2)
            print(C("-----------------------"
                    "-----------------------------------"))
            print(C(f"{Fore.GREEN}{Style.BRIGHT}You have chosen to quit"))
            print(C(f"{Fore.GREEN}{Style.BRIGHT}Redirecting..."))
            print(C("--------------------------"
                    "--------------------------------"))
            time.sleep(1)
            return text

        else:
            time.sleep(0.75)
            print(C("------------------------------------"
                    "----------------------"))
            print(C(f"{Fore.RED}{Style.BRIGHT}{text} is an"
                    "invalid data entry"))
            print(C("------------------------------------"
                    "----------------------"))


def calculate_usd_amount(amount, ticker):
    """
    Will calculate amount of USD needed for user to purchase their coin
    """
    usd_amount = 0
    price = 0
    for x in coins:
        if x['symbol'] == ticker:
            price = float((x['quote']['USD']['price']))

    usd_amount = int(amount) * price

    print(C("Calculating..."))
    print(C("-------------------------------------"))
    time.sleep(2.5)
    print(C(f"Amount: {Fore.MAGENTA}{Style.BRIGHT}{amount}"))
    print(C(f"Token: {Fore.MAGENTA}{Style.BRIGHT}${ticker}"))
    print(C(f"USD Needed: {Fore.MAGENTA}{Style.BRIGHT}${usd_amount}"))


def calculate_coin_amount(usd, ticker):
    """
    Will calculate amount of coins that can be purchased with USD amount given
    """
    amount_of_coins = 0
    price = 0
    for x in coins:
        if x['symbol'] == ticker:
            price = float((x['quote']['USD']['price']))

    amount_of_coins = (float(usd) / price)

    time.sleep(0.5)
    print(C("Calculating..."))
    print(C("-------------------------------------"))
    time.sleep(3)
    print(C(f"Balance: {Fore.MAGENTA}{Style.BRIGHT}${usd}"))
    print(C(f"Token: {Fore.MAGENTA}{Style.BRIGHT}${ticker}"))
    print(C(f"Amount Able to Buy:"
            "{Fore.MAGENTA}{Style.BRIGHT}{amount_of_coins}"))


def convert_two_cryptos(amount, coin_one, coin_two):
    """
    Will convert an amount of one coin in terms of another
    """
    amount_of_coins = 0
    price_of_coin_one = 0
    price_of_coin_two = 0
    coin_one_usd_value = 0

    for x in coins:
        if x['symbol'] == coin_one:
            price_of_coin_one = float((x['quote']['USD']['price']))

    for z in coins:
        if z['symbol'] == coin_two:
            price_of_coin_two = float((z['quote']['USD']['price']))

    coin_one_usd_value = int(amount) * price_of_coin_one
    amount_of_coins = (float(coin_one_usd_value) / price_of_coin_two)

    time.sleep(0.5)
    print(C("Calculating..."))
    print(C("-------------------------------------"))
    time.sleep(3)
    print(C(
        f"{amount} ${coin_one} --> {Fore.MAGENTA}{Style.BRIGHT}{amount_of_coins} ${coin_two}"))


def main():
    get_ticker_list()


main()
