"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/3/25 16:46
    @Author : south(南风)
    @File : register.py
    Describe:
    -*- coding: utf-8 -*-
"""
import login
from tkinter import *
import database
import main1
from PIL import Image, ImageTk
from tkinter import messagebox


def register1():
    root = Tk()
    pic = Image.open("1.jpg")
    rush = ImageTk.PhotoImage(pic)

    def add_in():
        name = n.get()
        pwd = p.get()
        pwd_again = p1.get()
        if pwd == pwd_again:
            database.add_infor(name, pwd)
            root.destroy()
            login.login1()
        else:
            messagebox.showerror("提醒", "两次密码不同")
            p.set("")
            p1.set("")

    def turn_main():
        root.destroy()
        main1.main()

    root.title("注册页面")
    root.geometry("800x600+400+100")
    lab = Label(root, image=rush)
    lab.pack(fill=BOTH, expand=True)

    lab1 = Label(root, text="用户名", width=10, font="Helvetic 20 bold")
    lab2 = Label(root, text="密码", width=10, font="Helvetic 20 bold")
    lab3 = Label(root, text="确认密码", width=10, font="Helvetic 20 bold")
    lab1.place(x=200, y=220)
    lab3.place(x=200, y=300)
    lab2.place(x=200, y=260)

    n = StringVar()
    p = StringVar()
    p1 = StringVar()
    user_name = Entry(root, textvariable=n, font="Helvetic 20 bold")
    user_pwd = Entry(root, show="*", textvariable=p, font="Helvetic 20 bold")
    user_pwd_again = Entry(root, show="*", textvariable=p1, font="Helvetic 20 bold")
    user_name.place(x=380, y=220)
    user_pwd.place(x=380, y=260)
    user_pwd_again.place(x=380, y=300)

    btn1 = Button(root, text="注册", command=add_in, width=12, font="Helvetic 20 bold")
    btn2 = Button(root, text="返回首页", command=turn_main, width=12, font="Helvetic 20 bold")
    btn1.place(x=220, y=360)
    btn2.place(x=460, y=360)

    root.mainloop()


if __name__ == '__main__':
    register1()
