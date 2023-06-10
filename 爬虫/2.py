# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/9/24 17:13
# @Author : south(南风)
# @File : 2.py
# Describe: 
# -*- coding: utf-8 -*-
import requests
from tqdm import tqdm
from pprint import pprint
import json

url = "https://data.services.jetbrains.com/products/releases?code=IIU&latest=true&type=release&build=&_=1667201004095"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 "
                  "Safari/537.36 Edg/107.0.1418.24 "
}
response = requests.get(url=url, headers=headers)
# print(response)
# pprint(response.text)
Iiu = response.json()["IIU"]
# print(type(Iiu))
# print(Iiu)
data = Iiu[0]
# print(data)
data1 = data["downloads"]["windows"]["link"]
# print(data1)
url1 = data1
# response1 = requests.get(url=url1, headers=headers).content
# response1 = requests.get(url=url1, headers=headers, timeout=3)
response1 = requests.get(url=url1, headers=headers, timeout=3, stream=True)
# total = int(response1.headers.get('content-length', 0))
data_size = int(response1.headers['Content-Length'])/1024/1024
# print(response1)
with open("idea.exe", "wb") as f:
    # , tqdm(desc='idea.exe', total=total, unit='iB', unit_scale=True,
    #                                        unit_divisor=1024, ) as bar
    for data in tqdm(response1.iter_content(1024*1024), total=data_size, desc='正在下载', unit='MB'):
        size = f.write(data)
        # bar.update(size)
print("over")
