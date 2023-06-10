# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2023/3/16 16:39
# @Author : south(南风)
# @File : ch11_1_1.py
# Describe:
# -*- coding: utf-8 -*-
from tkinter import *


def pythonClicked():
    if varP.get():
        lab.config(text="Select Python")
    else:
        lab.config(text="Unselect Python")


def javaClicked():
    if varJ.get():
        lab.config(text="Select Java")
    else:
        lab.config(text="Unselect Java")


def buttonClicked(event):
    lab.config(text="Button Clicked")


root = Tk()
root.geometry("300x180")

btn = Button(root, text="Click me")
btn.pack(anchor=W)
btn.bind("<Button-1>", buttonClicked)


varP = BooleanVar()
cbnP = Checkbutton(root, text="Python", variable=varP, command=pythonClicked)
cbnP.pack(anchor=W)
varJ = BooleanVar()
cbnJ = Checkbutton(root, text="Java", variable=varJ, command=javaClicked)
cbnJ.pack(anchor=W)


lab = Label(root, bg="yellow", height=2, width=12)
lab.pack()

root.mainloop()

