"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/4/9 15:27
    @Author : south(南风)
    @File : numpy1.py
    Describe:
    -*- coding: utf-8 -*-
"""
import numpy as np

# 转化为ndarray数组
# a = np.array([1, 2, 3, 4])
# print(a)
# print(type(a))
# b = np.array([[1, 2, 3], [4, 5, 6]])
# print(b)

# 求范数
# a = np.array([[0, 3, 4], [1, 6, 4]])
#
# b = np.linalg.norm(a, axis=1)  # 求行向量的范数
# c = np.linalg.norm(a, axis=0)  # 求列向量的范数
# d = np.linalg.norm(a)  # 求矩阵的范数
# print(b)
# print(c)
# print(d)


# 求线性方程的解
# a = np.array([[3, 1], [1, 2]])
# b = np.array([9, 8])
# x1 = np.linalg.inv(a) @ b  # @表示矩阵的乘法， inv表示求逆
# x2 = np.linalg.solve(a, b)  # solve原来求解线性方程组

# a = np.array([[3, 1],
#               [1, 2],
#               [1, 1]])
#
# b = np.array([9, 8, 6])
#
# x1 = np.linalg.pinv(a) @ b  # 求解非nxn阶的矩阵的逆

# A = np.array([[4, 2, -1],
#               [3, -1, 2],
#               [11, 3, 0]])
#
# B = np.array([[4, 2, -1, 2],
#               [3, -1, 2, 10],
#               [11, 3, 0, 8]])
#
#
# a = np.linalg.matrix_rank(A)
# b = np.linalg.matrix_rank(B)
# print(a, b)

A = np.array([[2, 3, 1],
              [1, -2, 4],
              [3, 8, -2],
              [4, -1, 9]])

B = np.array([[2, 3, 1, 4],
              [1, -2, 4, -5],
              [3, 8, -2, 13],
              [4, -1, 9, -6]])


C = np.array([4, -5, 13, -6])

a = np.linalg.matrix_rank(A)
b = np.linalg.matrix_rank(B)

# print(a, b)

x1 = np.linalg.pinv(A) @ C
# print(x1)


