# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/9/25 9:44
# @Author : south(南风)
# @File : 3D.py
# Describe: 
# -*- coding: utf-8 -*-
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from numpy import *

ax = plt.axes(projection='3d')

angle = linspace(0, 2 * pi * 5, 400)
x = cos(angle)
y = sin(angle)
z = linspace(0, 5, 400)

ax.plot3D(x, y, z)
ax.set_xlabel('X Axes')
ax.set_ylabel('Y Axes')
ax.set_zlabel('Z Axes')

plt.show()


