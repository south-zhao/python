"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/3/18 9:52
    @Author : south(南风)
    @File : ch12_4.py
    Describe:
    -*- coding: utf-8 -*-
"""
from tkinter import *

fruits = ["Banan", "Watermelon", "Pineapple", "Orange", "Grapes", "Mango"]

root = Tk()
root.geometry("300x210")

lb = Listbox(root, selectmode=MULTIPLE)
for i in fruits:
    lb.insert(END, i)
lb.pack(pady=10)

root.mainloop()










