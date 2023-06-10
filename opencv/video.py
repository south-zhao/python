"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/4/13 17:25
    @Author : south(南风)
    @File : video.py
    Describe:捕捉视频
    -*- coding: utf-8 -*-
"""
import numpy as np
import cv2

# cap = cv2.VideoCapture(0)
# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#     # Our operations on the frame come here
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     # Display the resulting frame
#     cv2.imshow('frame', gray)
#     if cv2.waitKey(0):
#         break
#     # When everything done,release the capture
# cap.release()
# cv2.destroyAllWindows()
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
