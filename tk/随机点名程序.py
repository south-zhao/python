"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/5/20 14:44
    @Author : south(南风)
    @File : 随机点名程序.py
    Describe:
    -*- coding: utf-8 -*-
"""
import random
import pyttsx3
from tkinter import *
from PIL import Image, ImageTk
import pandas as pd


root = Tk()
pic = Image.open("../python大作业/1.jpg")
rush = ImageTk.PhotoImage(pic)
root.title("主页")
root.geometry("800x600+400+100")
lab = Label(root, image=rush)
lab.pack(fill=BOTH, expand=True)

df = pd.read_excel("名单.xlsx")
name_list = list(df["姓名"])
random.shuffle(name_list)


begin = StringVar()
begin.set("开始")


def voice(name):
    begin.set("开始")
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say("有请" + name + "同学回答问题")
    engine.runAndWait()
    engine.stop()


def af():
    global s, num1
    num1 = random.choice(name_list)
    label.config(text=num1)
    s = label.after(40, af)


def show_num():
    x1 = begin.get()

    if x1 == "开始":
        af()
        begin.set("暂停")
    else:
        label.after_cancel(s)
        voice(str(num1))


label = Label(root, text="会是谁！", width=20, height=2, font="Helvetic 25 bold")

btn = Button(root, textvariable=begin, width=20, font="Helvetic 25 bold", command=show_num)
label.place(x=230, y=200)
btn.place(x=230, y=350)

root.mainloop()
