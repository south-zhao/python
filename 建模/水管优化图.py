import numpy as np
import csv
import networkx as nx
import pandas as pd
from pylab import *


class MiniTree(object):
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

    def create_mini_tree(self, start):
        visited = []
        list1 = []
        # 标记已访问
        visited.append(start)
        v1, v2 = None, None
        while len(visited) < len(self.vertex):
            min_weight = float('inf')
            for v in visited:
                for i in range(len(self.vertex)):
                    if i not in visited and self.weight[v][i] < min_weight:
                        v1 = v
                        v2 = i
                        min_weight = self.weight[v][i]
            visited.append(v2)
            list1.append((self.vertex[v1], self.vertex[v2], self.weight[v1][v2]))
        return list1


if __name__ == '__main__':
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    df = pd.read_excel("181个坐标点表.xlsx")
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

    df1.to_csv("181个坐标点距离表.csv", index=False)
    # 修正前的
    # 中心点和一级点的序号
    list1 = [0, 127, 68, 138, 107, 116, 11, 61, 86, 10, 129, 76, 177, 21, 161, 37]
    list1_n = [i for i in range(181) if i not in list1]

    # 修正后的
    list_n1 = [0, 127, 68, 138, 107, 116, 11, 61, 86, 10, 129, 76, 177, 21, 161, 37, 45, 91, 53, 147, 83]
    list1_nn = [i for i in range(181) if i not in list_n1]
    df_n = pd.read_excel("聚类后的181个坐标点表.xlsx")

    with open("181个坐标点距离表.csv", encoding="utf-8") as f:
        rows = [row for row in csv.reader(f)][1::]

    list3 = []

    pos = {}

    for x in range(len(list1)):
        if x == 0:
            dis = []
            for i in list1:
                col = []
                for j in list1:
                    col.append(float(rows[i][j + 1]))
                dis.append(col)
            mini_tree = MiniTree(list1, dis)
            list2 = mini_tree.create_mini_tree(0)
            # 中心点和一级点的坐标
            pos = {0: [26, 31], 127: [7, 8], 68: [31, 41], 138: [15, 23], 107: [7, 34], 116: [27, 19], 11: [41, 31],
                   61: [35, 51], 86: [24, 49], 10: [36, 25], 129: [5, 17], 76: [18, 41], 177: [42, 43], 21: [24, 30],
                   161: [35, 15], 37: [18, 14]}
            list3.extend(list2)

        else:
            dis = []
            df1_n = df_n[(df_n["标记"] == x - 1) & (df_n["序号"] != list1[x])]
            li = list(df1_n["序号"])
            li.insert(0, list1[x])
            for i1 in li:
                col = []
                for j1 in li:
                    col.append(float(rows[i1][j1 + 1]))
                dis.append(col)
            for z in li[1::]:
                pos[z] = list(df1_n.loc[z, ["X坐标", "Y坐标"]])

            mini_tree = MiniTree(li, dis)
            list2 = mini_tree.create_mini_tree(0)
            list3.extend(list2)

    # 修正前的图
    """
    G = nx.DiGraph()
    G.add_weighted_edges_from(list3)
    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_nodes(G, pos, nodelist=list1[:1], node_color="red", label="中心供水点")
    nx.draw_networkx_nodes(G, pos, nodelist=list1[1:], label="一级供水点")
    nx.draw_networkx_nodes(G, pos, nodelist=list1_n, node_color="orange", label="二级供水点")
    plt.legend()
    plt.show()
    """
    # 修正后的图
    H = nx.DiGraph()
    H.add_weighted_edges_from(list3)
    H.add_edge(86, 53, weight=3.16)
    H.remove_edge(7, 53)
    nx.draw(H, pos, with_labels=True)
    nx.draw_networkx_nodes(H, pos, nodelist=list_n1[:1], node_color="red", label="中心供水点")
    nx.draw_networkx_nodes(H, pos, nodelist=list_n1[1:], label="一级供水点")
    nx.draw_networkx_nodes(H, pos, nodelist=list1_nn, node_color="orange", label="二级供水点")
    plt.legend()
    plt.show()

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

    # 求解二级管道的长度
    length2 = 0
    for i in list3[15:]:
        length2 += i[2]

    length2 = length2 - a - 2.248

    money = (length1 * 1291 + length2 * 445) * 1000

    print("花费的总费用为：{:.2f}".format(money))
    print("总长度为：{:.2f}".format(length1 + length2))
    print("一级管道长度为：{:.2f}".format(length1))
    print("二级管道长度为：{:.2f}".format(length2))


