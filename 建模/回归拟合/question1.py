# dd为输入数据表，m为参数列，默认为0，如果flag为非None，则可任意值，无意义
# flag 标识参考列方式，默认None是按列取值
# flag = 'MAX' 按最大值取值
# flag = 'MIN' 按最小值取值
import matplotlib.pyplot as plt
import pandas as pd
from numpy import *


def GRA(dd, m=0, flag=None):
    # 读取为df格式
    # dd = dimensionlessProcessing(dd)

    x_mean = dd.mean(axis=0)
    # print(x_mean)
    for i in range(len(dd.columns)):
        dd.iloc[:, i] = dd.iloc[:, i] / x_mean[i]

    # 参考要素
    if flag == None:
        std = dd.iloc[:, m]  # 为参考要素
        dd.drop(dd.columns[m], axis=1, inplace=True)
    elif flag == 'MAX':
        std = dd.max(axis=1)
    elif flag == 'MIN':
        std = dd.min(axis=1)
    else:
        print('flag eorro!')
        return None

    # print(std)

    # print(dd)
    shape_n, shape_m = dd.shape[0], dd.shape[1]  # 计算行列

    # 与参考要素比较，相减
    a = zeros([shape_m, shape_n])

    for i in range(shape_m):
        for j in range(shape_n):
            a[i, j] = abs(dd.iloc[j, i] - std[j])

    # 取出矩阵中最大值与最小值
    # print(a)
    c, d = a.max().max(), a.min().min()
    # print(c, d)

    # 计算关联系数
    result = (d + 0.5 * c) / (a + 0.5 * c)

    # 求均值，得到灰色关联度,并返回
    result_list = [mean(result[i, :]) for i in range(shape_m)]

    return pd.DataFrame(result_list)


x = pd.read_excel("第一问数据.xlsx")
dd = x.iloc[:, [1, 4, 5, 6, 7, 8, 9, 10, 11]]
dd1 = x.iloc[:, 1:3]
dd2 = x.iloc[:, [1, 3]]

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
plt.rcParams['axes.unicode_minus'] = False
dd.plot(kind='line', figsize=(8, 6), grid=True, marker='o')
plt.xticks(range(0, 33, 1), range(1990, 2023, 1), rotation=45)
plt.xlabel("年份")
plt.ylabel("百分比")
plt.legend(loc=1)
plt.show()

dd1.plot(kind='line', figsize=(8, 6), grid=True, marker='o')
plt.xticks(range(0, 33, 1), range(1990, 2023, 1), rotation=45)
plt.xlabel("年份")
plt.ylabel("数量（/亿）")
plt.show()

dd2.plot(kind='line', figsize=(8, 6), grid=True, marker='o')
plt.xticks(range(0, 33, 1), range(1990, 2023, 1), rotation=45)
plt.xlabel("年份")
plt.ylabel("金额（/亿元）")
plt.show()

df = x.iloc[:, [1, 4, 5, 6, 7, 8, 9, 10, 11]].copy()
data_gra = GRA(df, m=0)
# print(data_gra)
df1 = x.iloc[:, 1:3].copy()
data_gra1 = GRA(df1, m=0)
# print(data_gra1)
df2 = x.iloc[:, [1, 3]].copy()
data_gra2 = GRA(df2, m=0)
# print(data_gra2)
# 关联度结果
res = []
res.extend(data_gra1[0])
res.extend(data_gra2[0])
res.extend(data_gra[0])
name = list(x)[2:]
dict1 = dict(zip(name, res))
dict1 = sorted(dict1.items(), key=lambda d: d[1], reverse=True)
print("各因素的关联度为：")
for i in dict1:
    print(i[0], i[1])
