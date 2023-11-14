"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time :  2023/11/14 9:38
    @Author : south(南风)
    @File : snnu.py
    Describe:
    -*- coding: utf-8 -*-
"""
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait  #等待页面加载完毕，寻找某些元素
from selenium.webdriver.support import expected_conditions as EC  ##等待指定标签加载完毕
from selenium.common.exceptions import TimeoutException, NoSuchElementException


browser = webdriver.Chrome()

browser.get("http://202.117.144.205:8602/snnuportal/userstatus.jsp")

name = browser.find_element(By.XPATH, "/html/body/form/blockquote/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/input")

name.send_keys("42112003")

password = browser.find_element(By.XPATH, '/html/body/form/blockquote/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[2]/input')

password.send_keys("20040208datemY")

browser.find_element(By.XPATH, '/html/body/form/blockquote/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/table/tbody/tr[4]/td[2]/div/div[2]/label').click()

browser.find_element(By.XPATH, '/html/body/form/blockquote/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/table/tbody/tr[6]/td[2]/table/tbody/tr/td/a/img').click()
time.sleep(1)

browser.find_element(By.XPATH, '/html/body/div[3]/div[7]/div/button').click()

browser.close()




