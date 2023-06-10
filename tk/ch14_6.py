"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/3/18 15:08
    @Author : south(南风)
    @File : ch14_6.py
    Describe:
    -*- coding: utf-8 -*-
"""
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("300x160")

note = Notebook(root)

frame1 = Frame()
lab = Label(frame1, text="Python")
lab.pack(pady=10, padx=10)
frame2 = Frame()
btn = Button(frame2, text="Help")
btn.pack(padx=10, pady=10)

note.add(frame1, text="选项1")
note.add(frame2, text="选项2")

note.pack(padx=10, pady=10, fill=BOTH, expand=True)

root.mainloop()








