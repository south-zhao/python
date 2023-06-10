"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/5/11 19:26
    @Author : south(南风)
    @File : 第四次作业.py
    Describe:
    -*- coding: utf-8 -*-
"""


# 第一题
def one():
    sentence = input("请输入一个英语句子:").strip()
    list1 = sentence.split(" ")
    list2 = []
    for i in range(len(list1) - 1):
        if list1[i] != list1[i + 1]:
            list2.append(list1[i])
    list2.append(list1[-1])
    a = " ".join(list2)
    print(a)


# 第二题
def two():
    sentence = input("请输入一段英语:").split(" ")
    for i in sentence:
        if len(i) == 3:
            print(i)
