"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/4/5 10:46
    @Author : south(南风)
    @File : Edge.py
    Describe:
    -*- coding: utf-8 -*-
"""
from selenium import webdriver
from selenium.webdriver.common.by import By  #选择器
from selenium.webdriver.common.keys import Keys   #按键
import time
driver = webdriver.Edge()
url = "https://mooc1.chaoxing.com/ztnodedetailcontroller/visitnodedetail?courseId=218586458&knowledgeId=439604122&_from_=232478606_71713389_195572660_86c6e6e49a5e2ee2097472a1b34a9fec&rtag=&nohead=1"
time.sleep(3)
driver.get(url)
for i in range(20):
    by_xpath = driver.find_element(By.XPATH, '//*[@id="caContentBox"]/div[2]/a[2]')
    time.sleep(60*2)
    by_xpath.send_keys(Keys.ENTER)

driver.close()
