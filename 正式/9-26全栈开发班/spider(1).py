import requests
from bs4 import BeautifulSoup
import re
import time
import random
# 基于速度的反爬 time  最可靠的一种反反爬手段
# 固定时间 更容易被对方发现你是爬虫   -- 随机
# 作业：  find_all方法解析一遍    select()选择器解析一遍
# 请求
def get_data():
    resposne = requests.get(page_url, headers=headers)
    if resposne.status_code == 200:
        html_data = resposne.text
        # print(html_data)
        return html_data

# 解析
def parse_data(data):
    soup = BeautifulSoup(data, 'lxml')
    title = soup.find_all('a', {'class': 'twoline'})  # 标题
    contents = soup.find_all('p', {'class': 'content__list--item--des'})  # 信息
    price = soup.find_all('span', {'class': 'content__list--item-price'})  # 价格
    # print(title)
    # print(contents)
    for titles, contentss, prices in zip(title, contents, price):
        t = titles.get_text().strip()
        h = "https://cs.lianjia.com" + titles['href']  # https://cs.lianjia.com/zufang/CS1683730393867485184.html
        c = contentss.get_text().strip()
        p = prices.get_text()
        # 二次处理信息字符
        css = re.sub('/|\n', '', c).replace('     ', '')
        print(t)
        print(h)
        print(css)
        print(p)
        print('====================')

if __name__ == '__main__':
    # url = 'https://cs.lianjia.com/zufang/pg{}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        # 页面请求来源
        'Referer': 'https://cs.lianjia.com/zufang/pg100'
    }
    for i in range(1,101):
        print('正在打印第{}页'.format(i))
        page_url = 'https://cs.lianjia.com/zufang/pg{}'.format(i)
        print("每一页链接：",page_url)
        html_data = get_data()
        t = random.randint(2,5)
        time.sleep(t)
        parse_data(html_data)
