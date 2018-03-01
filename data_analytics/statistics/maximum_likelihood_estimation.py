import scipy.stats as scs
import numpy as np
import pandas as pd
'''
    MLE: you loop through the possible parameters (or moments) and test the total likelyhood of each. The most likely one is probably right.
    Can not be done on large datasets as you will get a underflow error due to small numbers. Then you use the logMLE. Below is a simple poisson example of MLE
'''
def likelihood(X, l):
    x_range = range(min(X), max(X)+1)
    poisson = scs.poisson.pmf(x_range, l)
    prob = 1
    for x in X:
        prob *= scs.poisson.pmf(x, l)
    return prob
