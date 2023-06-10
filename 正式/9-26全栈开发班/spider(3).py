import requests
from jsonpath import jsonpath
import csv
import re

from matplotlib import pyplot as plt

'''
微博评论移动端：https://m.weibo.cn/detail/4813628149072458
'''

class Weibo():
    def __init__(self):
        # 用户输入接口信息
        self.user_url = 'https://data.weibo.com/index/ajax/newindex/searchword'
        self.user_data = {
            'word': user_text,
        }
        # 数据接口信息
        self.url = "https://data.weibo.com/index/ajax/newindex/getchartdata"
        self.payload = {
            'wid': '1091324264913',  # 关键词ID
            'dateGroup': '1hour',
        }
        self.headers = {
            'cookie': 'SUB=_2AkMUamEEf8NxqwJRmfAUxGzkZIRxzA7EieKiNpDfJRMxHRl-yT9jqhYYtRB6P-pP61QvA5JI4oXzwAjVYZtA7JPRlH07; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFMUbTi7AeRziiGIU1kxV_7; SINAGLOBAL=1957067357592.9653.1664544424005; ULV=1664544424034:1:1:1:1957067357592.9653.1664544424005:; WEB3=7ef756770a4aba698ee9731722a669fa; WEB3=e72c40e6ad1dc5425648bec99917c3a3',
            'referer': 'https://data.weibo.com/index/newindex?visit_type=trend&wid=1091324264913',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

    # 像用户接口发请求 获得wid
    def get_user_data(self):
        response = requests.request("POST", self.user_url, headers=self.headers, data=self.user_data)
        if response.status_code == 200:
            text_data = response.text
            # print(text_data)
            wid = re.findall(r'<li\swid=\\"(.*?)\\"\sword.*?>', text_data, re.S)[0]
            return wid

    # 请求接口数据
    def get_data(self):
        w = self.get_user_data()
        print(w)
        self.payload['wid'] = w
        response = requests.request("POST", self.url, headers=self.headers, data=self.payload)
        if response.status_code == 200:
            return response.json()

    # 解析时间和指数
    def parse_data(self, data):
        x_time = jsonpath(data, '$..x')[0]
        s_data = jsonpath(data, '$..s')[0]
        # plt.plot(x_time, s_data)
        # # plt.savefig("1.png")
        # plt.show()
        # 开启一个文件
        f = open('weibo.csv', 'w', newline='', encoding='gbk')
        csv_w = csv.writer(f)  # CSV文件对象
        csv_w.writerow(['关键词', '时间', '日期'])  # 按行写入数据
        for x_times, s_datas in zip(x_time, s_data):
            csv_w.writerow(['病毒', x_times, s_datas])  # 按行写入数据
            print(x_times, '--->', s_datas)
        f.close()

    def main(self):
        list_data = ['1hour', '1day', '1month', '3month']  # 时间板块
        for i in list_data:
            self.payload['dateGroup'] = i  # 切换4大板块爬取

            json_data = self.get_data()
            # print(json_data)
            self.parse_data(json_data)


if __name__ == '__main__':
    user_text = input('请输入你要检索的关键字：')
    s = Weibo()
    s.main()
