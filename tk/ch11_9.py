"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/3/16 17:29
    @Author : south(南风)
    @File : ch11_9.py
    Describe:
    -*- coding: utf-8 -*-
"""
from tkinter import *
from tkinter import messagebox


def callback():
    res = messagebox.askokcancel("OKCANCEL", "结束或取消")
    if res:
        root.destroy()
    else:
        return


root = Tk()
root.geometry("300x180")
root.protocol("WM_DELETE_WINDOW", callback)  # 更改协议绑定

root.mainloop()





