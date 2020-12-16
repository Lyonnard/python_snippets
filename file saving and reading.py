# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 17:12:59 2020

@author: ldelbin
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

header = "ciao\nio sono un header\ne contengo, virgole"
array = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [11, 22, 33, 44, 55, 66, 77, 88, 99]]
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

#### This is the numpy method ####
a_np = np.array(array)  # now it is two long rows
a_np = a_np.T  # transpose array two long columns

np.savetxt("np.csv", a_np, delimiter=",", header=header)  # save as ASCII CSV
np.save("np.npy", a_np)  # binary files: careful!
a_np_l = np.loadtxt("np.csv", delimiter=",")  # load the ASCII array back
a_np_ll = np.load("np.npy")  # load the binary array back

# in case you prefer to have column labels you can use dataframes
df = pd.DataFrame(data=a_np, columns=("x", "y"))
df.to_csv("df.csv", index=False, header=header)
df_l=pd.read_csv("df.csv")

# if the array come separated you can stack them by doing the following
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
c = np.c_[a, b]  # this stacks arrays in columns
# c = np.r_[a,b] #this concatenats along the second axis
d = 7

# print("Script completed")
