import numpy as np
import pandas as pd

'''
    the math behind pd.dataframe.cov() and pd.dataframe.corr()
'''
def covariance_try(x,y):
    '''
        INPUT: a numpy array or pandas scalar
        Return: the covariance of the data
    '''
    cov = 0
    x_mean = x.mean()
    y_mean = y.mean()
    '''
    for ind in range(len(x.index)):
        cov += (x[ind]-x_mean)*(y[ind]-y_mean)
        '''
    cov = ((x-x_mean)*(y-y_mean)).sum()
    return cov/len(x.index)

def correlation_try(x,y):
    '''
        INPUT: a numpy array or pandas scalar
        Return: the correlation of the data
    '''
    return covariance_try(x,y)/(x.std()*y.std())
