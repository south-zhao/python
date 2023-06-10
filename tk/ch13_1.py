"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/3/18 14:56
    @Author : south(南风)
    @File : ch13_1.py
    Describe:
    -*- coding: utf-8 -*-
"""
from tkinter import *

root = Tk()

root.geometry("300x180")
op = ("Python", "Java", "C")
var = StringVar(root)
# option = OptionMenu(root, var, "Python", "Java", "C")
option = OptionMenu(root, var, *op)
option.pack()

root.mainloop()








