# src/tools/nse_data.py

import yfinance as yf

def fetch_nse_stock(ticker: str):
    ticker = ticker + ".NS"
    data = yf.download(ticker, period="6mo", interval="1d")
    return data
