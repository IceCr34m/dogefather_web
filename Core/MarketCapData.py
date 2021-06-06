"""
This file is just a scratch for now
"""

API_KEY = ""

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': API_KEY,
}
session = Session()
session.headers.update(headers)



maping_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'

parameters = {
    'symbol': ['DOGEFATHER'],
}

try:
  response = session.get(maping_url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)


data = data['data']

quote_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
  'id':[9732],
}


try:
  response = session.get(quote_url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
