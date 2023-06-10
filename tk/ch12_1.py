"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/3/16 17:41
    @Author : south(南风)
    @File : ch12_1.py
    Describe:
    -*- coding: utf-8 -*-
"""
from tkinter import *

root = Tk()
root.geometry("300x210")

lb1 = Listbox(root)
lb1.pack(side=LEFT, padx=5, pady=10)
lb2 = Listbox(root, height=5, relief="raised")
lb2.pack(anchor=N, side=LEFT, padx=5, pady=10)

root.mainloop()








