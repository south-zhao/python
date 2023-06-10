"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/4/12 9:17
    @Author : south(南风)
    @File : 插值法.py
    Describe: Lagrange线性插值法, 抛物线插值法
    -*- coding: utf-8 -*-
"""
import numpy as np

x0 = np.array([100, 121])
y0 = np.array([10, 11])
q0 = lambda x: x-x0[1]
q1 = lambda x: x-x0[0]
y = q0(115)/q0(x0[0])*y0[0] + q1(115)/q1(x0[1])*y0[1]
print(np.round(y, 4))


