"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/7/26 8:49
    @Author : south(南风)
    @File : 人口数据.py
    Describe:
    -*- coding: utf-8 -*-
"""
import requests
from lxml import etree
import pandas as pd

url = "https://zhuanlan.zhihu.com/p/634146715"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183"}

response = requests.get(url=url, headers=headers)

text = response.text

xml = etree.HTML(text)
# 1-75
res = []
for i in range(1, 76):
    data = xml.xpath(f'/html/body/div[1]/div/main/div/article/div[1]/div/div/div[2]/table/tbody/tr[{i}]//text()')
    if i == 2:
        data = [1949, 54167, 0, 0, 0, 36, 20, 16]
        res.append(data)
    elif i > 2:
        data1 = []
        for j in data:
            if "," in j:
                res1 = j.split(",")
                da = int(res1[0] + res1[1])
                data1.append(da)
            elif "." in j:
                data1.append(float(j))
            else:
                data1.append(int(j))

        res.append(data1)
    else:
        res.append(data)

df = pd.DataFrame(res[1:], columns=res[0])
df.to_csv("人口数量表.csv", index=False)





