import streamlit as st
import yfinance as yf
import pandas as pd

st.title("🔥 Implied Volatility Screener for S&P and NYSE")

@st.cache_data
def get_sp500_tickers():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    tables = pd.read_html(url)
    return tables[0]['Symbol'].tolist()

@st.cache_data
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

tickers = get_sp500_tickers()
iv_results = []

for ticker in tickers:
    iv, price, volume = get_stock_data(ticker)
    if iv and price and volume:
        iv_results.append({
            "Ticker": ticker,
            "Price ($)": round(price, 2),
            "Volume": int(volume),
            "Avg IV (%)": round(iv * 100, 2)
        })

df_sp500 = pd.DataFrame(iv_results)