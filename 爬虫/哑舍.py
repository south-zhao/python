"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/4/10 22:51
    @Author : south(南风)
    @File : 哑舍.py
    Describe:
    -*- coding: utf-8 -*-
"""
import requests
from lxml import etree
import time

begin = time.time()
for x in range(2206, 2236):
    url = f"https://www.biqiuge8.cc/book/21311/1397{x}.html"


    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 "
                      "Safari/537.36 "
    }

    response = requests.get(url=url, headers=headers)
    response.encoding = "gbk"

    content = response.text

    title = etree.HTML(content).xpath('/html/head/title/text()')

    content1 = etree.HTML(content).xpath('//*[@id="content"]/text()')

    with open("哑舍\\" + title[0] + ".txt", 'w', encoding="utf-8") as f:
        f.writelines(content1)
    print(title[0] + "已完成")
    print("------------")

#
end = time.time()
print(end - begin)

print("over!")









