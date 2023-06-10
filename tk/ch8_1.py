# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2023/3/15 20:13
# @Author : south(南风)
# @File : ch8_1.py
# Describe:
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()

# for i in ["red", "green", "blue"]:
#     Frame(root, bg=i, height=50, width=200).pack()
f = {"red": "cross", "green": "boat", "blue": "clock"}
for i in f:
    Frame(root, bg=i, cursor=f[i], height=50, width=200).pack()

root.mainloop()








