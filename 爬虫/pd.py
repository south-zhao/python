"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/6/12 15:46
    @Author : south(南风)
    @File : pd.py
    Describe:
    -*- coding: utf-8 -*-
"""
import requests
for i in range(1, 49):
    url = f"https://s3.ananas.chaoxing.com/sv-w8/doc/db/da/e1/433bc86848271a06ba1e1602f0231e29/thumb/{i}.png"
    headers = {"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43"}
    con = requests.get(url=url, headers=headers)
    with open(f"3/{i}.png", "wb") as f:
        f.write(con.content)
