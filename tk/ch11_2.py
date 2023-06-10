# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2023/3/16 16:49
# @Author : south(南风)
# @File : ch11_2.py
# Describe:
# -*- coding: utf-8 -*-
from tkinter import *


def callback(event):
    lab.config(text="位置: %d %d" % (event.x, event.y))
    print("Clicked at", event.x, event.y)


root = Tk()

frame = Frame(root, width=300, height=180)

lab = Label(frame, width=10, bg="yellow")
lab.pack(padx=10, pady=10)
frame.bind("<Button-1>", callback)
frame.pack()
root.mainloop()



