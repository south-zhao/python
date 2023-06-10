"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/5/27 16:19
    @Author : south(南风)
    @File : test1.py
    Describe:
    -*- coding: utf-8 -*-
"""
# import networkx as nx
# import matplotlib.pyplot as plt
# # 创建空的网格
# G=nx.Graph()
# # 添加节点
# G.add_node('JFK')
# G.add_nodes_from(['SFO','LAX','ATL','FLO','DFW','HNL'])
#
# # 添加连线
# G.add_edges_from([('JFK','SFO'),('JFK','LAX'),('LAX','ATL'),('FLO','ATL'),('ATL','JFK'),('FLO','JFK'),('DFW','HNL')])
# G.add_edges_from([('OKC','DFW'),('OGG','DFW'),('OGG','LAX')])
#
# nx.draw_networkx(G,pos=nx.circular_layout(G),with_labels=True,alpha=0.5,node_color='yellow',node_shape='s',
#                  linewidths=4,
#                  width=2,edge_color='blue',style='--',
#                  font_size=15,font_color='blue',font_family='SimHei')
# # pos选用圆形样式，with_labels=True在节点上绘制标签，alpha=0.5节点透明度
# #linewidths=4节点边框宽度为4，node_color='yellow'节点颜色设为黄色，node_shape='s'节点的形状设为正方形
# # width=2边的线宽2,edge_color='blue'设置边的颜色,style='--'边的线样式，
# # font_size=15设置标签字号大小,font_color='blue'设置标签字体颜色,font_family='SimHei'设置标签字体
# plt.show()
import pandas as pd
import numpy as np
import re
import datetime
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
import json
# def rewrite():
#     df = pd.read_excel("个人消费数据\male\{}".format(file))
df = pd.read_excel("5044.xlsx")
#     df = pd.read_excel(r"个人消费数据\female\{}".format(filename))
morning = []
noon = []
afternoon = []
for i in range(len(df)):
    if datetime.datetime(1900, 1, 1, 5).time() < datetime.datetime.strptime(df.loc[i][0].split()[1], "%H:%M:%S").time() < datetime.datetime(1900, 1, 1, 11).time():
        morning.append(df.loc[i][2])
    elif datetime.datetime(1900, 1, 1, 11).time() < datetime.datetime.strptime(df.loc[i][0].split()[1], "%H:%M:%S").time() < datetime.datetime(1900, 1, 1, 17).time():
        noon.append(df.loc[i][2])
    elif datetime.datetime(1900, 1, 1, 17).time() < datetime.datetime.strptime(df.loc[i][0].split()[1], "%H:%M:%S").time() < datetime.datetime(1900, 1, 1, 23, 59, 59).time():
        afternoon.append(df.loc[i][2])
a = df.loc[df["种类"].isnull()].index.tolist()
b = df.loc[df["种类"]=="待定"].index.tolist()
c = df.loc[df["种类"]=="一层待定"].index.tolist()
pat = re.compile("一层[\u4e00-\u9fa5]+")
morning1 = []
afternoon1 = []
noon1 = []
for i in morning:
    if str(i) == "nan":
        continue
    res = pat.findall(i)
    if len(res) > 0 and res[0] == "一层待定":
        res.remove("一层待定")
    morning1.extend(res)
for i in afternoon:
    if str(i) == "nan":
        continue
    res = pat.findall(i)
    if len(res) > 0 and res[0] == "一层待定":
        res.remove("一层待定")
    afternoon1.extend(res)
for i in noon:
    if str(i) == "nan":
        continue
    res = pat.findall(i)
    if len(res) > 0 and res[0] == "一层待定":
        res.remove("一层待定")
    noon1.extend(res)
fdist_m1 = FreqDist(morning1)
fdist_m11 = list(fdist_m1.most_common())
fdist_n1 = FreqDist(noon1)
fdist_n11 = list(fdist_n1.most_common())
fdist_a1 = FreqDist(afternoon1)
fdist_a11 = list(fdist_a1.most_common())
a.extend(b)
fdist_m = FreqDist(morning)
fdist_m1 = list(fdist_m.most_common())
fdist_n = FreqDist(noon)
fdist_n1 = list(fdist_n.most_common())
fdist_a = FreqDist(afternoon)
fdist_a1 = list(fdist_a.most_common())
if str(fdist_a1[0][0]) == "nan":
    fdist_a1.pop(0)
if str(fdist_m1[0][0]) == "nan":
    fdist_m1.pop(0)
if str(fdist_n1[0][0]) == "nan":
    fdist_n1.pop(0)
for i in a:
    if datetime.datetime(1900, 1, 1, 5).time() < datetime.datetime.strptime(df.iloc[i, 0].split()[1], "%H:%M:%S").time() < datetime.datetime(1900, 1, 1, 11).time():
        df.iloc[i, 2] = fdist_m1[0][0]
    elif datetime.datetime(1900, 1, 1, 11).time() < datetime.datetime.strptime(df.iloc[i, 0].split()[1], "%H:%M:%S").time() < datetime.datetime(1900, 1, 1, 17).time():
        df.iloc[i, 2] = fdist_n1[0][0]
    elif datetime.datetime(1900, 1, 1, 17).time() < datetime.datetime.strptime(df.iloc[i, 0].split()[1], "%H:%M:%S").time() < datetime.datetime(1900, 1, 1, 23, 59, 59).time():
        df.iloc[i, 2] = fdist_a1[0][0]
for i in c:
    if datetime.datetime(1900, 1, 1, 5).time() < datetime.datetime.strptime(df.iloc[i, 0].split()[1], "%H:%M:%S").time() < datetime.datetime(1900, 1, 1, 11).time():
        if len(fdist_m11) == 0:
            if len(fdist_a11) == 0:
                if len(fdist_n11) == 0:
                    df.iloc[i, 2] = fdist_m1[0][0]
                else:
                    df.iloc[i, 2] = fdist_n11[0][0]
            else:
                df.iloc[i, 2] = fdist_a11[0][0]
        else:
            df.iloc[i, 2] = fdist_m11[0][0]
    elif datetime.datetime(1900, 1, 1, 11).time() < datetime.datetime.strptime(df.iloc[i, 0].split()[1], "%H:%M:%S").time() < datetime.datetime(1900, 1, 1, 17).time():
        if len(fdist_n11) == 0:
            if len(fdist_a11) == 0:
                if len(fdist_m11) == 0:
                    df.iloc[i, 2] = fdist_n1[0][0]
                else:
                    df.iloc[i, 2] = fdist_m11[0][0]
            else:
                df.iloc[i, 2] = fdist_a11[0][0]
        else:
            df.iloc[i, 2] = fdist_n11[0][0]
    elif datetime.datetime(1900, 1, 1, 17).time() < datetime.datetime.strptime(df.iloc[i, 0].split()[1], "%H:%M:%S").time() < datetime.datetime(1900, 1, 1, 23, 59, 59).time():
        if len(fdist_a11) == 0:
            if len(fdist_m11) == 0:
                if len(fdist_n11) == 0:
                    df.iloc[i, 2] = fdist_a1[0][0]
                else:
                    df.iloc[i, 2] = fdist_n11[0][0]
            else:
                df.iloc[i, 2] = fdist_m11[0][0]
        else:
            df.iloc[i, 2] = fdist_a11[0][0]
print(df)
