# src/portfolio/optimizer.py

import numpy as np

def optimize(weights, returns):
    return np.dot(weights, returns.mean())
