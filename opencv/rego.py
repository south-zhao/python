"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/6/6 17:43
    @Author : south(南风)
    @File : rego.py
    Describe:
    -*- coding: utf-8 -*-
"""
import cv2
import os
import pickle
import numpy as np
from PIL import Image, ImageFont, ImageDraw
import face_recognition

# 打开摄像头
Webcam = cv2.VideoCapture(0)
# 加载OpenCV人脸检测分类器Haar
face_cascade = cv2.CascadeClassifier(os.path.join(r"C:\Users\xjiez\Desktop\Code\python\opencv", "haarcascade_frontalface_default.xml"))

Recognizer = cv2.face.LBPHFaceRecognizer_create()
Recognizer.read(os.path.join("train result", 'Training.yml'))

Labels = {}

with open('Label.pickle', 'rb') as file:
    OriginalLabel = pickle.load(file)
    Labels = {v: k for k, v in OriginalLabel.items()}


def cv2AddChineseText(img, text, position, textColor=(0, 255, 0), textSize=30):
    if (isinstance(img, np.ndarray)):  # 判断是否OpenCV图片类型
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(img)
    # 字体的格式
    fontStyle = ImageFont.truetype("simsun.ttc", textSize, encoding="utf-8")
    # 绘制文本
    draw.text((position[0], position[1]-50), text, textColor, font=fontStyle)
    # 转换回OpenCV格式
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)



while True:
    Return, Frame = Webcam.read()  # 读取该帧的画面
    Frame = cv2.flip(Frame, 1)

    GrayScale = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)  # 6灰度处理
    Faces = face_recognition.face_locations(GrayScale)
    # Faces = face_cascade.detectMultiScale(GrayScale, 1.3, 5)  # 检查人脸
    for face in Faces:
        X, Y, W, H = face
        ROI_GRAY = GrayScale[Y:Y + H, X:X + W]
        # ROI_COLOR = Frame[Y:Y + H, X:X + W]

        ID, Confidence = Recognizer.predict(ROI_GRAY)  # 预测函数
        if Confidence >= 70:
            Frame = cv2AddChineseText(Frame, Labels[ID], (H, X), (0, 0, 255), 30)
            # print(Labels[ID])
            # cv2.putText(Frame, Labels[ID], (X, Y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.rectangle(Frame, (H, X), (Y, W), (255, 0, 0), 1)
    # 9显示图片
    cv2.imshow('Image', Frame)

    # 10暂停窗口
    if cv2.waitKey(1) == ord('q'):
        break
# 11释放资源
Webcam.release()
# #12销毁窗口
cv2.destroyAllWindows()
