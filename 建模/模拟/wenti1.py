"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time :  2023/8/28 10:45
    @Author : south(南风)
    @File : wenti1.py
    Describe:
    -*- coding: utf-8 -*-
"""
import pandas as pd
import statsmodels.api as sm

df = pd.read_excel("表1 指导教师信息与选队意愿.xls")
df = df.iloc[1:36]
list2 = []
for i in df.values:
    list_in = [1 if i[1] == "男" else 0, 0 if i[2] == "硕士" else 1]
    if i[3] == "讲师":
        list_in.append(0)
    elif i[3] == "副教授":
        list_in.append(1)
    else:
        list_in.append(2)
    list_in.append(i[4])
    list_in.append(i[6])
    list_in.append(i[9])
    list2.append(list_in)
df1 = pd.DataFrame(list2)
x = sm.add_constant(df1.iloc[:, :5])  # 生成自变量
y = df1[5]  # 生成因变量
model = sm.OLS(y, x)  # 生成模型
result = model.fit()  # 模型拟合
result.summary()  # 模型描述
print(result.params)
