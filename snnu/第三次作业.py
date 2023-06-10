"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/5/4 19:22
    @Author : south(南风)
    @File : 第三次作业.py
    Describe:
    -*- coding: utf-8 -*-
"""
import random


# 第一题
def one():
    list1 = [random.randint(1, 1000) for i in range(50)]
    print(list1)
    list1 = [i for i in list1 if i % 2 == 0]
    print(list1)


# 第二题
def two():
    list1 = [random.randint(1, 100) for i in range(20)]
    print(list1)
    list2 = list1[::2]
    list2.sort(reverse=True)
    for i in range(10):
        list1[i*2] = list2[i]
    print(list1)


# 第三题
def three():
    list1 = ['1', '2', '3', '4']
    list2 = []
    for i in range(4):
        for j in range(4):
            if j != i:
                for m in range(4):
                    if m != j and m != i:
                        for n in range(4):
                            if n != m and n != j and n != i:
                                num = list1[i] + list1[j] + list1[m] + list1[n]
                                list2.append(int(num))

    def is_prime(numb):
        for y in range(2, int(numb**(1/2)) + 1):
            if numb % y == 0:
                break
        else:
            print(numb)

    print(list2)
    for index in list2:
        is_prime(index)


three()
