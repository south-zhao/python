# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/9/29 9:52
# @Author : south(南风)
# @File : day1.py
# Describe: 爬取豆瓣读书的信息
# -*- coding: utf-8 -*-
import csv
import os
import requests
import re

url = "https://book.douban.com/latest?icn=index-latestbook-all"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 "
                  "Safari/537.36 "
}

# res = requests.get(url=url, headers=headers, timeout=3)

# print(res)
# print(res.text)

with open('1.html', 'r', encoding='utf-8') as f:
    content = f.read()
# content = res.text
# print(content)
z = '<li\sclass="media\sclearfix".*?<img\sclass="subject-cover".*?src="(.*?)"/>.*?<a\sclass="fleft"' \
    '\shref="(.*?)">(.*?)</a>.*?<p\sclass="subject-abstract\scolor-gray">(.*?)</p>.*?' \
    '<span\sclass="font-small\scolor-red\sfleft">(.*?)</span>.*?' \
    '<a\shref=".*?">(.*?)</a>'    # 解析表达式
result = re.findall(z, content, re.S)
# print(result)

# f = open('douban.csv', 'a', encoding="utf-8-sig", newline="")
# f.write(img, href, name)
# csv_writer = csv.writer(f)

# 3.构建列表头
# csv_writer.writerow(["书籍名", "作者", "出版时间", "出版社", "原价", "现价", "评分"])
for data in result:
#     # print(data)
    img = data[0]
    href = data[1]
    name = data[2]
    author = data[3].strip()
    score = data[4]
    price = data[5]
    price1 = re.findall('[\u4e00-\u9fa5]{3}\s(.*?)元', price, re.S)
    author_data = re.findall('(.*?)\s/\s(.*?)\s/\s(.*?)\s/\s(.*?)\s/\s.*?', author)
    # print(author_data)
    # print(price1[0])
    for i in author_data:
        author_name = i[0]
        time = i[1]
        store = i[2]
        origin_price = i[3]

#     # 4. 写入csv文件内容
#         csv_writer.writerow([name, author_name, time, store, origin_price, price1[0], score])
    # if not os.path.exists('DATA'):
    #     os.makedirs('DATA')
    # img_data = requests.get(url=img, headers=headers).content
    # with open('DATA/{}.jpg'.format(name), 'wb') as f:
    #     f.write(img_data)
# f.close()

