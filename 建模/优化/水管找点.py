"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/7/21 19:32
    @Author : south(南风)
    @File : test.py
    Describe:
    -*- coding: utf-8 -*-
"""
import networkx as nx
import itertools
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

from pylab import *
import random
import csv

"""
# 数据处理，得到两点间的距离
import numpy as np
import pandas as pd

df = pd.read_excel("坐标.xlsx")
num = [j for j in df["序号"]]
x = [j for j in df["X坐标"]]
y = [j for j in df["Y坐标"]]

# 两点间的距离
distance = []


for i in range(len(num)):
    col = [i]
    for j in range(len(num)):
        col.append('{:.2f}'.format(np.linalg.norm(np.array([x[i], y[i]]) - np.array([x[j], y[j]]))))

    distance.append(col)


column = num
column.insert(0, "序号")

df1 = pd.DataFrame(distance, columns=column)

df1.to_csv("距离.csv", index=False)
"""
#
# mpl.rcParams['font.sans-serif'] = ['SimHei']
# df = pd.read_excel("坐标.xlsx")
# # 提取位置坐标数据
# X = df[['X坐标', 'Y坐标']][1::].values
#
# # 设置聚类数目范围
# k_range = range(4, 30)
#
# # 存储不同聚类数目的轮廓系数
# s_scores = []
#
# # 对每个聚类数目进行聚类并计算轮廓系数
# for k in k_range:
#     # 创建KMeans对象并进行聚类
#     kmeans = KMeans(n_clusters=k, random_state=100).fit(X)
#     # 获取聚类标签
#     labels = kmeans.labels_
#     # 计算轮廓系数并存储
#     s_score = silhouette_score(X, labels)
#     s_scores.append(s_score)
#
# # 绘制聚类数目与轮廓系数的关系图
# plt.plot(k_range, s_scores, 'o-', label="聚类数目的轮廓系数")
# plt.legend()
# plt.xlabel('Number of clusters')
# plt.ylabel('Silhouette score')
# plt.show()
"""
# 选取合适的一级点个数

df = pd.read_excel("坐标.xlsx")
# 提取位置坐标数据
X = df[['X坐标', 'Y坐标']][1::].values

k = 15
mpl.rcParams['font.sans-serif'] = ['SimHei']
# 创建KMeans对象并进行聚类
kmeans = KMeans(n_clusters=k, random_state=100).fit(X)

# 获取每个一级供水站的位置坐标
centers = kmeans.cluster_centers_

y_pred = list(kmeans.labels_)

color = ["#" + "".join([random.choice("0123456789ABCDEF") for j in range(6)]) for i in range(15)]

fig, axi1 = plt.subplots(1)
for i in range(len(y_pred)):
    axi1.scatter(X[i, 0], X[i, 1],
                 marker='o',
                 c=color[y_pred[i]])
axi1.scatter(centers[:, 0], centers[:, 1], marker='x', s=100, c='black', label="中心点")
axi1.legend()
plt.ylabel("Y坐标")
plt.xlabel("X坐标")
plt.show()
"""


# df = pd.read_excel("标签.xlsx")
# # 提取位置坐标数据
# X = df[['X坐标', 'Y坐标']][1::].values
# k = 15
#
# # 创建KMeans对象并进行聚类
# kmeans = KMeans(n_clusters=k, random_state=100).fit(X)
#
#
# # 获取每个一级供水站的位置坐标
# centers = list(kmeans.cluster_centers_)
# dis1 = []
#
# for i in range(15):
#     df1 = df[df["标记"] == i]
#     num1 = [j for j in df1["序号"]]
#     x1 = [j for j in df1["X坐标"]]
#     y1 = [j for j in df1["Y坐标"]]
#     dis = []
#     for j in range(len(num1)):
#         dis.append([np.linalg.norm(np.array([x1[j], y1[j]]) - np.array([centers[i][0], centers[i][1]])), num1[j]])
#
#     dis1.append(dis)
#
# dian = []
# for i in range(15):
#     list1 = dis1[i]
#     list1.sort()
#     dian.append(list1[0][1])

# 暂时得到的一级点
# print(dian) # [127, 68, 138, 107, 116, 11, 61, 86, 10, 129, 76, 177, 21, 161, 37]
# one = [(0, 26, 31), (127, 7, 8), (68, 31, 41), (138, 15, 23), (107, 7, 34), (116, 27, 19), (11, 35, 42), (61, 35, 61), (86, 24, 49), (10, 36, 25), (129, 5, 17), (76, 18, 41), (177, 42, 43), (21, 24, 30), (161, 35, 15), (37, 18, 14)]
#
# G = nx.Graph()
# G.add_weighted_edges_from(one)

# nx.draw(G, pos=pos, with_labels=True)
#
# plt.show()

# df = pd.read_excel("标签.xlsx")
# x = 1
# df1 = df[(df["标记"] == x-1) & (df["序号"] != 127)]
# print(list(df1.loc[36, ["X坐标", "Y坐标"]]))

