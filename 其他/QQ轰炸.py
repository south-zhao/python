# -*- coding: utf-8 -*-
# @Time : 2022/8/29 21:11
# @Author : south(南风)
# @File : QQ轰炸.py
# Describe:
# -*- coding: utf-8 -*-
# QQ信息的轰炸
import win32gui as gui
import win32con as con
# 确定发送对象
handle = gui.FindWindow(0, "昵称")
for i in range(100):
    # 2.准备要发送的内容
    # gui窗口 send发送  message消息  给窗口发送一个消息(黏贴)
    gui.SendMessage(handle, con.WM_PASTE)
    # 模拟按下enter，发信息
    gui.SendMessage(handle, con.WM_KEYDOWN, con.VK_RETURN)
