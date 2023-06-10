"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/3/18 14:48
    @Author : south(南风)
    @File : ch12_22.py
    Describe:
    -*- coding: utf-8 -*-
"""
from tkinter import *

root = Tk()

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

lb = Listbox(root, yscrollcommand=scrollbar.set)
for i in range(50):
    lb.insert(END, "Line " + str(i))

lb.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar.config(command=lb.yview)
root.mainloop()











