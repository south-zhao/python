"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/3/27 18:14
    @Author : south(南风)
    @File : ch18_10.py
    Describe:
    -*- coding: utf-8 -*-
"""
from tkinter import *
from tkinter.ttk import Treeview

root = Tk()
root.geometry("600x800")


def re1():
    ii = chose_tree.selection()
    for i in ii:
        print(chose_tree.item(i, "values")[0])


btn = Button(root, text="提交", command=re1)
btn.place(x=100, y=500)
chose_tree = Treeview(root, columns=("course_id", "course_name", "course_num"), show="headings", height=18,
                      selectmode=EXTENDED)
chose_tree.heading("course_id", text="课程号")
chose_tree.heading("course_name", text="课程名")
chose_tree.heading("course_num", text="剩余量")
chose_tree.column("course_id", anchor=CENTER, width=100)
chose_tree.column("course_name", anchor=CENTER, width=200)
chose_tree.column("course_num", anchor=CENTER, width=100)
c_id = ["12432", "3123", "3131"]
c_name = ["1243", "312", "313"]
c_num = ["124", "31", "31"]
for i in zip(c_id, c_name, c_num):
    chose_tree.insert("", index=END, values=i)
chose_tree.place(x=100, y=100)

root.mainloop()
