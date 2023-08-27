# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/10/22 18:15
# @Author : south(南风)
# @File : sp.py
# Describe: 
# -*- coding: utf-8 -*-
import requests

url = 'https://www.a2mu.com/p/204230-2-19.html'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

response = requests.get(url=url, headers=headers)

print(response.text)




