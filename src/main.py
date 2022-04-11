import datasheet as ds
import binance_api as bnc_api

btc_price = bnc_api.get_crypto_price()
ds.populate_datasheet(btc_price['price'])
