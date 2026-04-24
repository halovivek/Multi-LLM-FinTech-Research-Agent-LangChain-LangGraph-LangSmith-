import yfinance as yf
import pandas as pd


def fetch_stock_data(ticker: str):
    data = yf.download(ticker, period="6mo")
    return data


def calculate_rsi(data):
    delta = data['Close'].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(14).mean()
    avg_loss = loss.rolling(14).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi.iloc[-1]


def calculate_metrics(data):
    returns = data['Close'].pct_change().dropna()
    sharpe = returns.mean() / returns.std()
    return {"sharpe": sharpe}
