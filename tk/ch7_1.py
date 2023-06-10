# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2023/3/12 22:21
# @Author : south(南风)
# @File : ch7_1.py
# Describe:
# -*- coding: utf-8 -*-
from tkinter import *


def pr():
    num = var.get()
    if num == 1:
        lab.config(text="你是男生")
    else:
        lab.config(text="你是女生")


root = Tk()

var = IntVar()
# var.set(1)

lab = Label(root, text="这是预算", bg="lightyellow", width=30)

r1 = Radiobutton(root, text="男生", variable=var, value=1, command=pr)

r2 = Radiobutton(root, text="女生", variable=var, value=2, command=pr)

lab.pack()
r1.pack()
r2.pack()

root.mainloop()





