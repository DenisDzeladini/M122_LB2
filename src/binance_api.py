import os
from binance.client import Client

api_key = os.environ.get('binance_api_key')
api_secret = os.environ.get('binance_api_secret')

client = Client(api_key, api_secret)
client.API_URL = 'https://testnet.binance.vision/api'


def get_crypto_price():
    btc_price = client.get_symbol_ticker(symbol="BTCUSDT")
    return btc_price