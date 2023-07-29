"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/7/27 8:15
    @Author : south(南风)
    @File : question3.py
    Describe:
    -*- coding: utf-8 -*-
"""
import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
from sympy import *


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
# 原方程
eq = list1[0] + list1[1] * medice + list1[2] * money + list1[3] * born + list1[4] * death + list1[5] * add + list1[6] * boy + list1[7] * city
# 更改医疗
eq1 = list1[0] + list1[1] * medice * 1.5 + list1[2] * money + list1[3] * born + list1[4] * death + list1[5] * add + list1[6] * boy + list1[7] * city
# 男女
eq2 = list1[0] + list1[1] * medice + list1[2] * money + list1[3] * born + list1[4] * death + list1[5] * add + list1[6] * boy * 0.975 + list1[7] * city
# 城镇化
eq3 = list1[0] + list1[1] * medice + list1[2] * money + list1[3] * born + list1[4] * death + list1[5] * add + list1[6] * boy + list1[7] * city * 1.07

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
res1 = []
res2 = []
res3 = []

for i in range(10):
    l = ['medice', 'money', 'born', 'death', 'add', 'boy', 'city']
    dict1 = {'medice': 0, 'money': 0, 'born': 0, 'death': 0, 'add': 0, 'boy': 0, 'city': 0}
    for j in range(7):
        dict1[l[j]] = pre_data[j][i]

    res1.append(eq1.subs({medice: dict1['medice'], money: dict1['money'], born: dict1['born'], death: dict1['death'], add: dict1['add'], boy: dict1['boy'], city: dict1['city']}))
    res2.append(eq2.subs({medice: dict1['medice'], money: dict1['money'], born: dict1['born'], death: dict1['death'], add: dict1['add'], boy: dict1['boy'], city: dict1['city']}))
    res3.append(eq3.subs({medice: dict1['medice'], money: dict1['money'], born: dict1['born'], death: dict1['death'], add: dict1['add'], boy: dict1['boy'], city: dict1['city']}))
    res.append(eq.subs({medice: dict1['medice'], money: dict1['money'], born: dict1['born'], death: dict1['death'], add: dict1['add'], boy: dict1['boy'], city: dict1['city']}))


print("10年长期预测：")
for m, n in zip(y, res):
    print("{}年人口数量为{:.4f}亿".format(m, n))
print("医疗条件变好后10年长期预测：")
for m, n in zip(y, res1):
    print("{}年人口数量为{:.4f}亿".format(m, n))
print("男女比例接近平衡后10年长期预测：")
for m, n in zip(y, res2):
    print("{}年人口数量为{:.4f}亿".format(m, n))
print("城镇化加快后10年长期预测：")
for m, n in zip(y, res3):
    print("{}年人口数量为{:.4f}亿".format(m, n))

