# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 12:11:36 2023

@author: user
"""

!pip install graphics.py

from graphics import *
from math import *
from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt

size_screen = 900
coord_min = -700
coord_max = 700
skip = 25
# Creating the 3D by the Function  z = cos*r*d^-r
def calc_z(x, y):
    r = sqrt(x ** 2 + y ** 2)
    return (cos(radians(r))) * (700 * 1.005 ** (-r))

# Setting the window
window = GraphWin("3D_Graph", size_screen, size_screen)
window.setCoords(-850, -850, 850, 850)
window.setBackground("Black")

# list of lower point that I don't want to draw
lower_points=[-size_screen]*(coord_max*2)

# Setting the image
image = Image.new("RGB",(1500,1500))
draw = ImageDraw.Draw(image)

# draw the formula on the window & parallel on the image
for y_axis in range(coord_min, coord_max, skip):
    for x_axis in range(coord_min, coord_max):
        if y_axis + calc_z(x_axis, y_axis) > lower_points[x_axis - coord_min]:
            window.plot(x_axis, y_axis + calc_z(x_axis, y_axis) , "yellow")
            draw.point([(x_axis + 850, 1500 - (y_axis + calc_z(x_axis, y_axis) + 850))], fill="yellow")
            lower_points[x_axis - coord_min] = y_axis + calc_z(x_axis, y_axis)

# rotate the image in 45 degree & save:
image = image.rotate(45)
image.show()
image.save("C:\TEMP\png.GIF")

window.getMouse()
window.close()

