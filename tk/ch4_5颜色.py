# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2023/3/11 22:46
# @Author : south(南风)
# @File : ch4_5颜色.py
# Describe:
# -*- coding: utf-8 -*-
from tkinter import *


def blue():
    lab.config(bg="blue")


def yellow():
    lab.config(bg="yellow")


root = Tk()
root.title("颜色")
lab = Label(root, width=40, height=10)
bt1 = Button(root, text="blue", command=blue)
bt2 = Button(root, text="yellow", command=yellow)
bt3 = Button(root, text="结束", command=root.destroy)
lab.pack()
bt1.pack(anchor=S, padx=5, pady=5, side=LEFT)
bt2.pack(anchor=S, padx=5, pady=5, side=LEFT)
bt3.pack(anchor=S, padx=5, pady=5, side=LEFT)


root.mainloop()







