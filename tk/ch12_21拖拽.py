"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/3/18 14:38
    @Author : south(南风)
    @File : ch12_21拖拽.py
    Describe: 功能方面还存在问题
    -*- coding: utf-8 -*-
"""
from tkinter import *


def get_index(event):
    lb.index = lb.nearest(event.y)


def drag(event):
    new_index = lb.nearest(event.y)
    if new_index < lb.index:
        x = lb.get(new_index)
        lb.delete(new_index)
        lb.insert(new_index+1, x)
        lb.index = new_index
    elif new_index > lb.index:
        x = lb.get(new_index)
        lb.delete(new_index)
        lb.insert(new_index + 1, x)
        lb.index = new_index


fruits = ["Banana", "Watermelon", "Pineapple", "Orange", "Grapes", "Mango"]

root = Tk()

lb = Listbox(root)
for i in fruits:
    lb.insert(END, i)
    lb.bind("<Button-1>", get_index)
    lb.bind("<B1-Motion>", drag)
lb.pack(padx=10, pady=10)

root.mainloop()




