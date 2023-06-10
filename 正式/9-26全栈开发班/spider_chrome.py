"""
1，安装selenium
-- 命令：pip install selenium
-- 网络不稳的请换源安装：pip install selenium -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

2，打开百度，输入chrome webdriver，下载谷歌浏览器webdriver驱动
-- http://npm.taobao.org/mirrors/chromedriver/
-- 根据自己谷歌版本选择驱动器
-- 选择对应版本，如果没有对应版本选择跟谷歌版本相近但不超过谷歌版本的
-- 下载后解压

3，拷贝到python安装路径
-- 找到Lib目录
-- 进入site-packages目录，将下载好的webdriver驱动放进该目录文件里

4，配置环境变量
-- 将webdriver驱动所在文件路径复制
-- 添加到系统环境变量里的Path路径里

5，验证是否配置完成
-- from selenium import webdriver
a = webdriver.Chrome()
a.get('https://www.baidu.com/')


6，如果上述操作报错，执行以下方法：
-- 将下载的驱动放入python环境的Scripts的文件夹里
-- 再将路径添加到环境变量（如果安装python时勾选了自动添加环境变量这步可省略）

7，上述两种方法还报错，执行以下方法：
-- 将下载的驱动放进项目根目录
"""
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

a = webdriver.Chrome()
a.get('https://www.snnu.edu.cn')

time.sleep(3)
# text = a.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[2]/div[2]/div/div/div/div[1]/a")
# # a.find_element(By.LINK_TEXT, "会议安排").click()
#
# # a.back()
# # time.sleep(3)
# text_url = text.get_attribute('href')
# a.get(text_url)
# time.sleep(3)
# a.back()
# a.find_element(By.LINK_TEXT, "会议安排").click()
a.find_element(By.CLASS_NAME, "btn").click()
time.sleep(2)
text = a.find_element(By.ID, "showkeycode1020297")
text.send_keys("本科生")
text.send_keys(Keys.ENTER)
