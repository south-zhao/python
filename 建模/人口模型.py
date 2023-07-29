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
from scipy.optimize import curve_fit

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


def fund(x, xm, r0):
    return xm/(1+(xm/6.55-1)*np.exp((-r0)*(x-1959)))


popt, pcov = curve_fit(fund, year, num)
yvals = fund(year, popt[0], popt[1])
y2 = fund(2025, popt[0], popt[1])
print(y2)
Err = sum([(i - j)**2 for i, j in zip(yvals, num)])
print(Err)
plot1 = plt.plot(year, num, "*", label='original values')
plot2 = plt.plot(year, yvals, "r", label="curve_fit values")
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend(loc=4)
plt.title("curve_fit")
plt.show()


# 改进过后的
# z1 = np.polyfit(year, num, 3)
# p1 = np.poly1d(z1)
# yval = p1(year1)
# # Err = sum([(i - j)**2 for i, j in zip(yval, num)])
# # print(Err)
# plot1 = plt.plot(year, num, "*", label='original values')
# # for i, j in zip(year, num):
# #     plt.text(i, j, j, ha="center", va="bottom", fontsize=5)
# plot2 = plt.plot(year1, yval, "r", label="curve_fit values")
# # for i, j in zip(year1[::2], yval[::2]):
# #     plt.text(i, j-0.5, str(j)[:5], horizontalalignment="center", verticalalignment="bottom", fontsize=7)
# plt.xlabel('x axis')
# plt.ylabel('y axis')
#
# plt.legend(loc=4)
# plt.title("curve_fit")
# plt.show()


# 多项式拟合
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("人口数量表.csv")
year = df["年度"]
num = df["总人口(万人)"]

# 多项式
z1 = np.polyfit(year, num, 40)
p1 = np.poly1d(z1)
yval = p1(year)
Err = sum([(i - j)**2 for i, j in zip(yval, num)])
print(Err)
plot1 = plt.plot(year, num, "*", label='original values')

plot2 = plt.plot(year, yval, "r", label="curve_fit values")

plt.xlabel('x axis')
plt.ylabel('y axis')

plt.legend()
plt.title("curve_fit")
plt.show()
print(num)
print(yval)
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv("人口数量表.csv")
year = df["年度"]
num = df["总人口(亿人)"]
"""
x1 = np.linspace(1949, 2022, 50)

f2 = interp1d(np.array(year), np.array(num), 'cubic')
y2 = f2(x1)

z1 = np.polyfit(x1, y2, 5)
p1 = np.poly1d(z1)
yval = p1(x1)
Err = sum([(i - j)**2 for i, j in zip(yval, num)])
print(Err/len(x1))
plot1 = plt.plot(x1, y2, "*", label='original values')

plot2 = plt.plot(x1, yval, "r", label="curve_fit values")

plt.xlabel('x axis')
plt.ylabel('y axis')

plt.legend()
plt.title("curve_fit")
plt.show()

print(y2)
print(yval)
"""

"""
# 多项式回归
test = [2023, 2024, 2025, 2026, 2027]
dataset_length = len(year)
test_length = len(test)
# 将数据转化为numpy数组
datasets_X = np.array(year).reshape([dataset_length, 1])
test_X = np.array(test).reshape([test_length, 1])
datasets_Y = np.array(num)
for i in range(2, 5):
# 构造多项式特征
    poly_reg = PolynomialFeatures(degree=3)
    X_poly = poly_reg.fit_transform(datasets_X)

    # 使用线性回归模型学习X_poly和datasets_Y之间的映射关系
    lin_reg = LinearRegression()
    lin_reg.fit(X_poly, datasets_Y)

    # 数据可视化
    # 蓝色显示训练数据点
    plt.scatter(datasets_X, datasets_Y, color='blue', label="origin data")

    # X轴
    my_x_ticks = np.arange(1949, 2023, 3)
    plt.xticks(my_x_ticks)


    # 绘制线
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False
    X = np.arange(1949, 2023).reshape([-1, 1])
    yval = lin_reg.predict(poly_reg.fit_transform(X))
    plt.plot(X, yval, color='red', label="predict data")
    plt.xticks(rotation=45)
    plt.xlabel('Years')
    plt.ylabel('People num(/亿)')
    plt.title(f"参数为{i}拟合结果")
    plt.legend()
    # plt.grid()
    plt.show()

# 数据建模
# 构造三次多项式特征
poly_reg = PolynomialFeatures(degree=3)

X_poly = poly_reg.fit_transform(datasets_X)

# 使用线性回归模型学习X_poly和datasets_Y之间的映射关系
lin_reg_3 = LinearRegression()
lin_reg_3.fit(X_poly, datasets_Y)
# print(lin_reg_3.coef_)
# print(lin_reg_3.intercept_)
data = poly_reg.fit_transform(test_X)
pred = lin_reg_3.predict(data)
plt.scatter(test_X, pred, color='green', label="predict data")
plt.scatter(datasets_X, datasets_Y, color='blue', label="origin data")
# X轴
my_x_ticks = np.arange(1949, 2026, 3)
plt.xticks(my_x_ticks)

# 绘制线
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
plt.rcParams['axes.unicode_minus'] = False
X = np.arange(1949, 2023).reshape([-1, 1])
yval = lin_reg_3.predict(poly_reg.fit_transform(X))
plt.plot(X, yval, color='red', label="拟合")
plt.xticks(rotation=45)
plt.xlabel('Years')
plt.ylabel('People num(/亿)')
plt.legend()
# plt.grid()
plt.show()
print("5年短期预测结果:")
for i, j in zip(pred, test):
    print("{}年的预测人口为{:.4f}亿".format(j, i))
5年短期预测结果:
2023年的预测人口为13.9450亿
2024年的预测人口为13.9301亿
2025年的预测人口为13.9079亿
2026年的预测人口为13.8784亿
2027年的预测人口为13.8414亿
# [ 0.00000000e+00 -2.84191860e+02  1.43998351e-01 -2.43074545e-05]
# 186862.5904222844
"""

"""
# 长期预测
test1 = [2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032]

def fund(x, xm, r0):
    return xm/(1+(xm/5.4167-1)*np.exp((-r0)*(x-1949)))


popt, pcov = curve_fit(fund, year, num)
yvals = fund(year, *popt)
y2 = fund(np.array(test1), popt[0], popt[1])
plt.plot(year, num, "*", label='original values')
plt.plot(year, yvals, "r", label="curve_fit values")
plt.scatter(test1, y2, color='blue', label="predict data")
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.title("curve_fit")
plt.show()
print("10年长期预测：")
for i, j in zip(test1, y2):
    print("{}年预测人口为{:.4f}亿".format(i, j))
    10年长期预测：
2023年预测人口为14.4325亿
2024年预测人口为14.4949亿
2025年预测人口为14.5557亿
2026年预测人口为14.6147亿
2027年预测人口为14.6722亿
2028年预测人口为14.7279亿
2029年预测人口为14.7821亿
2030年预测人口为14.8348亿
2031年预测人口为14.8859亿
2032年预测人口为14.9355亿
# print(popt[0], popt[1])
# 16.40955829574329 0.03642713934964601
"""


