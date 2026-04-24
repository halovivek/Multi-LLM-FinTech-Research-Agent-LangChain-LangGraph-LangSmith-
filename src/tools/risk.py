# src/tools/risk.py

import numpy as np

def calculate_var(returns):
    return np.percentile(returns, 5)

def sharpe_ratio(returns):
    return returns.mean() / returns.std()
