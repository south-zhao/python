"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/5/28 15:12
    @Author : south(南风)
    @File : TSP.py
    Describe:
    -*- coding: utf-8 -*-
"""
# import numpy as np
#
# # 定义城市和坐标
# cities = ['A', 'B', 'C', 'D', 'E']
# coordinates = np.array([[0, 0], [1, 2], [3, 1], [4, 3], [2, 4]])
#
# # 计算距离矩阵
# num_cities = len(cities)
# distances = np.zeros((num_cities, num_cities))
# for i in range(num_cities):
#     for j in range(i + 1, num_cities):
#         distances[i, j] = np.linalg.norm(coordinates[i] - coordinates[j])
#         distances[j, i] = distances[i, j]
#
# # 打印距离矩阵
# print("距离矩阵：")
# print(distances)


import networkx as nx
import itertools
import matplotlib.pyplot as plt

# 定义城市和距离矩阵
cities = ['A', 'B', 'C', 'D', 'E']
distances = [[0, 4, 2, 5, 6],
             [4, 0, 3, 2, 3],
             [2, 3, 0, 4, 5],
             [5, 2, 4, 0, 3],
             [6, 3, 5, 3, 0]]

# 创建完全图
G = nx.Graph()
G.add_nodes_from(cities)
for i, j in itertools.combinations(range(len(cities)), 2):
    G.add_edge(cities[i], cities[j], weight=distances[i][j])

H = nx.Graph()
H.add_nodes_from(cities)
H.add_edge(cities[0], cities[1])
H.add_edge(cities[1], cities[3])
H.add_edge(cities[3], cities[4])
H.add_edge(cities[4], cities[2])
H.add_edge(cities[2], cities[0])
nx.draw(H, with_labels=True)
 
# 求解旅行商问题
shortest_tour = None
min_tour_length = float('inf')
for permutation in itertools.permutations(cities):
    tour_length = sum([G[permutation[i]][permutation[i+1]]['weight'] for i in range(len(cities)-1)])
    tour_length += G[permutation[-1]][permutation[0]]['weight']
    if tour_length < min_tour_length:
        shortest_tour = permutation
        min_tour_length = tour_length

# 打印结果
print("最短旅行路径：", shortest_tour)
print("路径长度：", min_tour_length)
# nx.draw(G, with_labels=True)
plt.show()

