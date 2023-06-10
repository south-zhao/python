# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2023/3/12 0:01
# @Author : south(南风)
# @File : ch6_2.py
# Describe:
# -*- coding: utf-8 -*-
from tkinter import *


def btn_hit():
    if x.get() == "":
        x.set("fasj  sfdrjka")
        btn.config(text="点我隐藏")
    else:
        x.set("")
        btn.config(text="点我显示")


root = Tk()
x = StringVar()

label = Label(root, textvariable=x, fg="blue", bg="lightyellow", width=25, height=2)
label.pack()
btn = Button(root, text="点我显示", command=btn_hit)
btn.pack()

root.mainloop()








