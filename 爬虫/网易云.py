# -*- coding: utf-8 -*-
# @Time : 2022/8/26 20:00
# @Author : south(南风)
# @File : 网易云.py
# Describe:
# -*- coding: utf-8 -*-
# 爬取网易云音乐
import re

import requests

url = "https://music.163.com/discover/toplist?id=3778678"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/104.0.0.0 Safari/537.36 '
}

response = requests.get(url=url, headers=headers)
# print(response)
# print(response.text)


re_data = re.findall('<li><a href="/song\?id=(\d+)">(.*?)</a></li>', response.text)
print(re_data)

for num_id, name in re_data:
    # print(num_id, name)
    music_url = f'https://music.163.com/song/media/outer/url?id={num_id}.mp3'
    response_1 = requests.get(music_url, headers=headers).content
    # print(response_1)
    with open('music\\' + name + '.mp3', 'wb') as f:
        f.write(response_1)
    print(num_id, name)



