"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/4/13 19:34
    @Author : south(南风)
    @File : 第一次作业.py
    Describe: python课程第一次作业
    -*- coding: utf-8 -*-
"""
from pprint import pprint


# 第一题
def pr_rectangle():
    for i in range(10):
        for j in range(20):
            if i == 0 or i == 9:
                print("*", end="")
            else:
                if j == 0 or j == 19:
                    print("*", end="")
                else:
                    print("+", end="")
        print()


pr_rectangle()


# 第二题
def re_n(x):
    """
    传入一个数字并返回累加和大于参数的最小数字
    :param x: 参数
    :return: 类型错误返回提示，正确返回最小数字
    """
    if type(x) == int:
        flag = True
        sum1 = 0
        n = 1
        while flag:
            sum1 = sum1 + n
            n += 1
            if sum1 > x:
                flag = False
        print(x)
        return n - 1
    else:
        return "TypeError: Please input 'int'"


a = re_n(20)
print(a)


# 第三题
list1 = [[i + j for j in range(10)] for i in range(5)]
pprint(list1)
num = 0
for i in range(5):
    for j in range(10):
        if (i * j) % 2 == 0:
            num += 1
            print(f"a[{i}][{j}]", end=" ")
            if num % 10 == 0:
                print()




