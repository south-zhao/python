# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2023/3/11 23:14
# @Author : south(南风)
# @File : 登录页面.py
# Describe:
# -*- coding: utf-8 -*-
from tkinter import *


def pr():
    print("Acc: %s\nPass: %s" % (acco.get(), pwd.get()))
    # acco.delete(0, END)
    # pwd.delete(0, END)


root = Tk()
pic = PhotoImage(file="../img/bullet_supply.png")
lab = Label(root, text="hgdsfhgjksdfjgfhaks", image=pic, compound="top")
acc = Label(root, text="Account")
pas = Label(root, text="Password")

acco = Entry(root)
pwd = Entry(root, show="*")

log = Button(root, text="login", command=pr)
ex = Button(root, text="推出", command=root.destroy)
lab.grid(row=0, column=0, columnspan=2)
acc.grid(row=1)
pas.grid(row=2)
acco.grid(row=1, column=1)
pwd.grid(row=2, column=1)
log.grid(row=3, column=0)
ex.grid(row=3, column=1)

root.mainloop()









