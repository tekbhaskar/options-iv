import streamlit as st
import pandas as pd

def show_high_iv(df):
    st.subheader("🔥 Top 20 Stocks by Highest Implied Volatility")
    high_iv = df.sort_values(by="Avg IV (%)", ascending=False).head(20)
    st.dataframe(high_iv.reset_index(drop=True), use_container_width=True)
