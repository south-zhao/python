"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/3/18 10:11
    @Author : south(南风)
    @File : ch12_19.py
    Describe:
    -*- coding: utf-8 -*-
"""
from tkinter import *


def addIn():
    var = entry.get()
    if len(var.strip()) == 0:
        return
    lb.insert(END, var)
    entry.delete(0, END)


def dele():
    index = lb.curselection()
    if len(index) == 0:
        return
    lb.delete(index)

root = Tk()
entry = Entry(root)
entry.grid(row=0, column=0, padx=5, pady=5)

btn = Button(root, text="增加", command=addIn)
btn.grid(row=0, column=1, padx=5, pady=5)

lb = Listbox(root)
lb.grid(row=1, column=0, columnspan=2, padx=5, sticky=W)

btnd = Button(root, text="删除", command=dele)
btnd.grid(row=2, column=0, padx=5, pady=5, sticky=W)

root.mainloop()










