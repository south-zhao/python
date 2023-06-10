"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/5/2 12:05
    @Author : south(南风)
    @File : 人口模型.py
    Describe:
    -*- coding: utf-8 -*-
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_excel("近年来人口数量表.xlsx")
year = [int(i) for i in df["年份"]][::-1]
year1 = year
year = np.array(year)
year1.extend([2022, 2023, 2024, 2025])
year1 = np.array(year1)
num = df["人数"]
num = [float(i.split("亿")[0]) for i in num][::-1]
num = np.array(num)


# def fune(x, r):
#     return 6.55 * np.exp(r * (x - 1959))
#
#
# popt, pcov = curve_fit(fune, year, num)
# yvals = fune(year, popt[0])
# Err = sum([(i - j)**2 for i, j in zip(yvals, num)])
# print(Err)
# plot1 = plt.plot(year, num, "*", label='original values')
# plot2 = plt.plot(year, yvals, "r", label="curve_fit values")
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.legend(loc=4)
# plt.title("curve_fit")
# plt.show()


# def fund(x, xm, r0):
#     return xm/(1+(xm/6.55-1)*np.exp((-r0)*(x-1959)))
#
#
# popt, pcov = curve_fit(fund, year, num)
# yvals = fund(year, popt[0], popt[1])
# y2 = fund(2025, popt[0], popt[1])
# print(y2)
# Err = sum([(i - j)**2 for i, j in zip(yvals, num)])
# print(Err)
# plot1 = plt.plot(year, num, "*", label='original values')
# plot2 = plt.plot(year, yvals, "r", label="curve_fit values")
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.legend(loc=4)
# plt.title("curve_fit")
# plt.show()


# 改进过后的
z1 = np.polyfit(year, num, 3)
p1 = np.poly1d(z1)
yval = p1(year1)
# Err = sum([(i - j)**2 for i, j in zip(yval, num)])
# print(Err)
plot1 = plt.plot(year, num, "*", label='original values')
# for i, j in zip(year, num):
#     plt.text(i, j, j, ha="center", va="bottom", fontsize=5)
plot2 = plt.plot(year1, yval, "r", label="curve_fit values")
# for i, j in zip(year1[::2], yval[::2]):
#     plt.text(i, j-0.5, str(j)[:5], horizontalalignment="center", verticalalignment="bottom", fontsize=7)
plt.xlabel('x axis')
plt.ylabel('y axis')

plt.legend(loc=4)
plt.title("curve_fit")
plt.show()




