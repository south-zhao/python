# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2023/3/16 17:16
# @Author : south(南风)
# @File : ch11_4.py
# Describe:
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox


def leave(event):
    ret = messagebox.askyesno("ch11_4", "是否离开")
    if ret == True:
        root.destroy()
    else:
        return


root = Tk()
root.geometry("300x180")

root.bind("<Escape>", leave)

lab = Label(root, text="测试ESC键", bg="yellow", height=4, width=15)
lab.pack(pady=30)

root.mainloop()

