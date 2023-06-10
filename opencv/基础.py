"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/4/13 16:45
    @Author : south(南风)
    @File : 基础.py
    Describe: opencv读取图片等简单操作
    -*- coding: utf-8 -*-
"""
import os.path
from PIL import Image

import cv2

cv2.namedWindow("img2", cv2.WINDOW_NORMAL)  # 可以调整窗口大小，不设置则不可调整

img = cv2.imread("img/img.png", 0)
img1 = cv2.imread("img/img.png", 1)
img2 = cv2.imread("img/1.jpg", 0)

cv2.imwrite(os.path.join("Training Data", "6.jpg"), img)

cv2.imshow("img", img)
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)

cv2.waitKey(0)

# cv2.destroyWindow("img")
cv2.destroyAllWindows()
