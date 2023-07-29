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
import random
import numpy as np
import pandas as pd
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sympy import *


df = pd.read_csv("人口数量表.csv")
year = df["年度"]
num = df["总人口(亿人)"]


# 多项式回归
test = [2023, 2024, 2025, 2026, 2027]
dataset_length = len(year)
test_length = len(test)
# 将数据转化为numpy数组
datasets_X = np.array(year).reshape([dataset_length, 1])
test_X = np.array(test).reshape([test_length, 1])
datasets_Y = np.array(num)
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
plt.scatter(test_X, pred, color='green', label="预测数据")
plt.plot(datasets_X, datasets_Y, '*', label="原始数据")
# X轴
my_x_ticks = np.arange(1949, 2028, 3)
plt.xticks(my_x_ticks)

# 绘制线
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
plt.rcParams['axes.unicode_minus'] = False
X = np.arange(1949, 2023).reshape([-1, 1])
yval = lin_reg_3.predict(poly_reg.fit_transform(X))
plt.plot(X, yval, color='red', label="拟合数据")
plt.xticks(rotation=45)
plt.xlabel('年份')
plt.ylabel('人口总数(/亿)')
plt.legend()
# plt.grid()
plt.show()
print("5年短期预测结果:")
for i, j in zip(pred, test):
    print("{}年的预测人口为{:.4f}亿".format(j, i))
# 5年短期预测结果:
# 2023年的预测人口为13.9450亿
# 2024年的预测人口为13.9301亿
# 2025年的预测人口为13.9079亿
# 2026年的预测人口为13.8784亿
# 2027年的预测人口为13.8414亿
# [ 0.00000000e+00 -2.84191860e+02  1.43998351e-01 -2.43074545e-05]
# 186862.5904222844


df1 = pd.read_excel("长期预测数据.xlsx")

people = df1['people']
year1 = df1["year"]
medice1 = df1["medice"]
money1 = df1["money"]
born1 = df1["born"]
death1 = df1["death"]
add1 = df1["add"]
boy1 = df1["boy"]
city1 = df1["city"]



def looper(limit):
    col = ['medice', 'money', 'born', 'death', 'add', 'old', 'boy', 'girl', 'city', 'village']
    for i in range(len(col)):
        x = 'people ~ ' + " + ".join(col)
        lm = ols(x, data=df1).fit()
        pval = lm.pvalues
        pmax = max(pval)
        if pmax > limit:
            ind = pval.idxmax()
            col.remove(ind)
        else:
            return lm


lm = looper(0.05)
list1 = list(lm.params)
medice, money, born, death, add, boy, city = symbols('medice money born death add boy city')

eq = list1[0] + list1[1] * medice + list1[2] * money + list1[3] * born + list1[4] * death + list1[5] * add + list1[6] * boy + list1[7] * city
y = [2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032]
pre_data = []

# medice预测
z1 = np.polyfit(year1[13:], medice1[13:], 2)
p1 = np.poly1d(z1)
yval = p1(y)
pre_data.append(list(yval))
# '''
name = [money1, born1, death1, add1, boy1, city1]
for i in range(6):
    if i == 3:
        lis = [i - j for i, j in zip(pre_data[2], pre_data[3])]
        pre_data.append(lis)
    elif i == 2:
         z11 = np.polyfit(year1, name[i], 2)
         p11 = np.poly1d(z11)
         yval1 = p11(y)
         pre_data.append(list(yval1))
    else:
        z11 = np.polyfit(year1, name[i], 3)
        p11 = np.poly1d(z11)
        yval1 = p11(y)
        pre_data.append(list(yval1))
res = []
for i in range(10):
    l = ['medice', 'money', 'born', 'death', 'add', 'boy', 'city']
    dict1 = {'medice': 0, 'money': 0, 'born': 0, 'death': 0, 'add': 0, 'boy': 0, 'city': 0}
    for j in range(7):
        dict1[l[j]] = pre_data[j][i]

    res.append(eq.subs({medice: dict1['medice'], money: dict1['money'], born: dict1['born'], death: dict1['death'], add: dict1['add'], boy: dict1['boy'], city: dict1['city']}))

my_x_ticks = np.arange(1990, 2033, 2)


res1 = []
for i in range(len(people)):
    res1.append(eq.subs({medice: medice1[i], money: money1[i], born: born1[i], death: death1[i], add: add1[i], boy: boy1[i], city: city1[i]}))

plt.xticks(my_x_ticks)
plt.plot(year1, people, '*', label="原始数据")
plt.plot(year1, res1, 'r', label="拟合数据")
plt.scatter(y, res, color='green', label="预测数据")
plt.xticks(rotation=45)
plt.legend()
plt.xlabel("年份")
plt.ylabel("人口总数(/亿)")
plt.show()

color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in range(7)]
label = ["医疗数目", "国民生产总值", "出生率", "死亡率", "增长率", "男比重", "城镇化"]

# for n in range(7):
#     if n == 1:
#         continue
plt.plot(y, pre_data[1], color=color[1], label=label[1])

plt.xlabel("年份")
plt.title("相关数据未来十年预测图")
plt.legend()
plt.show()
print("10年长期预测：")
for m, n in zip(y, res):
    print("{}年人口数量为{:.4f}亿".format(m, n))

