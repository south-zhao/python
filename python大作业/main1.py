"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/3/25 23:40
    @Author : south(南风)
    @File : mian.py
    Describe:
    -*- coding: utf-8 -*-
"""
from tkinter import *

from PIL import Image, ImageTk
import register
import login


def main():
    root = Tk()
    pic = Image.open("1.jpg")
    rush = ImageTk.PhotoImage(pic)

    def turn_register():
        root.destroy()
        register.register1()

    def turn_login():
        root.destroy()
        login.login1()

    root.title("主页")
    root.geometry("800x600+400+100")
    lab = Label(root, image=rush)
    lab.pack(fill=BOTH, expand=True)

    btn1 = Button(root, text="注册", command=turn_register, width=20, font="Helvetic 25 bold")
    btn2 = Button(root, text="登录", command=turn_login, width=20, font="Helvetic 25 bold")
    btn1.place(x=230, y=200)
    btn2.place(x=230, y=330)

    root.mainloop()


if __name__ == '__main__':
    main()
