"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/3/31 14:31
    @Author : south(南风)
    @File : 高斯定理.py
    Describe:
    -*- coding: utf-8 -*-
"""
import time
b = time.time()
sum1 = 0
for i in range(1, 1001):
    sum1 += i
e = time.time()
print(sum1)
print(e - b)

b1 = time.time()
a = (1 + 1000) * 1000 / 2
e1 = time.time()
print(a)
print(e1 - b1)




