# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2023/3/11 17:41
# @Author : south(南风)
# @File : ch2_23.py
# Describe:
# -*- coding: utf-8 -*-
from tkinter import *

counter = 0


def run_counter(digit):
    def counting():
        global counter
        counter += 1
        digit.config(text=str(counter))
        digit.after(1000, counting)
    counting()


root = Tk()
root.title("计数器")
digit = Label(root, bg="yellow", fg="blue", height=3, width=10, font="Helvetic 20 bold")
digit.pack()
run_counter(digit)

root.mainloop()















