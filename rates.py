import http.client
import cachetools.func
import requests, json, time

from concurrent.futures import ThreadPoolExecutor


USD = "USDT"
URL = "https://api.binance.com"
API_TYPES = {"price" : "/api/v3/avgPrice","time" : "/api/v3/time"}


@cachetools.func.ttl_cache(maxsize=20, ttl=60)
def get_rates_cached(currs = ["BTC","ETH"]):
    return get_rates_concurrent(currs)

def get_rates_concurrent(currs = ["BTC","ETH"]):
    executor = ThreadPoolExecutor(max_workers=4)
    if isinstance(currs, str):
       currency_pairs= currs + USD
    else:
      currency_pairs = [currency + USD for currency in currs ]
    result =  zip(currency_pairs, executor.map(make_request, currency_pairs))
    return dict(result) 

def get_rates(currs = ["BTC","ETH"]):
    currency_pairs =   [currency + USD for currency in currs ]
    results = [ {symbol:make_request(symbol)} for symbol in currency_pairs]
    return results 

def make_request(symbol):
    try:
      params = {"symbol":symbol }
      r = requests.get(url = URL+API_TYPES["price"] , params=params) 
      return  json.loads(r.content)["price"]
    except:
      return None
  