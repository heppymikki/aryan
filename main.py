import os
from dotenv import load_dotenv
import yfinance as yf
from ta.momentum import RSIIndicator
import streamlit as st

# Fetch stock data
stock = yf.Ticker("TCS.NS")
df = stock.history(interval="1m", period="1d")  # 1-min candles for today

# Calculate RSI
rsi = RSIIndicator(close=df['Close'], window=14)
df['RSI'] = rsi.rsi()

# Streamlit UI
st.title("My AI Market Screener")
st.line_chart(df['Close'])
st.write(df.tail())

st.write("AI says: RSI (Relative Strength Index) is a momentum indicator. An RSI value of 30 typically means the stock is oversold and may be due for a price correction or bounce.")
