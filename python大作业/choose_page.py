"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/5/1 15:34
    @Author : south(南风)
    @File : choose_page.py
    Describe:
    -*- coding: utf-8 -*-
"""
from tkinter import *
from PIL import Image, ImageTk
import num_root
import grade1


def choose():
    root = Tk()
    pic = Image.open("1.jpg")
    rush = ImageTk.PhotoImage(pic)
    root.title("主页")
    root.geometry("800x600+400+100")
    lab = Label(root, image=rush)
    lab.pack(fill=BOTH, expand=True)

    def turn_choose():
        root.destroy()
        num_root.chose_neng()

    def turn_grad():
        root.destroy()
        grade1.grade()

    btn1 = Button(root, text="选课功能", command=turn_choose, width=20, font="Helvetic 25 bold")
    btn2 = Button(root, text="成绩", width=20, font="Helvetic 25 bold", command=turn_grad)
    btn1.place(x=230, y=200)
    btn2.place(x=230, y=330)

    root.mainloop()


if __name__ == '__main__':
    choose()
