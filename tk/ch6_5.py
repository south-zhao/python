# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2023/3/12 20:03
# @Author : south(南风)
# @File : ch6_5.py
# Describe:
# -*- coding: utf-8 -*-
from tkinter import *


def cal(*args):
    x2.set(x1.get())


def cal1(*args):
    x2.set("被读取数据")


def hit():
    print("读取数据", x1.get())


root = Tk()
root.title("ch6_5")

x1 = StringVar()
x2 = StringVar()

entry = Entry(root, textvariable=x1)
x1.trace("w", cal)
x1.trace("r", cal1)
entry.pack()

lab = Label(root, textvariable=x2)
x2.set("同步显示")
lab.pack()

btn = Button(root, text="点击读取", command=hit)
btn.pack()

root.mainloop()







