# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2023/3/12 12:36
# @Author : south(南风)
# @File : ch6_3.py
# Describe:
# -*- coding: utf-8 -*-
from tkinter import *


def callback(*args):
    print("data change : ", xE.get())


root = Tk()
xE = StringVar()

entry = Entry(root, textvariable=xE)
entry.pack()
xE.trace("w", callback)

root.mainloop()


