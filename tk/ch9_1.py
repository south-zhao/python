# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2023/3/16 10:17
# @Author : south(南风)
# @File : ch9_1.py
# Describe:
# -*- coding: utf-8 -*-
from tkinter import *


root = Tk()
Scale(root, from_=0, to=10).pack()
Scale(root, from_=0, to=10, length=300, orient=HORIZONTAL, tickinterval=1).pack()
root.mainloop()



