# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/10/4 22:40
# @Author : south(南风)
# @File : 笔趣阁.py
# Describe: 
# -*- coding: utf-8 -*-
import requests
from lxml import etree

for x in range(531, 550):
    url = f"http://www.beqege.cc/15565/207{x}.html"
    ips = {'http': '124.161.43.77:4258', 'https': '124.161.43.77:4258'}
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 '
                      'Safari/537.36 '
    }
    r = requests.get(url, headers=headers, proxies=ips, timeout=7)

    # print(r)
    content = r.text
    title = etree.HTML(content).xpath('//*[@id="content_read"]/div/div[2]/h1')
    content1 = etree.HTML(content).xpath('//*[@id="content"]/p')
    if len(title) == 0:
        continue
    with open("1//" + title[0].text + ".txt", 'w', encoding="utf-8") as f:
        for i in content1:
            if i.text is not None:
                i = i.text
                f.write(i + "\n")
    print("over")
# print(r.text)
# with open("2.html", 'w', encoding="utf-8") as f:
#     f.write(r.text)



