import streamlit as st
import pandas as pd
from data_loader import load_sp500_tickers, load_nyse_tickers
from iv_fetcher import get_stock_data
from high_iv_tab import show_high_iv
from low_iv_tab import show_low_iv

st.set_page_config(page_title="Modular IV Screener", layout="wide")
st.title("📈 Implied Volatility Options Screener")

# Sidebar: Exchange selector
exchange = st.sidebar.selectbox("Choose Exchange", ["S&P 500", "NYSE"])

@st.cache_data
def get_tickers(exchange):
    if exchange == "S&P 500":
        return load_sp500_tickers()
    elif exchange == "NYSE":
        return load_nyse_tickers()

tickers = get_tickers(exchange)

# Limit to N tickers for performance (adjustable)
max_tickers = st.sidebar.slider("Number of stocks to scan", 10, 50, 5)
tickers = tickers[:max_tickers]

iv_results = []
progress = st.progress(0)

for i, ticker in enumerate(tickers):
    iv, price, volume = get_stock_data(ticker)
    if iv and price and volume:
        iv_results.append({
            "Ticker": ticker,
            "Price ($)": round(price, 2),
            "Volume": int(volume),
            "Avg IV (%)": round(iv * 100, 2)
        })
    progress.progress((i + 1) / len(tickers))

df = pd.DataFrame(iv_results)

tab1, tab2 = st.tabs(["🔥 High IV", "❄️ Low IV"])

with tab1:
    show_high_iv(df)

with tab2:
    show_low_iv(df)

# Manual Rrefresh button
if st.button("Refresh Data"):
    st.rerun()