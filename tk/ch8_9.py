# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2023/3/16 10:11
# @Author : south(南风)
# @File : ch8_9.py
# Describe:
# -*- coding: utf-8 -*-
import random
from tkinter import *

root = Tk()
root.title("模拟对话")
# t1 = Toplevel()
# Label(t1, text="你好").pack()
msgY, msgN, msgE = 1, 2, 3


def MessageB():
    msg = random.randint(1, 3)
    if msg == msgY:
        labT = "Yes"
    elif msg == msgN:
        labT = "No"
    else:
        labT = "Exit"
    t1 = Toplevel()
    Label(t1, text=labT).pack(fill=BOTH, expand=True)


btn = Button(root, text="点我", command=MessageB)
btn.pack()

root.mainloop()




root.mainloop()




