"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/6/1 19:25
    @Author : south(南风)
    @File : 第七次作业.py
    Describe:
    -*- coding: utf-8 -*-
"""
import random


def one(a):
    a = a.strip("[").strip("]")
    a = a.replace(" ", "")
    a = a.split(",")
    a = [int(i) for i in a]
    b = sum(a) / len(a)
    i = 0
    while i < len(a):
        if a[i] < b:
            a.remove(a[i])
        else:
            i += 1

    print(a)

a = input("请输入:")
# one(a)

def two(num):
    if int(num) > 100 or int(num) < 0:
        print("无效数字")
    elif 90 <= int(num) <= 100:
        print("优秀")
    elif 80 <= int(num) < 90:
        print("良好")
    elif 70 <= int(num) < 80:
        print("一般")
    elif 60 <= int(num) < 70:
        print("及格")


# two(a)
def three(list1):
    list1 = list1.strip("[").strip("]")
    list1 = list1.replace(" ", "")
    list1 = list1.split(",")
    list1 = [int(i) for i in list1]
    random.shuffle(list1)
    new1 = []
    new2 = []
    for i in range(len(list1)):
        if i % 2 == 0:
            new1.append(list1[i])
        else:
            new2.append(list1[i])
    sum1 = sum(new1)
    sum2 = sum(new2)
    if sum1 > sum2:
        print(sum1)
        print(new1)
    else:
        print(sum2)
        print(new2)


# three(a)



