# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2023/3/16 17:11
# @Author : south(南风)
# @File : ch11_3.py
# Describe:
# -*- coding: utf-8 -*-
from tkinter import *


def enter(event):
    x.set("鼠标进入")


def leave(event):
    x.set("鼠标离开")


root = Tk()

root.geometry("300x180")

btn = Button(root, text="Exit", command=root.destroy)
btn.pack(pady=30)
btn.bind("<Enter>", enter)
btn.bind("<Leave>", leave)

x = StringVar()
lab = Label(root, textvariable=x, height=4, width=15, bg="yellow")
lab.pack(pady=30)

root.mainloop()

