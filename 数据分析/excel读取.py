# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Author  : south(南风)
# @Time    : 2022/9/10 13:46
# @File    : excel读取.py
# @Software: PyCharm
# @Describe: 读取excel表格里面的内容
import pandas as pd

df = pd.read_excel("1.xlsx")
print(df.iloc[:, [11]].values)




