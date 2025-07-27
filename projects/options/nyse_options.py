
import streamlit as st
import pandas as pd
import yfinance as yf   
import time


# From NYSE

@st.cache_data
def get_nyse_tickers():
    url = 'https://old.nasdaq.com/screening/companies-by-industry.aspx?exchange=NYSE&render=download'
    df = pd.read_csv(url)
    return df['Symbol'].tolist()

@st.cache_data
def get_nyse_stock_data(ticker):
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

tickers = get_nyse_tickers()
iv_results = []

progress = st.progress(0)
for i, ticker in enumerate(tickers):
    iv, price, volume = get_nyse_stock_data(ticker)
    if iv and price and volume:
        iv_results.append({
            "Ticker": ticker,
            "Price ($)": round(price, 2),
            "Volume": int(volume),
            "Avg IV (%)": round(iv * 100, 2)
        })
    progress.progress((i+1)/len(tickers))

df_nyse = pd.DataFrame(iv_results)