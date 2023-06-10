# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2023/3/16 10:23
# @Author : south(南风)
# @File : ch9_4.py
# Describe:
# -*- coding: utf-8 -*-
from tkinter import *


def ch(source):
    r1 = r.get()
    g1 = g.get()
    b1 = b.get()
    myC = "#%02x%02x%02x" % (r1, g1, b1)
    root.config(bg=myC)


root = Tk()
root.geometry("360x240")
frame = Frame(root)
frame.pack()
# r = Scale(root, from_=0, to=255, command=ch)
# g = Scale(root, from_=0, to=255, command=ch)
# b = Scale(root, from_=0, to=255, command=ch)
r = Scale(frame, from_=0, to=255, command=ch)
g = Scale(frame, from_=0, to=255, command=ch)
b = Scale(frame, from_=0, to=255, command=ch)
r.set(255)

r.grid(row=0, column=0)
g.grid(row=0, column=1)
b.grid(row=0, column=3)

root.mainloop()









