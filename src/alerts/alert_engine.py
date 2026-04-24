# src/alerts/alert_engine.py

def check_signals(rsi):
    if rsi > 70:
        return "SELL signal"
    elif rsi < 30:
        return "BUY signal"
    return "HOLD"
