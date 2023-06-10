# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2023/3/11 23:38
# @Author : south(南风)
# @File : 简易计算.py
# Describe:
# -*- coding: utf-8 -*-
from tkinter import *


def res():
    resu.configure(text="结果是 " + str(eval(pu.get())))


root = Tk()
lab = Label(root, text="请输入表达式:")
pu = Entry(root)
resu = Label(root)
btn = Button(root, text="结果", command=res)

lab.pack()
pu.pack()
resu.pack()
btn.pack()

root.mainloop()




