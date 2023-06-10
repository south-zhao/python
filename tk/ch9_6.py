# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2023/3/16 10:34
# @Author : south(南风)
# @File : ch9_6.py
# Describe:
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()
root.geometry("300x100")
cities = ("新加坡", "上海", "东京")
# spin = Spinbox(root, from_=10, to=30, increment=2)  # 每次增加2
spin = Spinbox(root, values=cities)  # 每次增加2
# spin = Spinbox(root, from_=10, to=30)  # 每次增加1
spin.pack(pady=20)

root.mainloop()

