# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2023/3/15 22:16
# @Author : south(南风)
# @File : ch8_3.py
# Describe:
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()

frame = Frame(root, bg="lightyellow")
frame.pack()

btn = Button(frame, text="Red", fg="red")
btn.pack(side=LEFT, padx=5, pady=5)
btn1 = Button(frame, text="Green", fg="green")
btn1.pack(side=LEFT, padx=5, pady=5)
btn2 = Button(frame, text="Blue", fg="blue")
btn2.pack(side=LEFT, padx=5, pady=5)

frame1 = Frame(root, bg="lightblue")
frame1.pack()
btn3 = Button(frame1, text="Purple", fg="purple")
btn3.pack(side=LEFT, padx=5, pady=5)

root.mainloop()





