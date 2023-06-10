# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2023/3/11 16:43
# @Author : south(南风)
# @File : ch2_19.py
# Describe:
# -*- coding: utf-8 -*-
from tkinter import *


root = Tk()
root.title("图像")
root.geometry("300x150")
pic = PhotoImage(file="../img/me_destroy_1.png")
s_te = """cghjhgvjhkhkjljl
jsdzfjskdfjsd gfhjgfgfgfgfgfg
fgfjkgkjhjkhjgg"""
label = Label(root, image=pic, text=s_te, compound="left", bg="lightyellow", justify="center")
label.pack()

root.mainloop()









