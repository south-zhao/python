"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time :  2023/9/17 20:50
    @Author : south(南风)
    @File : 1.py
    Describe:
    -*- coding: utf-8 -*-
"""
from snownlp import SnowNLP

with open("唐诗人语料集29.txt", "r", encoding="utf-8") as f:
    data = f.readlines()

s = SnowNLP(data[1])
print(s.summary())
print(s.sentences)
