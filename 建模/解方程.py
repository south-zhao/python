"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/7/14 21:10
    @Author : south(南风)
    @File : 解方程.py
    Describe:
    -*- coding: utf-8 -*-
"""
import numpy as np
import sympy as sp

# 对于线性方程的求解方法
a = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
x1 = np.linalg.inv(a) @ b # 第一种 用线性代数求逆
x2 = np.linalg.solve(a, b) # 第二种
print(x1, x2)

x1, x2 = sp.symbols('x1, x2')
s = sp.solve([x1**2+x2**2-1, x1-x2], [x1, x2])
print(s)





