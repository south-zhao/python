"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/3/26 9:33
    @Author : south(南风)
    @File : num_root.py
    Describe:
    -*- coding: utf-8 -*-
"""
from tkinter import *
from tkinter.ttk import Notebook
import database
from tkinter.ttk import Treeview
import choose_page


# 选课和选课结果
def chose_neng():
    root = Tk()
    root.title("主页面")
    root.geometry("800x600+400+100")

    # 搜索键聚焦提示信息清除
    def wu(event):
        num.set("")

    # 搜索键绑定函数
    def search_infor(*args):
        infor = num.get()
        cid, cname, cnum = database.search(infor)
        del_infor1 = chose_tree.get_children()
        for item in del_infor1:
            chose_tree.delete(item)
        if cid and cname and cnum is not False:
            chose_tree.insert("", END, values=[cid, cname, cnum])
        else:
            cid, cname, cnum = database.show()
            for o in zip(cid, cname, cnum):
                chose_tree.insert("", END, values=o)

    # 选课提交
    def enter():
        ch_index = chose_tree.selection()
        ch_id = []
        for index in ch_index:
            ch_id.append(chose_tree.item(index, "values")[0])
        flag = database.add_chose_course(ch_id)
        del_infor = chose_tree.get_children()
        for item in del_infor:
            chose_tree.delete(item)
        cid, cname, cnum = database.show()
        for p in zip(cid, cname, cnum):
            chose_tree.insert("", END, values=p)
        if flag:
            resul()

    note = Notebook(root)

    chose_frame = Frame()
    # 查看选课结果
    res_frame = Frame()

    num = StringVar()
    ch_entry = Entry(chose_frame, textvariable=num, width=40)
    num.set("请输入课程号或课程名称")
    ch_entry.bind("<FocusIn>", wu)
    ch_entry.place(x=100, y=50)

    def re_choose():
        root.destroy()
        choose_page.choose()

    btn = Button(chose_frame, text="搜索", command=search_infor, width=10, height=1)
    btn_sub = Button(chose_frame, text="提交", width=10, height=1, command=enter)
    btn_ret = Button(chose_frame, text="返回选择页面", width=10, height=1, command=re_choose)
    btn_ret.place(x=300, y=500)
    btn_sub.place(x=200, y=500)
    btn.place(x=400, y=45)

    # 选课结果
    def resul():
        tree = Treeview(res_frame, columns=("course_id", "course_name"), show="headings", height=25)
        tree.heading("course_id", text="课程号")
        tree.heading("course_name", text="课程名")
        tree.column("course_id", anchor=CENTER, width=250)
        tree.column("course_name", anchor=CENTER, width=250)
        res_cid, res_cname = database.get_chose_infor()
        for j in zip(res_cid, res_cname):
            tree.insert("", index=END, values=j)
        tree.place(x=130, y=20)
        tree.after(1000, resul)

    resul()
    chose_tree = Treeview(chose_frame, columns=("course_id", "course_name", "course_num"), show="headings", height=18,
                          selectmode=EXTENDED)
    chose_tree.heading("course_id", text="课程号")
    chose_tree.heading("course_name", text="课程名")
    chose_tree.heading("course_num", text="剩余量")
    chose_tree.column("course_id", anchor=CENTER, width=150)
    chose_tree.column("course_name", anchor=CENTER, width=200)
    chose_tree.column("course_num", anchor=CENTER, width=150)
    c_id, c_name, c_num = database.show()
    for i in zip(c_id, c_name, c_num):
        chose_tree.insert("", index=END, values=i)
    chose_tree.place(x=100, y=100)
    scrollbar = Scrollbar(chose_frame)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar.config(command=chose_tree.yview)
    chose_tree.configure(yscrollcommand=scrollbar.set)

    note.add(chose_frame, text="选课")
    # 查看结果
    note.add(res_frame, text="选课结果")
    note.pack(fill=BOTH, expand=True)

    root.mainloop()


if __name__ == '__main__':
    chose_neng()
