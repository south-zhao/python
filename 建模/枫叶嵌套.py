"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/7/18 10:48
    @Author : south(南风)
    @File : 枫叶嵌套.py
    Describe:
    -*- coding: utf-8 -*-
"""
import cv2
import numpy as np
import math

# 将图片文件命名为fy.jpg,与程序放在同一目录下
img = cv2.imread('fy.jpg')
rows, cols, chnl = img.shape
x1 = np.linspace(1, 90, 200)
data1 = []
for jiao in x1:
    # 旋转参数：旋转中心，旋转角度，scale
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), jiao, 1)
    # 参数：原始图像，旋转参数，元素图像宽高
    rotated = cv2.warpAffine(img, M, (cols, rows))

    grayimg = cv2.cvtColor(rotated, cv2.COLOR_BGR2GRAY)

    # 二值化
    ret, binary_img = cv2.threshold(grayimg, 240, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(binary_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cont in contours:
        # 对每个轮廓点求最小外接矩形
        rect = cv2.minAreaRect(cont)
        # cv2.boxPoints可以将轮廓点转换为四个角点坐标
        box = cv2.boxPoints(rect)
        # 这一步不影响后面的画图，但是可以保证四个角点坐标为顺时针
        startidx = box.sum(axis=1).argmin()
        box = np.roll(box, 4 - startidx, 0)
        # 在原图上画出预测的外接矩形
        box = box.reshape((-1, 1, 2)).astype(np.int32)
        cv2.polylines(grayimg, [box], True, (0, 255, 0), 1)
        data = []
        for i in box:
            data.append(list(i[0]))
        data.sort()
        op1 = math.pow(data[0][0] - data[1][0], 2) + math.pow(data[0][1] - data[1][1], 2)
        op2 = math.pow(data[0][0] - data[2][0], 2) + math.pow(data[0][1] - data[2][1], 2)
        data = []
        if op1 > 10 and op1 != 98596:
            data1.append([jiao, abs((op1 / op2) - 1), op1, op2])
data1.sort()
# 正方形的边长
length = int(math.sqrt(data1[0][2]))
print(f"旋转角度为{data1[0][0]}, 正方形的边长为{length}")
