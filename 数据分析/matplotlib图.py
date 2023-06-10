# C:\Bin\envirment\python
# -*- coding: utf-8 -*-
# @Author  : south(南风)
# @Time    : 2022/9/9 9:30
# @File    : matplotlib图.py
# @Software: PyCharm
# @Describe: 利用matplotlib进行数据分析
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
import random

font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=10)

x = range(2, 26, 2)
y = [12, 13, 1, 17, 19, 30, 29, 39, 29, 18, 6, 4]
#
# plt.plot(x, y)
# # plt.savefig("1.png")
# plt.xticks(x)
# plt.yticks(range(min(y), max(y)+1))
# plt.show()

# y = [random.randint(20, 35) for i in range(120)]
# x = range(0, 120)
#
# _x = list(x)[::10]
#
# plt.plot(x, y)
# plt.xticks(_x)
# plt.show()

a = [random.randint(0, 5) for i in range(20)]
b = [random.randint(0, 3) for x in range(20)]
#
a_x = [i for i in range(11, 31)]
_x = ["{}岁".format(i) for i in range(11, 31)]
plt.figure(figsize=(12, 7), dpi=80)

plt.plot(a_x, a, label="自己")
plt.plot(a_x, b, label="同桌")

plt.legend(prop=font, loc="upper right")

plt.xticks(a_x, _x, rotation=45, fontproperties=font)

plt.xlabel("年龄", fontproperties=font)
plt.ylabel("数量", fontproperties=font)
plt.title("交女朋友数量分析图", fontproperties=font)
#
# plt.grid()
plt.show()
