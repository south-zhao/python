"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/6/8 22:09
    @Author : south(南风)
    @File : grade1.py
    Describe:
    -*- coding: utf-8 -*-
"""
from tkinter import *
from tkinter.ttk import Notebook
import database


def grade():
    root = Tk()
    root.title("成绩系统")
    root.geometry("800x600+400+100")

    note = Notebook()

    total = Frame()
    math = Frame()
    Chinese = Frame()
    English = Frame()

    note.add(total, text="总分")
    note.add(math, text="数学")
    note.add(English, text="英语")
    note.add(Chinese, text="语文")
    note.pack(fill=BOTH, expand=True)

    root.mainloop()



if __name__ == '__main__':
    grade()

