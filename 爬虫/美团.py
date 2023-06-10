# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/10/18 10:04
# @Author : south(南风)
# @File : 美团.py
# Describe: 
# -*- coding: utf-8 -*-
import time
from lxml import etree
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MT:
    def __init__(self):
        self.url = "http://i.meituan.com/"
        self.browser = webdriver.Chrome()

    def get_data(self, url):
        self.browser.get(url)
        time.sleep(5)
        data = self.browser.page_source
        # print(data)
        return data

    def parse_data(self, data):
        xml = etree.HTML(data)
        name = xml.xpath('//*[@id="app"]/div/div/div[2]/section/section/div[2]/div[1]/div[1]//text()')
        sale = xml.xpath('//*[@id="app"]/div/div/div[2]/section/section/div[2]/div[1]/div[2]//text()')
        s_price = xml.xpath('//*[@id="app"]/div/div/div[2]/section/section/div[2]/div[2]/span[1]//text()')
        price = xml.xpath('//*[@id="app"]/div/div/div[2]/section/section/div[2]/div[2]/span[2]//text()')
        url = []
        for i in range(1, 20):
            self.browser.find_element(By.XPATH, f'//*[@id="app"]/div/div/div[2]/section/section[{i}]/div[2]/div[1]/div[1]').click()
            time.sleep(3)
            url.append(self.browser.current_url)
            self.browser.back()
            time.sleep(7)
        print(url)
        s_price = [i + "元" for i in s_price[::2]]
        print(price, s_price)

    def run(self):
        data = self.get_data(self.url)
        self.parse_data(data)


if __name__ == '__main__':
    a = MT()
    a.run()















