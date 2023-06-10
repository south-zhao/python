'''
安装MySQL: https://blog.csdn.net/qq_32630565/article/details/84455572

作业：
爬取 https://www.qinghuawang.net/链接中名人名句模块内的所有类别文章，具体有以下类别：
    -- 经典句子 说说句子 唯美句子 伤感句子 青春励志

关于保存要求：把类别标题以及文章内容存入数据库
关于数据库的表设计：
        要求数据库的数据库名统一取"xiaoxiao"
        要求数据库的表名统一取"demo"
        要求要有自增的id字段
        保存标题的字段统一取“name”
        保存文章的字段统一取“text”
'''
import requests
from lxml import etree
import pymysql  # pip install pymysql


# url = 'https://www.qinghuawang.net/haojuzi/jingdian/'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
# }
class Spider():
    def __init__(self):  # 初始化方法  当创建了一个类的实例之后 就会立马调用到这个init方法
        self.url = 'https://www.qinghuawang.net/haojuzi/jingdian/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }
        # 连接sql环境               # 用户名     密码              数据库名             编码
        self.db = pymysql.connect(user='root', password='admin', database='xiaoxiao', charset='utf8')
        self.cursor = self.db.cursor()  # 获取操作游标

    # 请求
    def get_data(self, url):
        response = requests.get(url, headers=self.headers)
        # response.encoding = 'utf-8'
        response.encoding = response.apparent_encoding  # 获取网站本身编码
        if response.status_code == 200:
            return response.text

    # 解析一级页面  解析列表页的详情内容
    def parse_one_data(self, data):
        xml = etree.HTML(data)
        title = xml.xpath('//ul[@class="infoListUL mt5"]/li/a/text()')  # 标题
        href = xml.xpath('//ul[@class="infoListUL mt5"]/li/a/@href')  # 详情链接
        for titles, hrefs in zip(title, href):
            print(titles)
            print(hrefs)
            print('======')
            self.parse_two_data(hrefs)

    # 解析二级页面  解析详情页的详情内容
    def parse_two_data(self, url):
        # 先像详情链接发请求
        contents = self.get_data(url)  # 二级页面的网页源码
        # print("二级页面：",contents)
        xml = etree.HTML(contents)
        c = xml.xpath('//div[@class="articleText"]/p/text()')
        print("文章", c)
        self.save_data(c)

    # 保存
    def save_data(self, qinghua):
        sql = 'insert into biao(text) values (%s)'
        self.cursor.execute(sql, str(qinghua))  # 执行sql语句
        self.db.commit()  # 提交

    # 统一调用功能方法
    def main(self):
        html_data = self.get_data(self.url)
        self.parse_one_data(html_data)


if __name__ == '__main__':
    # 多个类别的链接
    url_list = [
        'https://www.qinghuawang.net/haojuzi/jingdian/',
        'https://www.qinghuawang.net/haojuzi/shuoshuo/',
        'https://www.qinghuawang.net/haojuzi/weimei/'
    ]
    for url in url_list:
        print("类别的链接:", url)
        s = Spider()
        s.main()
    # data = s.get_data()
    # # print(data)
    # s.parse_data(data)
