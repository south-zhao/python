"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/3/18 14:29
    @Author : south(南风)
    @File : ch12_20.py
    Describe:
    -*- coding: utf-8 -*-
"""
from tkinter import *


def item_sort():
    if var.get():
        rev = True
    else:
        rev = False
    listT = list(lb.get(0, END))
    sore = sorted(listT, reverse=rev)
    lb.delete(0, END)
    for j in sore:
        lb.insert(END, j)


fruits = ["Banana", "Watermelon", "Pineapple", "Orange", "Grapes", "Mango"]

root = Tk()

lb = Listbox(root)
for i in fruits:
    lb.insert(END, i)
lb.pack(padx=10, pady=5)

btn = Button(root, text="排序", command=item_sort)
btn.pack(side=LEFT, padx=10, pady=5)


var = BooleanVar()
cb = Checkbutton(root, variable=var, text="从大到小")
cb.pack(side=LEFT)

root.mainloop()



