# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/10/6 15:51
# @Author : south(南风)
# @File : 情话.py
# Describe: 爬取情话
# -*- coding: utf-8 -*-
import requests
from lxml import etree
import pymysql


class Spider:
    def __init__(self):
        self.url = "https://www.qinghuawang.net/"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }
        self.ips = {'http': '182.37.69.95:4214', 'https': '182.37.69.95:4214'}
        self.db = pymysql.connect(user='root', password='root', database='word', charset='utf8')
        self.cursor = self.db.cursor()

    def get_data(self, url):

        response = requests.get(url=url, headers=self.headers, proxies=self.ips)
        response.encoding = response.apparent_encoding
        if response.status_code == 200:
            return response.text

    def prase_one(self, data):
        xml1 = etree.HTML(data)
        type1 = xml1.xpath('//div[@class="rightBar1"]/div[1]/ul/li/a/text()')
        href1 = xml1.xpath('//div[@class="rightBar1"]/div[1]/ul/li/a/@href')
        for i, j in zip(href1, type1):
            self.prase_two(j, i)

    def prase_two(self, type_s, url):
        response2 = self.get_data(url)
        xml2 = etree.HTML(response2)
        title = xml2.xpath('//div[@class="infoList"]/ul/li/a/text()')
        href2 = xml2.xpath('//div[@class="infoList"]/ul/li/a/@href')
        for i, j in zip(title, href2):
            self.prase_three(type_s, i, j)

    def prase_three(self, type_s, title, url):
        response3 = self.get_data(url)
        xml3 = etree.HTML(response3)
        word = xml3.xpath('//div[@class="articleText"]/p/text()')
        time = word[0]
        for i in word[1:]:
            self.save(type_s, title, time, i)
            print('over')

    def save(self, ty, ti, tim, wo):
        sql = 'insert into hua(type, title, time, word) values (%s, %s, %s, %s)'
        self.cursor.execute(sql, (ty, ti, tim, wo))  # 执行sql语句
        self.db.commit()  # 提交

    def main(self):
        html_data = self.get_data(self.url)
        self.prase_one(html_data)


if __name__ == '__main__':
    s = Spider()
    s.main()
