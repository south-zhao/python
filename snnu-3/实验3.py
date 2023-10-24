"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time :  2023/10/20 18:36
    @Author : south(南风)
    @File : 实验3.py
    Describe:
    -*- coding: utf-8 -*-
"""
from ctypes import *


p = CDLL("./Project1.dll")
a = p.sum(12, 23)

print(a)

