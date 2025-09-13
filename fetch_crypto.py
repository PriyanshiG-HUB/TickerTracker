# fetch_crypto.py  -- simple ccxt + pycoingecko example
import ccxt
from pycoingecko import CoinGeckoAPI

def fetch_ccxt():
    try:
        exchange = ccxt.binance()               # public endpoints do not need keys
        ohlcv = exchange.fetch_ohlcv('BTC/USDT', timeframe='1m', limit=5)
        print("ccxt / Binance - last 5 OHLCV rows (ms_timestamp, open, high, low, close, volume):")
        for row in ohlcv:
            print(row)
    except Exception as e:
        print("ccxt error:", e)

def fetch_coingecko():
    try:
        cg = CoinGeckoAPI()
        data = cg.get_coin_market_chart_by_id('bitcoin', vs_currency='usd', days=1)
        last = data['prices'][-1]   # [timestamp_ms, price]
        print("\nCoinGecko - latest price (ts_ms, price_usd):", last)
    except Exception as e:
        print("CoinGecko error:", e)

if __name__ == "__main__":
    fetch_ccxt()
    fetch_coingecko()
