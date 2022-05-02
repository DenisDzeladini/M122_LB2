import data_processing as dp
import os
from binance.client import Client

# Get key and secret from defined environment variables
api_key = os.environ.get('binance_api_key')
api_secret = os.environ.get('binance_api_secret')

client = Client(api_key, api_secret)
client.API_URL = 'https://testnet.binance.vision/api'


def get_crypto_info():
    btc_price = client.get_symbol_ticker(symbol="BTCUSDT")
    btc_ticker = client.get_ticker(symbol="BTCUSDT")
    dp.populate_datasheet(btc_price['price'], btc_ticker['priceChange'], btc_ticker['priceChangePercent'])


get_crypto_info()
