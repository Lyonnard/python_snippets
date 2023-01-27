#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created Date: 
Author: Leonardo Del Bino

Description of the script

Copyright (c) 2023 Akhetonics GmbH
'''

import numpy as np
import matplotlib.pyplot as plt

class MyClass:
    def __init__(self, attribute):
        self.attribute = attribute

    def my_method(self):
        print(f"The attribute of the class is: {self.attribute}")

if __name__ == "__main__":
    # Prepare the figure and axis for plotting
    fig, ax = plt.subplots()
    
    # Create an instance of the class and call the method
    my_instance = MyClass("example_attribute")
    my_instance.my_method()
    
    # Plot example
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x)
    ax.plot(x, y)

    plt.tight_layout()
    fig.savefig('Koen bias.png', dpi=600, bbox_inches='tight', pad_inches=0)
    #fig.savefig('Koen bias.pdf', dpi=600, bbox_inches='tight', pad_inches=0)

    plt.show()
