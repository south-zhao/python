# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2023/3/11 20:14
# @Author : south(南风)
# @File : ch4_1.py
# Describe:
# -*- coding: utf-8 -*-
from tkinter import *


def msgShow():
    label["text"] = "I love you"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"


root = Tk()
root.title("ch4_1")
label = Label(root)
pic = PhotoImage(file="../img/pause_nor.png")
btn1 = Button(root, text="打印消息", command=msgShow, cursor="heart",  width=20)
btn2 = Button(root, text="结束", command=root.destroy, cursor="heart", width=20)
label.pack()
btn1.pack(side=LEFT)
btn2.pack(side=LEFT)

root.mainloop()





