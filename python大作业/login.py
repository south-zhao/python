"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/3/25 13:52
    @Author : south(南风)
    @File : login.py
    Describe:
    -*- coding: utf-8 -*-
"""
from tkinter import *
import database
from PIL import Image, ImageTk
import main1
import choose_page
import num_root


def login1():
    root = Tk()
    pic = Image.open("1.jpg")
    rush = ImageTk.PhotoImage(pic)

    def correct():
        name = user_name.get()
        pwd = pwd1.get()
        res = database.get_infor(name, pwd)
        if res == "no":
            pwd1.set("")
        elif res == "ok":
            with open("person.txt", "w", encoding="utf-8") as f:
                f.write(name + "\n")
            root.destroy()
            choose_page.choose()
        else:
            turn_main()

    def turn_main():
        root.destroy()
        main1.main()

    root.title("登陆页面")
    root.geometry("800x600+400+100")
    lab = Label(root, image=rush)
    lab.pack(fill=BOTH, expand=True)

    lab1 = Label(root, text="用户名", width=11, font="Helvetic 20 bold")
    lab2 = Label(root, text="密码", width=11, font="Helvetic 20 bold")
    lab1.place(x=200, y=250)
    lab2.place(x=200, y=300)

    pwd1 = StringVar()

    user_name = Entry(root, font="Helvetic 20 bold")
    user_pwd = Entry(root, textvariable=pwd1, show="*", font="Helvetic 20 bold")
    user_name.place(x=380, y=250)
    user_pwd.place(x=380, y=300)

    btn1 = Button(root, text="登录", command=correct, width=12, font="Helvetic 20 bold")
    btn2 = Button(root, text="返回首页", command=turn_main, width=12, font="Helvetic 20 bold")
    btn1.place(x=220, y=360)
    btn2.place(x=440, y=360)

    root.mainloop()


if __name__ == '__main__':
    login1()

