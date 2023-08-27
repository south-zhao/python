"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/7/23 10:33
    @Author : south(南风)
    @File : 1.py
    Describe:
    -*- coding: utf-8 -*-
"""
import csv

import networkx as nx
import pandas as pd
from matplotlib import pyplot as plt


class MiniTree(object):
    def __init__(self, vertex, weight):
        """
        最小生成树
        """
        self.vertex = vertex
        self.weight = weight

    def create_mini_tree(self, start):
        """
        最小生成树
        :param start:
        :return:
        """
        visited = []
        list1 = []
        # 标记已访问
        visited.append(start)
        v1, v2 = None, None
        while len(visited) < len(self.vertex):
            min_weight = float('inf')
            for v in visited:
                for i in range(len(self.vertex)):
                    # 边没有被访问过且 权重较小
                    if i not in visited and self.weight[v][i] < min_weight:
                        v1 = v
                        v2 = i
                        min_weight = self.weight[v][i]
            visited.append(v2)
            # print('%f -> %f weight = %f' % (self.vertex[v1], self.vertex[v2], self.weight[v1][v2]))
            list1.append((self.vertex[v1], self.vertex[v2], self.weight[v1][v2]))
        return list1


if __name__ == '__main__':
    list1 = [0, 127, 68, 138, 107, 116, 11, 61, 86, 10, 129, 76, 177, 21, 161, 37]
    df = pd.read_excel("标签.xlsx")


    with open("距离.csv", encoding="utf-8") as f:
        rows = [row for row in csv.reader(f)][1::]
    list3 = []
    pos = {}
    # 一级点
    for x in range(len(list1)-4):
        if x == 0:
            dis = []
            for i in list1:
                col = []
                for j in list1:
                    col.append(float(rows[i][j+1]))
                dis.append(col)
            mini_tree = MiniTree(list1, dis)
            list2 = mini_tree.create_mini_tree(0)
            pos = {0: [26, 31], 127: [7, 8], 68: [31, 41], 138: [15, 23], 107: [7, 34], 116: [27, 19], 11: [41, 31], 61: [35, 51], 86: [24, 49], 10: [36, 25], 129: [5, 17], 76: [18, 41], 177: [42, 43], 21: [24, 30], 161: [35, 15], 37: [18, 14]}
            list3.extend(list2)

        else:
            dis = []
            df1 = df[(df["标记"] == x-1) & (df["序号"] != list1[x])]
            li = list(df1["序号"])
            li.insert(0, list1[x])
            for i1 in li:
                col = []
                for j1 in li:
                    col.append(float(rows[i1][j1+1]))
                dis.append(col)
            for z in li[1::]:
                pos[z] = list(df1.loc[z, ["X坐标", "Y坐标"]])

            mini_tree = MiniTree(li, dis)
            list2 = mini_tree.create_mini_tree(0)
            list3.extend(list2)


    G = nx.DiGraph()
    G.add_weighted_edges_from(list3)
    G.add_edge(86, 53, weight=3.16)
    G.remove_edge(7, 53)
    # pos = {0: [26, 31], 127: [7, 8], 68: [31, 41], 138: [15, 23], 107: [7, 34], 116: [27, 19], 11: [41, 31], 61: [35, 51], 86: [24, 49], 10: [36, 25], 129: [5, 17], 76: [18, 41], 177: [42, 43], 21: [24, 30], 161: [35, 15], 37: [18, 14]}
    nx.draw(G, pos, with_labels=True)

    # 二级点
    # plt.show(）

    # 求解一级管道的长度
    length1 = 0
    a = 0
    for i in list3:
        if i[0] == 68 and i[1] == 45:
            a += i[2]
        if i[0] == 107 and i[1] == 91:
            a += i[2]
        if i[0] == 10 and i[1] == 147:
            a += i[2]
        if i[0] == 76 and i[1] == 83:
            a += i[2]

    for i in list3[:15]:
        length1 += i[2]

    length1 = length1 + a + 3.16

    length2 = 0
    for i in list3[15:]:
        length2 += i[2]

    length2 = length2 - a - 2.24

    money = (length1 * 1291 + length2 * 445) * 1000

    print(money)

    print(length1 + length2)

    print(list3)
