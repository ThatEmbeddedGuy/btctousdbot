import http.client
import requests 
import json 
from concurrent.futures import ThreadPoolExecutor


USD = "USDT"
URL = "https://api.binance.com"
API_TYPES = {"price" : "/api/v3/avgPrice","time" : "/api/v3/time"}

def main(currs = ["BTC","ETH"] ):
    print(getRatesConcurrent(currs))


def getRatesConcurrent(currs = ["BTC","ETH"]):
    executor = ThreadPoolExecutor(max_workers=4)
    currency_pairs =   [currency + USD for currency in currs ]
    result =  zip(currency_pairs, executor.map(request, currency_pairs))
    return dict(result) 

def getRates(currs = ["BTC","ETH"]):
    currency_pairs =   [currency + USD for currency in currs ]
    results = [ {symbol:request(symbol)} for symbol in currency_pairs]
    return results 

def request(symbol):
    try:
      params = {"symbol":symbol }
      r = requests.get(url = URL+API_TYPES["price"] , params=params) 
      return  json.loads(r.content)["price"]
    except:
      return None
  

if __name__ == "__main__":
    # execute only if run as a script
    print("exec start")
    main()
    print("exec stop")