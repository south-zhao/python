"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/3/22 19:30
    @Author : south(南风)
    @File : 网站.py
    Describe:
    -*- coding: utf-8 -*-
"""
import requests

url = "http://q1.getmc.cn:15922/"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/111.0.0.0 Safari/537.36"}

# for i in range(1000):
res = requests.get(url=url, headers=headers)
res.encoding = res.apparent_encoding
print(res.text)
# print("0k")


