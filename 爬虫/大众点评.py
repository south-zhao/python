# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/10/13 20:03
# @Author : south(南风)
# @File : 大众点评.py
# Describe: 
# -*- coding: utf-8 -*-
import os
import re

from lxml import etree

from config import texts
import requests
from fontTools.ttLib import TTFont


class Dz:
    def __init__(self):
        self.url = "https://www.dianping.com/xian/ch10/g110r467"

        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': 'navCtgScroll=0; showNav=#nav-tab|0|1; fspop=test; cy=17; cye=xian; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=183d139ccb6c8-075c6eff2f75d7-26021f51-e1000-183d139ccb6c8; _lxsdk=183d139ccb6c8-075c6eff2f75d7-26021f51-e1000-183d139ccb6c8; _hc.v=3b4336f9-4d7b-6558-eda1-38b5f2840b1f.1665662570; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1665662570; s_ViewType=10; lgtoken=05915b7dc-381d-4cdd-819e-301d20438c21; WEBDFPID=3w9vywyu0vwz56wx1ux7uw39zuwzw57u816w86z13w5979585v2uw93y-1981022617210-1665662616793WGGCIGAfd79fef3d01d5e9aadc18ccd4d0c95071572; _lxsdk_s=183d139ccb6-a02-97e-f40%7C%7C75; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1665662692; s_ViewType=10',
            'Referer': 'https://www.dianping.com/xian/ch10/g110',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        }

    def get_html_data(self):
        response = requests.request("GET", self.url, headers=self.headers)

        data = response.text

        return data

    def parse_data(self, data):
        r1 = '<link rel="stylesheet".*?type="text/css".href="(.*?)">'
        font_link = 'https:' + re.findall(r1, data, re.S)[1]
        # print(font_link)
        font_response = requests.get(font_link).text
        num_link = re.findall(r'PingFangSC-Regular-shopNum.*?embedded-opentype.*?url\("(.*?)"\);', font_response, re.S)

        tag_link = re.findall(r'PingFangSC-Regular-tagName.*?embedded-opentype.*?url\("(.*?)"\);', font_response, re.S)

        woff_url = num_link + tag_link
        woff_href = ['https:' + x for x in woff_url]
        return woff_href

    def save_font(self, link):
        content = requests.get(link).content
        if not os.path.exists('font_doc'):
            os.mkdir('font_doc')
        file_name = link.split('/')[-1]
        with open('font_doc' + '/' + file_name, 'wb') as f:
            f.write(content)
        return file_name

    def get_font_map(self, file_name=None):
        t = TTFont('font_doc' + '/' + file_name)
        file_name1 = file_name.split('.')[0]
        t.saveXML('font_doc' + '/' + f'{file_name1}.xml')
        font_names = t.getGlyphOrder()[2:]
        code_dict = {}
        for index, value in enumerate(texts):
            code_dict[font_names[index]] = value

        jiemi_dict = {}
        for k, v in code_dict.items():
            if k.startswith('uni'):
                key = k.replace('uni', '&#x')
                key_a = key + ';'
                jiemi_dict[key_a] = v
            else:
                jiemi_dict[k] = v

        return jiemi_dict

    def parse_rep_data(self, jiemi_dict, response):
        for k, v in jiemi_dict.items():
            response = response.replace(k, v)
        # print(response)
        return response

    def parse_response(self, response=None, response1=None):
        if response:
            xml = etree.HTML(response)
            ping = xml.xpath('//div[@class="comment"]/a[@module="list-readreview"]//text()')
            jun = xml.xpath('//div[@class="comment"]/a[@class="mean-price"]//text()')
            print(ping)
            print(jun)
        if response1:
            xml = etree.HTML(response1)
            addr = xml.xpath('//div[@class="tag-addr"]//span[@class="tag"]//text()')
            print(addr)


    def run(self):
        html_data = self.get_html_data()
        num_link = self.parse_data(html_data)
        jiemi_list = []
        for i in num_link:
            file_name = self.save_font(i)
            jiemi_dict = self.get_font_map(file_name)
            jiemi_list.append(jiemi_dict)
        response = self.parse_rep_data(jiemi_list[0], html_data)
        # self.parse_response(response)

        response1 = self.parse_rep_data(jiemi_list[1], html_data)

        self.parse_response(response=response, response1=response1)


if __name__ == '__main__':
    a = Dz()
    a.run()
