# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2023/3/16 10:03
# @Author : south(南风)
# @File : ch8_8.py
# Describe:
# -*- coding: utf-8 -*-
from tkinter import *


def priInfo():
    selection = ""
    for i in checkbox:
        if checkbox[i].get() == True:
            selection = selection + sport[i] + "\t"
    print(selection)


root = Tk()
root.title("ch8_8")
root.geometry("400x220")

labF = LabelFrame(root, text="选择你喜欢的运动")
sport = {0: "足球", 1: "篮球", 2: "棒球", 3: "网球"}
checkbox = {}
for i in range(len(sport)):
    checkbox[i] = BooleanVar()
    Checkbutton(labF, text=sport[i], variable=checkbox[i]).grid(row=i+1, sticky=W)

labF.pack(ipadx=5, ipady=5, pady=10)

btn = Button(root, text="确定", width=10, command=priInfo)
btn.pack()

root.mainloop()

