"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/3/30 15:11
    @Author : south(南风)
    @File : ch16_1.py
    Describe:
    -*- coding: utf-8 -*-
"""
from tkinter import *
from tkinter import messagebox


def hello():
    messagebox.showinfo("Hello", "欢迎使用")


root = Tk()

root.geometry("400x300")

menubar = Menu(root)
menubar.add_command(label="Hello", command=hello)
menubar.add_command(label="Exit", command=root.destroy)

root.config(menu=menubar)

root.mainloop()


