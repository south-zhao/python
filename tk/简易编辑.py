# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2023/3/15 19:49
# @Author : south(南风)
# @File : 简易编辑.py
# Describe:
# -*- coding: utf-8 -*-
from tkinter import *


def ch_all():
    ent.select_range(0, END)


def un_all():
    ent.select_clear()


def de():
    en.set("")


def only1():
    if var.get() == True:
        ent.config(state=DISABLED)
    else:
        ent.config(state=NORMAL)


root = Tk()


en = StringVar()
ent = Entry(root, textvariable=en)
ent.grid(row=0, columnspan=4)

choose = Button(root, text="选取", command=ch_all)

unchoose = Button(root, text="取消选取", command=un_all)

delete = Button(root, text="删除", command=de)

end = Button(root, text="结束", command=root.destroy)

var = BooleanVar()
var.set(False)

only = Checkbutton(root, text="只读", variable=var, command=only1)

choose.grid(row=1, column=0)
unchoose.grid(row=1, column=1)
delete.grid(row=1, column=2)
end.grid(row=1, column=3)
only.grid(row=2, columnspan=4)


root.mainloop()







