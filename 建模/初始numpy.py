"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/4/27 16:40
    @Author : south(南风)
    @File : 初始numpy.py
    Describe: numpy的简单了解
    -*- coding: utf-8 -*-
"""
import numpy as np

# x1 = np.array([1, 2, 3, 4])
# print(x1)
# print(type(x1))
# print(x1.ndim)  # 数组的维度
# print(x1.shape)  # (4, )==(1, 4) 表示一行有四个元素，只有一行

# a = np.ones((3, 3))  # 创建全一数组
# print(a)

# b = np.full((2, 4), 9)  # 指定数字创建数组
# print(b)

# c = np.empty((4, 4))  # 随机生成任意值
# print(c)

# 数组.fill(值)  全部替换为值

# a = np.identity(3)  # 创建单位矩阵
# a = np.eye(4)
# print(a)

# b = np.diag([1, 2, 3, 4], k=1)  # 创建对角矩阵，k调整位置
# print(b)

# c = np.tri(3)  # 下三角，还有tril(下), triu(上)
# print(c)

# a = np.arange(1, 6, 2)
# print(a)

# b = np.linspace(0, 10, 5, endpoint=False)  # False不包括stop值
# print(b)

"""
视图:当时有切片将得到的值赋给新的变量时，共用一个内存地址，任何一个的更改都会影响整题的更改
副本：使用copy函数，复制过来，就不会共用一个内存地址
"""
# x = np.array([1, 2, 3, 4, 5, 6])
# b = x[:4]
# x[3] = 0
# b[:] = 0
# print(x)
# y = x[:4].copy()
# y[:] = 0
# print(x)


# 形状的变更和大小的变更
# x = np.array([[1, 2],
#               [3, 4]])

# y = x.reshape(4)  # 变形
# np.expand_dims(y, axis=1)
# print(y[:, np.newaxis])

# x = np.arange(4)
#
# y = np.vstack((x, x, x))  # 垂直方向合并
#
# y1 = np.stack((x, x, x), axis=1)
#
# y2 = np.hstack((x, x, x))  # 水平方向合并

# A = np.eye(2)
# B = np.zeros((2, 3))
# C = np.ones((3, 2))
# D = np.eye(3) * 2
#
# y = np.block([[A, B],
#               [C, D]])  # 合并


x = np.arange(6).reshape(2, 3)

# y = np.tile(x, (2, 2))  # 重复

# y1 = np.repeat(x, 3, axis=1)  # 1, 0
# print(y1)
# print(y)

# print(x.T)  # 转置
# print(x.swapaxes(0, 1))


# 基本运算









