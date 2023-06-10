"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/3/18 15:01
    @Author : south(南风)
    @File : ch13_5.py
    Describe:
    -*- coding: utf-8 -*-
"""
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("300x120")

var = StringVar()
cb = Combobox(root, textvariable=var, values=("Python", "Java", "C"))
cb.current(0)
cb.pack(pady=10)
root.mainloop()



