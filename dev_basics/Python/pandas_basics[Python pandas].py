import pandas as pd

'''http://pandas.pydata.org/pandas-docs/stable/10min.html
http://nbviewer.jupyter.org/github/cs109/content/blob/master/labs/lab3/lab3full.ipynb
'''

# Datetime index
dt_index = pd.date_range(start='2015-1-1', end='2015-11-1', freq='m')
dt_series = pd.Series(data= np.random.randn(10), index = dt_index)
dt_series
'''
2015-01-31   -1.514688
2015-02-28   -0.353672
2015-03-31    0.736414
2015-04-30    2.119265
2015-05-31   -0.887404
2015-06-30    0.779502
2015-07-31   -0.531592
2015-08-31   -0.690342
2015-09-30    0.426414
2015-10-31   -1.018183
Freq: M, dtype: float64'''
dt_series[pd.to_datetime('2015-02-28')]
dt_series['2015-02-28'] #-0.35367248888259006

series_1 = pd.Series(np.random.randn(5), index = ['California', 'Alabama', 'Indiana', 'Montana', 'Kentucky'])
series_2 = pd.Series(np.random.randn(5), index = ['Washington', 'Alabama', 'Montana', 'Indiana', 'New York'])
series_1 + series_2
'''
Alabama      -0.635330
California         NaN
Indiana       0.154637
Kentucky           NaN
Montana      -0.768372
New York           NaN
Washington         NaN
dtype: float64
'''
