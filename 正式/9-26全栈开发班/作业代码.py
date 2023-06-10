import requests
from lxml import etree
import pymysql  # pip install pymysql

'''
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


class Spider():
    def __init__(self):  # 初始化方法  当创建了一个类的实例之后 就会立马调用到这个init方法
        # self.url = 'https://www.qinghuawang.net/haojuzi/jingdian/'
        self.url = 'https://www.qinghuawang.net/'  # 首页链接
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

    # 解析首页https://www.qinghuawang.net/中的‘名人名句’模块  因此self.url的起始链接需要更改成首页链接
    def parse_module_data(self, module_data):
        xml = etree.HTML(module_data)
        module_name = xml.xpath('//div[@class="indexRightBox mt10"][1]//ul/li/a/text()')
        module_href = xml.xpath('//div[@class="indexRightBox mt10"][1]//ul/li/a/@href')
        return module_name, module_href

    # 解析列表页的详情内容
    def parse_one_data(self, url):
        contents = self.get_data(url)  # 像模块链接发起请求，获得列表页源码
        xml = etree.HTML(contents)
        title = xml.xpath('//ul[@class="infoListUL mt5"]/li/a/text()')  # 标题
        href = xml.xpath('//ul[@class="infoListUL mt5"]/li/a/@href')  # 详情链接
        for titles, hrefs in zip(title, href):
            print("====列表页标题====：", titles)
            print("====列表页详情链接====：", hrefs)
            self.parse_two_data(hrefs, titles)  # 调用解析详情页的方法 并传入两个实参（hrefs,titles）

    # 解析详情页的详细文章内容
    def parse_two_data(self, url, c_name):  # c_name为形参 模拟的是要保存的文章标题
        # 先像详情链接发请求
        contents = self.get_data(url)  # 二级页面的网页源码
        # print("二级页面：",contents)
        xml = etree.HTML(contents)
        c = xml.xpath('//div[@class="articleText"]/p/text()')
        # 将list转为str
        article = ''.join(c)
        print("详情页文章内容：",article)
        self.save_data(c_name, article)

    # 保存
    def save_data(self, c_name, qinghua):
        sql = 'insert into demo(name,text) values (%s,%s)'
        # .execute()提交多个要保存的数据时候 要求以列表形式传入
        self.cursor.execute(sql, [c_name, qinghua])  # 执行sql语句
        self.db.commit()  # 提交

    # 统一调用功能方法
    def main(self):
        html_data = self.get_data(self.url)
        module_name, module_href = self.parse_module_data(html_data)  # 调用解析模块内容的方法 得到模块名字和模块链接
        for module_names, module_hrefs in zip(module_name, module_href):
            print("模块名字：", module_names)
            print("模块链接：", module_hrefs)
            self.parse_one_data(module_hrefs)  # 调用解析列表页的方法 并传入实参module_hrefs


if __name__ == '__main__':
    s = Spider()
    s.main()
    # data = s.get_data()
    # # print(data)
    # s.parse_data(data)
