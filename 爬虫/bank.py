# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/10/17 14:58
# @Author : south(南风)
# @File : bank.py
# Describe: 
# -*- coding: utf-8 -*-
import time
from lxml import etree
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://xkz.cbirc.gov.cn/jr/')
browser.find_element(By.ID, 'ext-gen48').click()
time.sleep(5)
browser.find_element(By.XPATH, '//*[@id="ext-gen68"]/div[4]').click()

browser.find_element(By.ID, 'ext-gen66').click()
time.sleep(10)
browser.find_element(By.XPATH, '//*[@id="ext-gen72"]/div[2]').click()

browser.find_element(By.ID, 'ext-gen51').click()
# wait = WebDriverWait(browser, 10)
# wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ext-gen78"]/div[2]')))
time.sleep(10)
# browser.find_element(By.XPATH, '//*[@id="ext-gen78"]/div[2]').click()

browser.find_element(By.ID, 'reportSearch').click()
time.sleep(5)
data = browser.page_source

xml = etree.HTML(data)
num = xml.xpath('//*[@id="ext-gen14"]/div/table/tbody/tr/td[2]/div//text()')
bianma = xml.xpath('//*[@id="ext-gen14"]/div/table/tbody/tr/td[3]//text()')
liushui = xml.xpath('//*[@id="ext-gen14"]/div/table/tbody/tr/td[4]//text()')
name = xml.xpath('//*[@id="ext-gen14"]/div/table/tbody/tr/td[5]/div/a//text()')
date = xml.xpath('//*[@id="ext-gen14"]/div/table/tbody/tr/td[7]/div//text()')
date1 = xml.xpath('//*[@id="ext-gen14"]/div/table/tbody/tr/td[8]/div//text()')
for n, b, l, na, da, da1 in zip(num, bianma, liushui, name, date, date1):
    print(n + "  " + b + "  " + l + "  " + na + "  " + da + "  " + da1)
    print("==========")











