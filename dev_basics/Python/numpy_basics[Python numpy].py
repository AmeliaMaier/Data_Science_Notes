import numpy as np

'''
http://www.scipy-lectures.org/intro/numpy/index.html
https://docs.scipy.org/doc/numpy-dev/user/quickstart.html
'''

ints = np.array(range(5))
floats = np.array(np.random.rand(5,))
bools = np.array([True]*5)
chars = np.array(list('ABCDE'))
strings = np.array(['A','BC',"DEF", "GHIJ", "KLMNO"])

dt = np.dtype('i4')   # 32-bit signed integer
dt = np.dtype('f8')   # 64-bit floating-point number
dt = np.dtype('c16')  # 128-bit complex floating-point number
dt = np.dtype('a25')  # 25-length zero-terminated bytes
dt = np.dtype('U25')  # 25-character string



nd_arr = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10],[11, 12, 13, 14, 15]])
print(nd_arr)
'''array([[ 1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10],
       [11, 12, 13, 14, 15]])'''
nd_arr[1,1] # 7
nd_arr[0:2,0:2]
'''array([[1, 2],
       [6, 7]])'''
nd_arr.sum(axis=1) #array([15, 40, 65])
nd_arr.max() #15

index_corresponding_to_max_value = nd_arr.argmax()
nd_arr.ravel()[index_corresponding_to_max_value] #15
