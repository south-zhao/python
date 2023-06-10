# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2023/3/15 22:39
# @Author : south(南风)
# @File : ch9_4_1.py
# Describe:
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.colorchooser import *


def bgUpdate():
    myC = askcolor()
    root.config(bg=myC[1])


root = Tk()
btn = Button(text="select", command=bgUpdate)
btn.pack()

root.mainloop()


