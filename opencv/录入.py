"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/6/6 23:22
    @Author : south(南风)
    @File : 录入.py
    Describe:
    -*- coding: utf-8 -*-
"""
import numpy as np
import cv2
import os

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(
    os.path.join(r"C:\Users\xjiez\Desktop\Code\python\opencv", "haarcascade_frontalface_default.xml"))
sampleNum = 3000

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # 增加例子数
        sampleNum = sampleNum + 1

        # 把照片保存到数据集文件夹
        cv2.imencode('.jpg', gray[y: y + h, x: x + w])[1].tofile("Training Data/赵鑫杰/" + str(sampleNum) + ".jpg")
    cv2.imshow("img", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    if sampleNum == 300:
        break

cap.release()
cv2.destroyAllWindows()
# img = cv2.imdecode(np.fromfile(os.path.join("Training Data/严天宇", "1.jpg"), dtype=np.uint8), cv2.IMREAD_COLOR)

# cv2.imencode('.jpg', img)[1].tofile("赵鑫杰/6.jpg")

