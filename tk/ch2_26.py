# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2023/3/11 17:59
# @Author : south(南风)
# @File : ch2_26.py
# Describe:
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.ttk import Separator


root = Tk()
root.title("分割线")
my = "一个人的旅行"
myContent = """sdfghljdksfg
gdfffhkl;dfjhkjglkfdhkgdf
gklhgfdhm,lbfgjkfgndm,/.f"""

lab1 = Label(root, text=my, font="Helvetic 20 bold")
lab1.pack(padx=10, pady=10)

sep = Separator(root, orient=HORIZONTAL)
sep.pack(fill=X, padx=5)

lab2 = Label(root, text=myContent)
lab2.pack(padx=10, pady=10)

root.mainloop()
