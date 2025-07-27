
import streamlit as st
import pandas as pd
import sp500_options as sp500
import nyse_options as nyse

st.title("🔥 Implied Volatility Screener for S&P and NYSE")
# Create tabs
tab1, tab2,tab3,tab4 = st.tabs(["🔥 S&P 500 High IV Stocks", "❄️ S&P 500 Low IV Stocks", "🔥 NYSE High IV Stocks", "❄️ NYSE Low IV Stocks"])

with tab1:
    st.subheader("S&P 500 Highest Implied Volatility")
    high_iv = df_sp500.sort_values(by="Avg IV (%)", ascending=False).head(20)
    st.dataframe(high_iv.reset_index(drop=True), use_container_width=True)

with tab2:
    st.subheader("S&P 500 Lowest Implied Volatility")
    low_iv = df_sp500.sort_values(by="Avg IV (%)", ascending=True).head(20)
    st.dataframe(low_iv.reset_index(drop=True), use_container_width=True)


with tab3:
    st.subheader("Top 20 NYSE Stocks by Highest Implied Volatility")
    high_iv = df_nyse.sort_values(by="Avg IV (%)", ascending=False).head(20)
    st.dataframe(high_iv.reset_index(drop=True), use_container_width=True)

with tab4:
    st.subheader("Top 20 NYSE Stocks by Lowest Implied Volatility")
    low_iv = df_nyse.sort_values(by="Avg IV (%)", ascending=True).head(20)
    st.dataframe(low_iv.reset_index(drop=True), use_container_width=True)
    

#Manual Refresh button
if st.button("Refresh Data"):
    st.rerun()