"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/3/31 14:36
    @Author : south(南风)
    @File : lowb.py
    Describe: 如果a+b+c=1000，且a²+b²=c²（a,b,c 为自然数），如何求出所有a、b、c可能的组合
    -*- coding: utf-8 -*-
"""
import time
#
# 这是一种耗时很长的方法，逻辑很简单
# def low_se():
#     b = time.time()
#     for i in range(1, 1001):
#         for j in range(1, 1001):
#             for m in range(1, 1001):
#                 if i + j + m == 1000 and i**2 + j**2 == m**2:
#                     print(i, j, m)
#     e = time.time()
#     print(e - b)
#
#
# low_se()


# 这是一种算法从，相比之下更快速一点,上一个43秒左右，这一个一秒不到
def low_se():
    b = time.time()
    for i in range(1, 1001):
        for j in range(1, 1001):
            c = 1000 - (i + j)
            if i**2 + j**2 == c**2:
                print(i, j, c)
    e = time.time()
    print(e - b)


low_se()

