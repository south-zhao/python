"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/6/5 10:06
    @Author : south(南风)
    @File : 二维码.py
    Describe:
    -*- coding: utf-8 -*-
"""
import qrcode
# 创建二维码对象
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
# 设置要生成的字符串
data = 2386
# 添加数据到二维码对象中
qr.add_data(data)
# 编译二维码对象
qr.make(fit=True)
# 创建二维码图片
img = qr.make_image(fill_color='black', back_color='white')
# 保存二维码图片
img.show()


