# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2023/3/12 12:42
# @Author : south(南风)
# @File : ch6_4.py
# Describe:
# -*- coding: utf-8 -*-
from tkinter import *


def cal(*args):
    x2.set(x1.get())


root = Tk()

x1 = StringVar()
x2 = StringVar()

ent = Entry(root, textvariable=x1)
lab1 = Label(root, textvariable=x2)

x2.set("同步显示")
x1.trace("w", cal)
ent.pack()
lab1.pack()

root.mainloop()







