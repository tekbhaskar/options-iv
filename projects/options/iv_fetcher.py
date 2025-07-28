import yfinance as yf
import pandas as pd

def get_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        price = info.get("regularMarketPrice", None)
        volume = info.get("volume", None)

        expirations = stock.options
        if not expirations:
            return None, price, volume
        chain = stock.option_chain(expirations[0])
        iv_data = pd.concat([chain.calls['impliedVolatility'], chain.puts['impliedVolatility']])
        avg_iv = iv_data.mean()
        return avg_iv, price, volume
    except:
        return None, None, None
