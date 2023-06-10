# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2023/3/16 10:49
# @Author : south(南风)
# @File : ch10_4.py
# Describe:
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox


def myMsg1():
    ret = messagebox.askretrycancel("Test1", "安装失败，再来一次")
    print("安装失败", ret)


def myMsg2():
    ret = messagebox.askyesnocancel("Test2", "编辑是否完成")
    print("编辑完成", ret)


# def myMsg():
#     messagebox.showinfo("Box", "Python Tkinter早安")


root = Tk()

# Button(root, text="带你去哦", command=myMsg).pack()
Button(root, text="安装失败", command=myMsg1).pack()
Button(root, text="安装完成", command=myMsg2).pack()

root.mainloop()






