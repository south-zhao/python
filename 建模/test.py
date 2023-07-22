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
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


"""
数据处理，得到两点间的距离
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
        col.append(np.linalg.norm(np.array([x[i], y[i]]) - np.array([x[j], y[j]])))

    distance.append(col)


column = num
column.insert(0, "序号")

df1 = pd.DataFrame(distance, columns=column)

df1.to_csv("距离.csv", index=False)
"""

df = pd.read_excel("坐标.xlsx")
# num = [j for j in df["序号"]]
# x = [j for j in df["X坐标"]]
# y = [j for j in df["Y坐标"]]
#
#
# pos = {}
# for i in range(len(num)):
#     pos[num[i]] = [x[i], y[i]]
#
# G = nx.Graph()
# G.add_nodes_from(num)
#
# nx.draw(G, pos=pos, with_labels=True)
#
# plt.show()
# 提取位置坐标数据
X = df[['X坐标', 'Y坐标']][1::].values

# 设置聚类数目范围
k_range = range(2, 30)

# 存储不同聚类数目的轮廓系数
s_scores = []

# 对每个聚类数目进行聚类并计算轮廓系数
for k in k_range:
    # 创建KMeans对象并进行聚类
    kmeans = KMeans(n_clusters=k, random_state=100).fit(X)
    # 获取聚类标签
    labels = kmeans.labels_
    # 计算轮廓系数并存储
    s_score = silhouette_score(X, labels)
    s_scores.append(s_score)

# 绘制聚类数目与轮廓系数的关系图
plt.plot(k_range, s_scores, 'o-')
plt.xlabel('Number of clusters')
plt.ylabel('Silhouette score')
plt.show()

# k = 4

# 创建KMeans对象并进行聚类
# kmeans = KMeans(n_clusters=k, random_state=0).fit(X)

# 为每个地点分配一个一级供水站的标签
# labels = kmeans.predict(X)

# 获取每个一级供水站的位置坐标
# centers = kmeans.cluster_centers_
# print(centers)

# y_pred = kmeans.labels_  # 获取训练后对象的每个样本的标签
# centtrod = kmeans.cluster_centers_
# color = ['red', 'pink', 'orange', 'blue', 'purple']
# fig, axi1 = plt.subplots(1)
# for i in range(len(y_pred)):
#     axi1.scatter(X[i, 0], X[i, 1],
#                  marker='o',
#                  c=color[y_pred[i]])
# axi1.scatter(centtrod[:, 0], centtrod[:, 1], marker='x', s=100, c='black')
# plt.show()
