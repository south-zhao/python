"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/3/25 13:38
    @Author : south(南风)
    @File : database.py
    Describe:
    -*- coding: utf-8 -*-
"""
import pymysql
from tkinter import messagebox

db = pymysql.connect(host='localhost',
                     user='root',
                     password='root',
                     database='python')

cursor = db.cursor()


def update_infor():
    sql = "select * from user"

    cursor.execute(sql)

    data = cursor.fetchall()
    db.commit()
    data = list(data)
    data = dict(data)
    return data


def get_infor(name, pwd):
    data = update_infor()
    if name in data.keys() and pwd == data[name]:
        res = messagebox.showinfo("提醒", "登陆成功")
    else:
        res = messagebox.askretrycancel("警告", "登陆失败,账号或密码错误")
        if res:
            res = "no"
    return res


def add_infor(name, pwd):
    data = update_infor()
    if name in data.keys():
        messagebox.showinfo("提醒", "用户名已经注册")
    else:
        sql1 = f"insert into user values ('{name}', '{pwd}')"
        cursor.execute(sql1)
        messagebox.showinfo("提醒", "注册成功")
    db.commit()


def show():
    sql_id = "select c_id from course"
    sql_name = "select c_name from course"
    sql_num = "select num from course"
    cursor.execute(sql_id)
    c_id = cursor.fetchall()
    c_id = list(c_id)
    cursor.execute(sql_name)
    c_name = cursor.fetchall()
    c_name = list(c_name)
    cursor.execute(sql_num)
    c_num = cursor.fetchall()
    c_num = list(c_num)
    db.commit()

    return c_id, c_name, c_num


def search(*args):
    c = args
    c_id, c_name, c_num = show()
    if c in c_id:
        index = c_id.index(c)
        d = c_name[index]
        e = c_num[index]
        return c[0], d[0], e[0]
    elif c in c_name:
        index = c_name.index(c)
        d = c_id[index]
        e = c_num[index]
        return d[0], c[0], e[0]
    else:
        messagebox.showerror("警告", "没有这个课程")
        return False, False, False


# 选课信息的添加
def add_chose_course(course_list):
    with open("person.txt", "r", encoding="utf-8") as f:
        information = f.readlines()
    name = information[0].strip("\n")
    for i in course_list:
        num = f"select num from course where c_id = {i}"
        cursor.execute(num)
        num = cursor.fetchone()[0]
        sql_add = f"insert into information values ('{name}', '{i}')"
        cursor.execute(sql_add)
        sql_update = f"update course set num = {int(num) - 1} where c_id = {i}"
        cursor.execute(sql_update)
        db.commit()
    messagebox.showinfo("提示", "选课成功")


# 得到选课结果
def get_chose_infor():
    with open("person.txt", "r", encoding="utf-8") as f:
        information = f.readlines()
    name = information[0].strip("\n")
    sql_get = f"select * from information where s_name = '{name}'"
    cursor.execute(sql_get)
    get_data = cursor.fetchall()
    db.commit()
    get_data = list(get_data)
    cid = []
    cname = []
    for i in get_data:
        sql_se = f"select * from course where c_id = {i[1]}"
        cursor.execute(sql_se)
        db.commit()
        data_infor = cursor.fetchone()
        cid.append(i[1])
        cname.append(data_infor[1])
    return cid, cname


# 获取成绩
def get_grad():

    with open("person.txt", "r", encoding="utf-8") as f:
        name = f.readline().strip("\n")

    sql = f"select * from grade where s_name = '{name}'"
    cursor.execute(sql)
    data = cursor.fetchone()
    db.commit()
    return data


