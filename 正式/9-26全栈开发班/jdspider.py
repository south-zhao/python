import json
import sys
import time
from selenium import webdriver  # # 驱动浏览器
from selenium.webdriver.common.by import By  # 选择器
from selenium.webdriver.common.keys import Keys  # 按键
from selenium.webdriver.support.wait import WebDriverWait  # 等待页面加载完毕，寻找某些元素
from selenium.webdriver.support import expected_conditions as EC  ##等待指定标签加载完毕
from selenium.webdriver import ChromeOptions
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup

# http://www.jsons.cn/unicode/ 编码转换工具
class Spider():
    def __init__(self):
        # 登录接口
        self.url = 'https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F%3Fcu%3Dtrue%26utm_source%3Dbaidu-pinzhuan%26utm_medium%3Dcpc%26utm_campaign%3Dt_288551095_baidupinzhuan%26utm_term%3D0f3d30c8dba7459bb52f2eb5eba8ac7d_0_bab5f738418346a3818b34c9db67a523https%3A%2F%2Fwww.jd.com%2F%3Fcu%3Dtrue%26utm_source%3Dbaidu-pinzhuan%26utm_medium%3Dcpc%26utm_campaign%3Dt_288551095_baidupinzhuan%26utm_term%3D0f3d30c8dba7459bb52f2eb5eba8ac7d_0_bab5f738418346a3818b34c9db67a523'
        # self.url = 'https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_bab5f738418346a3818b34c9db67a523https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_bab5f738418346a3818b34c9db67a523'
        self.options = webdriver.ChromeOptions()  # 配置文件对象
        self.options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 写入参数
        self.browser = webdriver.Chrome(options=self.options)

    # 访问京东
    def get_jd(self):
        self.browser.get(self.url)

        # 微信登录
        self.browser.find_element(By.XPATH,'//*[@id="kbCoagent"]/ul/li[2]/a/span').click()
        # QQ登录
        # 自己完成

        # 等待事件
        wait = WebDriverWait(self.browser,280)
        wait.until(EC.presence_of_all_elements_located((By.ID,'key')))

        # 查找输入框 输入检索内容
        text_input = self.browser.find_element(By.ID,'key')
        text_input.send_keys('美食')
        text_input.send_keys(Keys.ENTER)
        time.sleep(1.5)

    # 获得响应内容
    def get_data(self):
        page_index = 1
        while True:
            print('正在下载第{}页'.format(page_index))
            print("当前页面的URL：",self.browser.current_url)
            self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(1.5)  # 60条
            data = self.browser.page_source
            # print(data)
            self.parse_data(data)

            # 等待翻页按钮
            wait = WebDriverWait(self.browser, 280)
            wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'pn-next')))

            try:
                # 翻页爬取
                self.browser.find_element(By.CLASS_NAME, 'pn-next').click()
                page_index+=1
            except NoSuchElementException as e:
                print(e)
                print('爬取完毕~')
                sys.exit(0)

    # 解析
    def parse_data(self,data):
        soup = BeautifulSoup(data,'lxml')
        title = soup.select('.gl-i-wrap a em')  # 商品名
        price = soup.select('.gl-i-wrap .p-price strong i')  # 价格
        name = soup.select('.gl-i-wrap .J_im_icon a')  # 店铺名字
        print(len(title))
        # 定义一个空字典
        shop_info = {}
        for titles,prices,names in zip(title,price,name):
            t = titles.get_text()
            p = prices.get_text()
            n = names['title']
            print(t)
            print(p)
            print(n)
            print('===========')
            shop_info['商品名字'] = t
            shop_info['商品价格'] = p
            shop_info['店铺名字'] = n
            with open('shop_data.json', 'a', encoding='utf-8')as f:
                # json.dumps将dict转为str   默认会将中文编码ascii编码
                f.write(json.dumps(shop_info,ensure_ascii=False)+',\n')




if __name__ == '__main__':
    a = Spider()
    a.get_jd()
    a.get_data()
