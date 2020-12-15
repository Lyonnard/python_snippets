# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 17:12:59 2020

@author: Leonardo Del Bino
"""
import matplotlib.pyplot as plt
import numpy as np

# TODO find a standard documentation way


def main():
    plt.close('all')
    fig1 = plt.figure()
    fig1, ax_lst = plt.subplots(2, 2)  # creates a 2 by 2 figure list, if empty create 1 axes
    # axes is a single panel
    # axis is each direction in the axes
    # artist is every visible item


def my_plotter(ax, data1, data2, param_dict):
    out = ax.plot(data1, data2, **param_dict)
    return out

# which you would then use as:


data1, data2, data3, data4 = np.random.randn(4, 100)
fig, ax = plt.subplots(1, 1)
my_plotter(ax, data1, data2, {'marker': 'x'})


if __name__ == '__main__':
    main()
