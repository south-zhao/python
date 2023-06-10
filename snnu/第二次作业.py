"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/5/3 14:59
    @Author : south(南风)
    @File : 第二次作业.py
    Describe:
    -*- coding: utf-8 -*-
"""
import random


# 第一题
def func():
    a = list(input("请输入一个列表:").replace(",", "").replace(" ", "").replace("[", "").replace("]", ""))
    b = list(input("请输入两个数字，用逗号隔开:").split(","))
    b = sorted([int(i) for i in b])
    length = len(a)
    if b[1] > length - 1:
        print("The index is illegal")
    else:
        res = a[b[0]:b[1] + 1]
        print(res)


# 第二题
def fin():
    dict1 = {"高等数学": 65, "线性代数": 70, "C语言": 70, "Java": 80}
    key = input("用户输入查询的名称:")
    res = dict1.get(key, "The key does not exist")
    print(res)


# 第三题
def three():
    list1 = [random.randint(1, 100) for i in range(20)]
    list_f = list1[:10].copy()
    list_b = list1[10:].copy()
    print(list1)
    list_f.sort(reverse=False)
    list_b.sort(reverse=True)
    print(list_f)
    print(list_b)



