"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/5/27 14:20
    @Author : south(南风)
    @File : test.py
    Describe:
    -*- coding: utf-8 -*-
"""
from bs4 import BeautifulSoup
import requests
import pandas as pd


class SpiderHours(object):
    def __init__(self):
        self.url = "http://www.creprice.cn/rank/cityforsale.html"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            "Cookie": "cityredata=1245960d33d174122151e3280a2630a2; city=sq; userchannel=EL-cityhouse; Hm_lvt_c2a7a3cec6f9dd8849155424efab19c7=1562643454,1562643606,1562644057; Hm_lpvt_c2a7a3cec6f9dd8849155424efab19c7=1562644057"}

    def request_page(self):
        response = requests.get(self.url, headers=self.headers)
        ret = response.content.decode("utf-8")
        soup = BeautifulSoup(ret, features="lxml")
        content = soup.find_all("th")
        # print(content)

        temp_list = list()
        for info in content:  # 遍历数据
            temp_info = info.text.strip()  # 删除\n转义符
            temp_info = temp_info.replace(",", "")  # 删除数据中的","
            if len(temp_list) < 5:  # 整理数据，每行5个输出
                temp_list.append(temp_info)
            else:  # 第一行获取的数据名称有重复的，替换一下
                if temp_list == ['序号', '城市名称', '所属地级市', '城市规模\n城市规模', '单价（元/㎡）\n单价（元/㎡）']:
                    temp_list = ['序号', '城市名称', '所属地级市', '城市规模', '单价（元/㎡）']
                # a是追加
                with open("2022年全国房价.csv", "a") as f:  # 写入csv文件,这里每次都要打开，以后有空可以优化
                    f.write(",".join(temp_list) + "\n")
                    print(",".join(temp_list))
                temp_list = list()
                temp_list.append(temp_info)


if __name__ == '__main__':
    spider = SpiderHours()
    spider.request_page()
    data = pd.read_csv(r'2022年全国房价.csv', encoding='gbk')
    print(data.head(3))
    print(data.shape)
    print(data.info())
    print(data.describe())
    print(data.groupby('城市规模')['单价（元/㎡）'].mean())
    print(data.isnull().sum())  # 查看缺失值，统计缺失值，填充缺失值
    print(data.duplicated().sum())  # 去除重复数据
    print(data.城市名称.apply(len))  # 城市名称长度
    data['所属地级市'] = data['所属地级市'].apply(lambda x: 0 if x == '北京' else 1)  # 北京地级市
    print(data['所属地级市'])
    print(data.城市规模.value_counts())  # 城市规模
    print(data[(data['单价（元/㎡）'] < 15000) & (data['单价（元/㎡）'] > 10000)])  # 筛选数据大于13小于15
