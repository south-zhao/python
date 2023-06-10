"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/5/4 11:39
    @Author : south(南风)
    @File : 类比建模.py
    Describe: 以地球上的模型为例，推理相关星球的模型
    -*- coding: utf-8 -*-
"""
# 类比建模
# from sympy import *
#
#
# v0, g, t, x = symbols("v0 g t x")
# a = -g*t**2/2 + v0*t + 0.85 - x
# a = a.subs(t, v0/g)
# res = solve(a.subs({g: 9.8, x: 1.70}), v0)
# v = Float(res[1], 4)
# res1 = solve(a.subs({g: 9.8/6, v0: v}), x)
# print(res1)


# 数据拟合
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d

# x0 = np.array([1, 3, 4, 5, 6, 7, 8, 9, 10])
# y0 = np.array([10, 5, 4, 2, 1, 1, 2, 3, 4])
# for i in range(1, 4):
#     p = np.polyfit(x0, y0, i)
#     print(np.round(p, 4))
#     p1 = np.poly1d(p)
#     # y = np.polyval(p, x0)
#     y = p1(x0)
#     Err = sum([(i - j) ** 2 for i, j in zip(y, y0)])
#     print(np.round(Err, 4))
#     plot1 = plt.plot(x0, y0, "*", label='original values')
#     plot2 = plt.plot(x0, y, "r", label="curve_fit values")
#     plt.xlabel('x axis')
#     plt.ylabel('y axis')
#     plt.legend()
#     plt.title("curve_fit")
#     plt.show()

# a = np.loadtxt("数据文件/data3_8.txt")
# x0 = np.arange(0, 2.1, 0.1)
# y0 = a[1::2, :].flatten()  # 将多维数据转化为一维数据
#
#
# def func(x, b1, b2, l1, l2):
#     return b1*np.exp(-l1*x) + b2*np.exp(-l2*x)
#
#
# popt, pcov = curve_fit(func, x0, y0)
# yh = func(x0, *popt)
# plt.rc('font', family='SimHei')
# plt.plot(x0, y0, "o")
# plt.plot(x0, yh)
# plt.legend(["已知", "拟合"])
# plt.show()

a = np.loadtxt("数据文件/data3_9.txt")
water = a[::2, :].flatten()
sand = a[::2, :].flatten()
num_sand = water * sand
print(num_sand)
i = np.arange(1, 25)
t = (12*i - 4) * 3600
t1 = t[0]
t2 = t[-1]
f = interp1d(t, num_sand, 'cubic')  # 三次样条插值
tt = np.linspace(t1, t2, 1000)
y = f(tt)
plt.rc('font', family='SimHei')
# plt.plot(water, num_sand, "o")
plt.plot(tt, y)
# plt.legend(["已知", "拟合"])
plt.show()


