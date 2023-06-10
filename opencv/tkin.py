"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/6/7 22:30
    @Author : south(南风)
    @File : tkin.py
    Describe:
    -*- coding: utf-8 -*-
"""
import os
import pickle
import tkinter as tk
import cv2
from tkinter import messagebox
import face_recognition
from PIL import Image, ImageTk

window = tk.Tk()
camera = cv2.VideoCapture(0)
window.title('Cheney\' Face_rec 3.0')  # 窗口标题
window.geometry('800x500')  # 这里的乘是小x

name1 = tk.StringVar()
user_name = tk.Entry(window, textvariable=name1, font="Helvetic 20 bold", width=10)

Recognizer = cv2.face.LBPHFaceRecognizer_create()
Recognizer.read(os.path.join("train result", 'Training.yml'))
with open('Label.pickle', 'rb') as file:
    OriginalLabel = pickle.load(file)
    Labels = {v: k for k, v in OriginalLabel.items()}

with open("student.txt", "r", encoding="utf-8") as f:
    con = f.readlines()
    name = {}
    for i in con:
        infor = i.split()
        name[infor[1]] = infor[0]


def f_exit():  # 退出按钮
    exit()


def video_loop():  # 用于在label内动态展示摄像头内容（摄像头嵌入控件）
    global Confidence, ID
    success, img = camera.read()  # 从摄像头读取照片
    img = cv2.flip(img, 1)
    cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换颜色从BGR到RGBA
    imag = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 6灰度处理c
    Faces = face_recognition.face_locations(cv2image)
    Face1 = face_recognition.face_locations(imag)
    if success:
        for face in Faces:
            X, Y, W, H = face
            cv2.rectangle(cv2image, (H, X), (Y, W), (255, 0, 0), 1)
        for fc in Face1:
            x, y, w, h = fc
            ID, Confidence = Recognizer.predict(imag[y: y + h, x: x + w])  # 预测函数
        current_image = Image.fromarray(cv2image)  # 将图像转换成Image对象
        cv2image = ImageTk.PhotoImage(image=current_image)
        panel.imgtk = cv2image
        panel.config(image=cv2image)

    window.after(1, video_loop)


def f_sc():
    if Confidence >= 70:
        name1.set(Labels[ID])
        pwd1.set(name[Labels[ID]])
    else:
        name1.set("未知")


def add_infor():
    messagebox.showinfo("提醒", "请输入姓名和学号")
    a = name1.get()
    b = pwd1.get()
    if a and b:
        with open("student.txt", "a", encoding="utf-8") as f1:
            f1.writelines(f"{b} {a}")
        messagebox.showinfo("提醒", "新面部信息添加成功")


lab1 = tk.Label(window, text="姓名", width=5, font=('Arial', 12))
lab2 = tk.Label(window, text="学号", width=5, font=('Arial', 12))
lab1.place(x=520, y=200)
lab2.place(x=520, y=250)

pwd1 = tk.StringVar()

user_pwd = tk.Entry(window, textvariable=pwd1, font="Helvetic 20 bold", width=10)
user_name.place(x=570, y=200)
user_pwd.place(x=570, y=250)

# 在窗口界面设置放置Button按键并绑定处理函数
button_a = tk.Button(window, text='开始刷脸', font=('Arial', 12), width=10, height=2, command=f_sc)
button_a.place(x=10, y=20)

button_b = tk.Button(window, text='录入人脸', font=('Arial', 12), width=10, height=2, command=add_infor)
button_b.place(x=210, y=20)

button_b = tk.Button(window, text='退出', font=('Arial', 12), width=10, height=2, command=f_exit)
button_b.place(x=410, y=20)

panel = tk.Label(window, width=500, height=350)  # 摄像头模块大小
panel.place(x=10, y=100)  # 摄像头模块的位置
window.config(cursor="arrow")

video_loop()

#  窗口循环，用于显示
window.mainloop()
