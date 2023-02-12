# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 11:59:37 2023

@author: user
"""

#Section B

from math import *
from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt

# Section B:
def calc_zB(x, y):
    r = np.sqrt(x ** 2 + y ** 2)
    return np.cos(r) * (10*1.2 ** (-r))

x = np.linspace(7,-7,50)
y = np.linspace(7,-7,50)

X,Y = np.meshgrid(x,y)
Z =calc_zB(X,Y)

ax = plt.axes(projection='3d')
ax.plot_surface(Y,X,Z,cmap='viridis')
ax.set_title('Section 2')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()
