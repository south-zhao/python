# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2023/3/15 19:40
# @Author : south(南风)
# @File : ch7_7.py
# Describe:
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
# var.set(1)

lab = Label(root, text="这是预算", bg="lightyellow", width=30)
lab.grid(row=0)

c1 = Checkbutton(root, text="篮球", variable=var1)

c2 = Checkbutton(root, text="棒球", variable=var2)

c3 = Checkbutton(root, text="乒乓球", variable=var3)

c1.grid(row=1, sticky=W)
c2.grid(row=2, sticky=W)
c3.grid(row=3, sticky=W)

root.mainloop()
