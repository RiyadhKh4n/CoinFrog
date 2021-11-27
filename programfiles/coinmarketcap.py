import key
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
# import requests

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

params = {
    'start': '1',
    'limit': '250',
    'convert' : 'USD'
}

headers = {
    'X-CMC_PRO_API_KEY': key.api,
    'Accepts': 'application/json'
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=params)
  data = json.loads(response.text)
  coins = data['data']


except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

def validateTicker(ticker):
    """
    Will validate if the users ticker exits in 'coins'
    """
    
def calculateUSDAmount(amount, ticker):
    """
    Will calculate amount of USD needed for user to purchase their coin
    """

def calculateCoinAmount(USD, ticker):
    """
    Will calculate amount of coins can be purchased with USD amount given
    """

def displayCoinData(ticker, data):
    """
    Will display relevant data that user asks for
    """

