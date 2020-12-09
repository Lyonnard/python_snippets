# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 17:12:59 2020

@author: ldelbin
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

header = 'ciao\nio sono un header\ne contengo, virgole'
array = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [11, 22, 33, 44, 55, 66, 77, 88, 99]]
a = np.array(array)
a = a.T  # transpose array
df = pd.DataFrame(data=a, columns=('x', 'y'))
df.to_csv('test.csv', index=False, header=header)

np.savetxt('test2.csv', a, delimiter=',', header=header)

a_l = np.loadtxt('test2.csv', delimiter=',')

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
c = np.c_[a, b]
d = 7

print('hello word')
