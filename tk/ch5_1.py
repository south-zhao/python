# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2023/3/11 23:05
# @Author : south(南风)
# @File : ch5_1.py
# Describe:
# -*- coding: utf-8 -*-
from tkinter import *


root = Tk()
root.title("ch5_1")

name = Label(root, text="姓名 ")
addr = Label(root, text="地址 ")

name1 = Entry(root)
# addr1 = Entry(root)
addr1 = Entry(root, show="*")

name.grid(row=0)
addr.grid(row=1)
name1.grid(row=0, column=1)
addr1.grid(row=1, column=1)

root.mainloop()





