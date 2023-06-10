"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/4/9 20:39
    @Author : south(南风)
    @File : scipy1.py
    Describe:
    -*- coding: utf-8 -*-
"""
from scipy.optimize import fsolve, root, least_squares
from scipy.integrate import quad
import numpy as np

# fx = lambda \
#         x: x ** 980 - 5.01 * x ** 979 + 7.398 * x ** 978 - 3.388 * x ** 977 - x ** 3 + 5.01 * x ** 2 - 7.398 * x + 3.399
#
# x1 = fsolve(fx, 1.5, maxfev=400)
# x2 = root(fx, 1.5)
#
# print(x1)
# print("---------")
# print(x2)
# f = lambda x: [x[0]**2+x[1]**2-1, x[0]-x[1]]
# s1 = fsolve(f, [1, 1])
# s2 = root(f, [1, 1])
# print(s1)
# print("------")
# print(s2)


# def fun42(x, a, b):
#     return a*x**2+b*x
#
#
# i1 = quad(fun42, 0, 1, args=(2, 1))
# i2 = quad(fun42, 0, 1, args=(2, 10))
# # print(np.round(i1, 4))
# # print(np.round(i2, 4))
# print(i1)
# print(i2)





