import matplotlib.pyplot as plt
import numpy as np


plt.close("all")


fig1 = plt.figure()
fig1, ax_lst = plt.subplots(
    2, 2
)  # creates a 2 by 2 figure list, if empty create 1 axes
# create a figure
fig1 = plt.figure()

# create the figure and axis
fig1, ax_lst = plt.subplots(2, 2)
# creates a 2 by 2 figure list, if empty create 1 axes
# axes is a single panel
# axis is each direction in the axes
# artist is every visible item


def my_plotter(ax, data1, data2, param_dict):
    out = ax.plot(data1, data2, **param_dict)
    return out


data1, data2, data3, data4 = np.random.randn(4, 100)
x = np.arange(100)
fig, ax = plt.subplots(1, 1)
data1, data2, data3, data4 = np.random.randn(4, 20)
x = np.arange(20)

# to get the xkcd style
# use in context manager since it changes many rcparams
with plt.xkcd():
    my_plotter(ax, x, data2, {"marker": "x"})
plt.tight_layout()
plt.tight_layout()
    my_plotter(ax_lst[0,0], x, data2, {"marker": "x"})
plt.tight_layout()


# unify legend for multiple graphs

ln1 = ax1.plot(xdata,ydata,label='data A')
ln2 = ax2.plot(xdata,ydata,label='data B')

lines = ln1+ln2
labels = [l.get_label() for l in lines]
ax1.legend(lines,labels)