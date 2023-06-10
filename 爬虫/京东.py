# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/10/11 20:34
# @Author : south(南风)
# @File : 京东.py
# Describe: 
# -*- coding: utf-8 -*-
import time
import json
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait  #等待页面加载完毕，寻找某些元素
from selenium.webdriver.support import expected_conditions as EC  ##等待指定标签加载完毕
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pymysql

class Sp:
    def __init__(self):
        self.url = "https://www.jd.com/"
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.browser = webdriver.Chrome(options=self.options)
        self.db = pymysql.connect(user='root', password='root', database='word', charset='utf8')
        self.cursor = self.db.cursor()

    def get_jd(self):
        self.browser.get(self.url)
        # 等待事件
        wait = WebDriverWait(self.browser, 100)
        wait.until(EC.presence_of_element_located((By.ID, 'key')))

        text = self.browser.find_element(By.ID, 'key')
        text.send_keys("美食")
        text.send_keys(Keys.ENTER)
        # 延时等待获取下一个页面的源码
        time.sleep(2)

    def get_data(self):
        page = 1
        while True:
            print(f"正在下载第{page}页")
            print("当前页面的URL:", self.browser.current_url)
            self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            data = self.browser.page_source
            # print(data)
            self.parse_data(data)

            wait = WebDriverWait(self.browser, 100)
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'pn-next')))
            try:
                self.browser.find_element(By.CLASS_NAME, 'pn-next').click()
                page += 1
            except NoSuchElementException as e:
                print(e)
                print("完毕")
                sys.exit(0)

    def parse_data(self, data):
        soup = BeautifulSoup(data, 'lxml')
        title = soup.select('.gl-i-wrap a em')
        price = soup.select('.gl-i-wrap .p-price strong i')
        name = soup.select('.gl-i-wrap .J_im_icon a')
        print(len(title))
        shop_info = {}
        for i, j, z in zip(title, price, name):
            t = i.get_text()
            p = j.get_text()
            n = z['title']
            shop_info['商品信息'] = t
            shop_info['商品价格'] = p
            shop_info['店铺名字'] = n
            # self.save(t, p, n)
            with open('shop_data.json', 'a', encoding='utf-8') as f:
                f.write(json.dumps(shop_info, ensure_ascii=False) + ',\n')

    def save(self, t, p, n):
        sql = 'insert into jd(title, price, name) values (%s, %s, %s)'
        self.cursor.execute(sql, [t, p, n])  # 执行sql语句
        self.db.commit()


if __name__ == '__main__':
    a = Sp()
    a.get_jd()
    a.get_data()


