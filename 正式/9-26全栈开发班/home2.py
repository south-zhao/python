# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/10/1 14:01
# @Author : south(南风)
# @File : home2.py
# Describe: 爬取招聘信息
# -*- coding: utf-8 -*-
import time

import openpyxl
import requests
import pandas as pd
import json
from jsonpath import jsonpath  # pip install jsonpath
from openpyxl import workbook  # pip install openpyxl
import sys

# wb = workbook.Workbook()  # 创建Excel对象
# wb = openpyxl.load_workbook('新闻.xlsx')
# ws = wb.active  # 激活当前表
# ws.append(['标题', '媒体', '发布时间'])


# url = 'https://i.news.qq.com/trpc.qqnews_web.kv_srv.kv_srv_http_proxy/list'
# ips = {
#     'http': '113.235.75.15:4213',
#     'https': '113.235.75.15:4213'
# }
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
# }
#
# data = {
#     'sub_srv_id': '24hours',
#     'srv_id': 'pc',
#     'offset': '0',
#     'limit': '20',
#     'strategy': '1',
#     'ext': '{"pool":["top"],"is_filter":7,"check_type":true}',
# }
#
# r = requests.get(url=url, headers=headers, params=data, proxies=ips).json()

# with open('1.txt', 'w', encoding='utf-8') as f:
#     json.dump(r, f, ensure_ascii=False)
# with open('1.txt', 'r', encoding='utf-8') as f:
#     content = json.load(f)
# time = jsonpath(content, '$..create_time')
# for i in time:
#     print(i)
# title = jsonpath(content, '$..title')
# media_name = jsonpath(content, '$..media_name')
# for i, j, z in zip(title, media_name, time):
#     #     print(i + "   " + j)
#     my_list = [i, j, z]
#     ws.append(my_list)
# wb.save('新闻.xlsx')
data = pd.read_excel('新闻.xlsx', sheet_name='Sheet')
# a = set(data['媒体'])
# for i in a:
#     print(i)

name = input('你想查询的媒体:')
length = 0
time1 = []
for i, j, z in zip(data['标题'], data['媒体'], data['发布时间']):
    if j == name:
        length += 1
        time1.append(z)
        print(i + '   ' + j + '    ' + z)
time1.sort()
# print(time1)
print(f"\n{name}一共发了{length}条新闻, 最早的一条新闻是{time1[0]}发的")

# time.mktime(time.strptime(i, "%Y-%m-%d %H:%M:%S"))


