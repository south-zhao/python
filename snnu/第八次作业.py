"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/6/8 19:29
    @Author : south(南风)
    @File : 第八次作业.py
    Describe:
    -*- coding: utf-8 -*-
"""
import os
import shutil
import string


def one():
    a = input("请输入：")
    with open("a.txt", "w", encoding="utf-8") as f:
        f.write(a)
    if not os.path.exists("test"):
        os.makedirs("test")
    shutil.move("a.txt", "test/a.txt")
    with open("test/a.txt", "r", encoding="utf-8") as f:
        print(f.read())


def two():
    a = input("请输入：")
    with open("a.txt", "w", encoding="utf-8") as f:
        f.write(a)
    zi = 0
    en = 0
    ch = 0
    dian = 0
    punc = string.punctuation
    for i in a:
        if i.isalpha():
            en += 1
            zi += 1
        elif i in punc:
            dian += 1
        elif "\u4e00" <= i <= "\u9fff":
            zi += 1
            ch += 1
    with open("b.txt", "w", encoding="utf-8") as f:
        f.write(f"总字符：{zi} 中文：{ch} 英文：{en} 标点：{dian}")



