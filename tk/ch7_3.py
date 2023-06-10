# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2023/3/15 19:31
# @Author : south(南风)
# @File : ch7_3.py
# Describe:
# -*- coding: utf-8 -*-
from tkinter import *


def pr():
    lab.config(text=cities[var.get()])
    print(cities[var.get()])


root = Tk()

cities = {0: "东京", 1: "纽约", 2: "巴黎", 3: "伦敦", 4: "香港"}

var = IntVar()
# var.set(1)

lab = Label(root, text="这是预算", bg="lightyellow", width=30)

lab.pack()
for i, j in cities.items():
    # Radiobutton(root, text=j, variable=var, value=i, command=pr).pack()
    Radiobutton(root, text=j, indicatoron=0, variable=var,  value=i, command=pr, width=30).pack()

root.mainloop()
