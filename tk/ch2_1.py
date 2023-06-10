# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2023/3/11 16:14
# @Author : south(南风)
# @File : ch2_1.py
# Describe:
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()
root.title("ch2_1")
root.geometry("300x150")
label = Label(root, text="I like tkinter", bitmap="hourglass", compound="top", relief="ridge", padx=5, pady=10)
label.pack()
# print(type(label))
root.mainloop()
