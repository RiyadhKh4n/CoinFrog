import key
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
# import requests

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

params = {
    'start': '1',
    'limit': '100',
    'convert' : 'USD'
}

headers = {
    'X-CMC_PRO_API_KEY': key.key,
    'Accepts': 'application/json'
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=params)
  data = json.loads(response.text)
  coins = data['data']


except (ConnectionError, Timeout, TooManyRedirects) as e:
  print( e)


def getSHIBprice():
    for d in data['data']:
        if d['symbol'] == 'SHIB':
            price = float((d['quote']['USD']['price']))
            print(format(price, '.20f'))

def getBTCprice():
    for x in coins:
        if x['symbol'] == 'ETH':
            x['quote']['USD']['price']
            print(x['symbol'],  x['quote']['USD']['price']) 

getSHIBprice()
getBTCprice()
