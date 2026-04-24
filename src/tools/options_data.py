# src/tools/options_data.py

import yfinance as yf

def fetch_options_chain(ticker):
    stock = yf.Ticker(ticker + ".NS")
    options = stock.options

    chain = stock.option_chain(options[0])
    calls = chain.calls
    puts = chain.puts

    return {
        "calls": calls.to_dict(),
        "puts": puts.to_dict()
    }
