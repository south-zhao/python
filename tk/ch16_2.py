"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/3/30 15:15
    @Author : south(南风)
    @File : ch16_2.py
    Describe:
    -*- coding: utf-8 -*-
"""
from tkinter import *
from tkinter import messagebox


def newfile():
    messagebox.showinfo("New", "打开新档案")


root = Tk()

root.geometry("600x400")

menubar = Menu(root)
file = Menu(menubar, tearoff=False)
file.add_command(label="New File", command=newfile)
menubar.add_cascade(label="File", menu=file)
file.add_separator()
file.add_command(label="Exit", command=root.destroy)

root.config(menu=menubar)

root.mainloop()



