"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time :  2023/9/17 20:50
    @Author : south(南风)
    @File : 1.py
    Describe:
    -*- coding: utf-8 -*-
"""
import jieba.posseg as psg

with open("唐诗人语料集29.txt", "r", encoding="utf-8") as f:
    data = f.readlines()  # 14073

with open("stopwords.txt", "r", encoding="utf-8") as f:
    stopwords = f.readlines()
    stopword = set()
    for i in stopwords:
        i = i.replace("\n", "")
        stopword.add(i)

seg = psg.cut(data[1])
for i, j in seg:
    if i not in stopword:
        print(i)
