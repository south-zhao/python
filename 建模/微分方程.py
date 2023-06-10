"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/5/8 9:07
    @Author : south(南风)
    @File : 微分方程.py
    Describe:
    -*- coding: utf-8 -*-
"""
from scipy.integrate import odeint
import pylab as plt
import numpy as np

dy = lambda y, x: [y[1], np.sqrt(1 + y[0] ** 2) / 5 / (1 - x)]
x = np.arange(0, 1, 0.0001)
# 第一个参数是我们自行定义的需要求解的微分方程的函数   第二个参数代表求解的微分方程的初值，没有初值微分方程的解不能唯一确定   第三个参数是求解的微分方程中的自变量，应该是一个连续的序列值
y = odeint(dy, [0, 0], x)
plt.rc("font", size=16)
plt.plot(x, y[:, 0])
plt.plot([1, 1], [0, 0.2], '--k')
plt.show()






