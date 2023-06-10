"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/3/16 17:46
    @Author : south(南风)
    @File : ch12_2.py
    Describe:
    -*- coding: utf-8 -*-
"""
from tkinter import *

root = Tk()
root.geometry("300x210")

lb = Listbox(root)
lb.insert(END, "Banna")
lb.insert(END, "Cidaj")
lb.insert(END, "Dckds")
lb.pack(pady=10)

root.mainloop()











