import streamlit as st
import pandas as pd

def show_low_iv(df):
    st.subheader("❄️ Top 20 Stocks by Lowest Implied Volatility")
    low_iv = df.sort_values(by="Avg IV (%)", ascending=True).head(20)
    st.dataframe(low_iv.reset_index(drop=True), use_container_width=True)
