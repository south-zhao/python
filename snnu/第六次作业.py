"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/5/25 19:27
    @Author : south(南风)
    @File : 第六次作业.py
    Describe:
    -*- coding: utf-8 -*-
"""
import re


# 第一题
def one():
    text = " " + input("请输入一段英文文本:")
    str1 = input("请输入一个指定的字母作为单词的首字母:")
    pat = re.compile("\W" + "(" + str1 + "[a-z]+)", re.I)
    res = pat.findall(text)
    dict1 = {}
    for i in res:
        if i in dict1.keys():
            n = dict1[i][1]
            m = text.find(i, n) - 1
        else:
            m = text.find(i) - 1
        n = len(i)
        dict1[i] = (m, m+n)
        print(i, m)


# 第二题
def two():
    text1 = input("请输入一段文本:")
    se = input("请输入一个搜索的内容:")
    rep = input("请输入一个替换的内容:")
    a, num = re.subn(r"{}".format(se), rep, text1)
    print(a)
    print(num)

