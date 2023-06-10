import requests
from lxml import etree
from Chaojiying_Python.chaojiying_Python.chaojiying import Chaojiying_Client


# https://www.chaojiying.com/  超级鹰平台
class Spider():
    def __init__(self):
        # 首页接口
        self.index_url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

        # 用户登录接口
        self.url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
        self.data = {
            '__VIEWSTATE': 'aCnQyT3PaQqur1z0WmfLOCq0FvSxdh7ZHMgYiAHdXZr4NqI2UgkwNY5rb/QZJbh3+1Mw6L1qBDnuZ4eoPgziXWvk7+8/kHtElp5K07+A6i0wR46x+OHhBWi+m6Pmb+KhMeLAU4CcgGu/iggvD5U/qmxD9WY=',
            '__VIEWSTATEGENERATOR': 'C93BE1AE',
            'from': 'http://so.gushiwen.cn/user/collect.aspx',
            'email': '1376568275@qq.com',
            'pwd': 'qweqwe',
            'code': '2544',  # 验证码
            'denglu': '登录',
        }
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
        }
        self.s = requests.session()  # 实例化对象

    # 像首页发请求 解析出验证码图片链接
    def post_index(self):
        # r = requests.get(self.index_url,headers = self.headers)
        r = self.s.get(self.index_url, headers=self.headers)
        html_data = r.text
        xml = etree.HTML(html_data)
        # https://so.gushiwen.cn/RandCode.ashx
        img_src = 'https://so.gushiwen.cn' + xml.xpath('//img[@id="imgCode"]/@src')[0]
        print(img_src)

        # 将图片保存到本地
        img_data = self.s.get(img_src, headers=self.headers).content
        with open('code.png', 'wb')as f:
            f.write(img_data)

        chaojiying = Chaojiying_Client('Ladmin0226', 'admin123.', '939881')  # 用户中心>>软件ID 生成一个替换 96001
        im = open('code.png', 'rb').read()
        result = chaojiying.PostPic(im, 1004)
        # print(result)
        return result

    # 像用户登录解决发请求 实现登录
    def post_user(self):
        result = self.post_index()
        print(result)
        self.data['code'] = result
        r = self.s.post(self.url, headers=self.headers, data=self.data)
        print(r.status_code)
        print(r.text)


if __name__ == '__main__':
    a = Spider()
    a.post_user()
    # a.post_index()
