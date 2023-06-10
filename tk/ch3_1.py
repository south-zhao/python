# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2023/3/11 18:46
# @Author : south(南风)
# @File : ch3_1.py
# Describe:
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()
root.title("ch3_1")
lab1 = Label(root, text="陕西师范大学", bg="lightyellow")
lab2 = Label(root, text="西南大学", bg="lightgreen")
lab3 = Label(root, text="北京师范大学", bg="lightblue")
# lab1.pack()
# lab2.pack()
# lab3.pack()
# lab1.pack(side=BOTTOM)
# lab2.pack(side=BOTTOM)
# lab3.pack(side=BOTTOM)
# lab1.pack(side=LEFT)
# lab2.pack(side=LEFT)
# lab3.pack(side=LEFT)
lab1.pack()
lab2.pack(side=RIGHT)
lab3.pack(side=BOTTOM)
root.mainloop()

