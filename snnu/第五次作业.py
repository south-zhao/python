"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/5/18 19:16
    @Author : south(南风)
    @File : 第五次作业.py
    Describe:
    -*- coding: utf-8 -*-
"""


# 第一题
def one():
    sentence = input("请输入一个句子:").strip()
    list1 = [i for i in sentence if not i.isalpha() and not i.isdigit() and i != " "]
    print("".join(list1))


# 第二题
def two():
    name = input("请输入姓名:").strip()
    sex = input("请输入性别:").strip()
    age = input("请输入年龄:").strip()
    job = input("请输入职位:").strip()
    phone = input("请输入电话号码:").strip()
    if sex == "male" or sex == "boy":
        sex = "boy"
    elif sex == "female" or sex == "girl":
        sex = "girl"
    information = "My name is {}.I'm a {} years old {}.I am a {}.My telephone number is {}".format(name, age, sex, job, phone)
    print(information)


