# -*- coding: utf-8 -*-
# @Author : 阿尔法
# @File : 接单流程实战.py
# @Software: PyCharm
# time : 2022/10/12
"""
课题：
    接单流程实战

# 我们合作的接单平台，分成比例是28分成：
    2成派单平台的服务费
    我们拿8成
# 接单平台：结算周期：通过你在接单平台注册的派单小程序的手机号，打款到支付宝
# 不要把：用户名字，手机号码，密码弄错了
# 手机便签记下来
# 如果写错了，忘记了，找客服修改
# 支付宝：根据你注册的手机号码，找到你的支付宝账户，打款到支付宝
# 如果不是填写的上述注册信息，关于单子接单的打款咨询客服

网络上面：接单网站：不要去相信，弄不好还需要你交保证金(割韭菜)----不要相信
    在qq上面，按群名称搜索接单/python/爬虫----你在进群之后---先潜水(验证这是不是真的接单群)
    有很多接单平台是通过qq来管理的，那么通过这种方式你能找到几个接单群
    37,46，普遍是37分成

打开淘宝、京东，拼多多等电商平台：
    搜索python爬虫，python代写，想接什么类型的单子就搜索什么
    在商品列表页，观察月销量，从而判断出该店铺的单量有多少
    找到销量比较高的店铺---找客服---还需不需要技术

还需不需要技术，我会的很多，会爬虫，web，数据库，数据分析制图，制表
把你做过的项目截图，发给对方

进10个左右的接单群基本上够了----每天都有单子接

接单流程：
    在接单群里面，首先确定你可以做哪一个单子
    把你能够确定做的单子的id，发给客服，如果单子还在的话
    客服会把客户，你，拉进一个群----聊天群
    在群里面，开始沟通单子的细节(确定价格，开发周期，售后等等)
    然后让客户下单
    在客户下单之后，你就能在派单小程序看到你自己接的单子了

接单之后，客户下单了，还可以退单吗？
    可以的，但是尽量少出现
    一定要确定这个单子你能不能做，在聊天群中，你就要了解清楚

单子做不出来，说明技术不行，会影响后期客服给你继续派单
实在做不出来，我们接单交流群里面有上百人
你可以求助群里面的同学

关于报价：
    先了解需求，全部弄清楚之后，在报价
    要代码还是要数据
    如果要代码，是要py文件还是要可执行程序的exe
    可执行程序可以多报价200~300
    如果对方需要的是py文件，因为客户多数是不懂编程的，对方要py文件也就意味着你需要在对方的电脑上面搭建python环境

    .exe可执行程序：在windows操作系统中，直接双击就可以运行爬虫程序了
    把python代码编程.exe可执行程序：需要借助pyinstaller封装

    https://xueqiu.com/P/SP1000000  到  https://xueqiu.com/P/SP1050000
    数据量至少5w条

数据方面：20w条数据
    1.在用户详情页采集(12个字段)：数据是同步加载---没有加密
        用户ID、用户名、性别、是否认证、认证说明、发帖数、关注股票数、创建组合数、原发布数、问答数、关注数、粉丝数
    2.从用户界面进入到关注界面(3个字段)：数据是异步加载---没有加密
        关注者的粉丝数总量、关注数总量、帖子数总量
    3.从用户界面进入粉丝界面(3个字段)：数据是异步加载---没有加密
        粉丝的粉丝数总量、关注数总量、帖子数总量
    4.5.从用户页面进入组合页面 找到未关停组合(9个字段)：数据是同步加载---没有加密
        组合ID、组合股票数、组合总收益率、组合日收益率、组合月收益率、组合净值、组合关注人数、组合创建日期、最新调仓日期

关于报价：
    数据的采集的难易程度(有些数据是有加密的，加密的数据报价要高一点)
    先去判断数据的加密方式

关于报价的沟通：
    积累老客户

数据的存储方式：
"""
from requests_html import HTMLSession
# 创建请求对象
session = HTMLSession()
from lxml import etree
import re, json


cookie_str = """s=bp1229zzip; cookiesu=581665467162099; device_id=8959f7d3a8a0975bea00c76494df585a; remember=1; xq_a_token=56a322a6c306282464699a002a020e572f470d53; xqat=56a322a6c306282464699a002a020e572f470d53; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjc2Mzk0NzU0NTIsImlzcyI6InVjIiwiZXhwIjoxNjY4MDU5NTAwLCJjdG0iOjE2NjU0Njc1MDA2NDEsImNpZCI6ImQ5ZDBuNEFadXAifQ.HcZtgwMRBR623ik7-wr-cj3lPvcft5RP-saBpcAMrYSuE30-jSY3Wkx-mMnO8I3VoXXLYGK1h1o4Q75bklU2_S7b7SIjOLz-BvD-zI6CJHF6RMh0PpSbTWqlTxcEgQr10CG6JcDnVydeiUbhVUQoecxyITaE0gn6tqktrViUocjR4b9EuC68Ihg1tILCm2vIf7MpYN1GUV-VNy605wA9p2wfYCwIB7oYgNTlLxS5W6HlDWV6gc4xxB9iTHX9kkyLqp69lXf2j-mywABOAkbNZ0DKOD3DDTI3cT6Ci2L54mMg0dzDxI0-mCX8f70VFaQBuHwzhpg0o2eFEJsRXB_C7A; xq_r_token=b38021e15138c70474f88cce4e4b6e8ec8be8dc5; xq_is_login=1; u=7639475452; bid=5c0d84cbcf1f097beab2f6615a918a08_l93scxvh; __utmz=1.1665467518.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_1db88642e346389874251b5a1eded6e3=1665467162,1665578300; __utma=1.1668548215.1665467518.1665467518.1665578300.2; __utmc=1; acw_tc=2760826616655803264376271e6a9ef0476adf5f3f1f86436918bc9f197c9b; __utmt=1; __utmb=1.8.10.1665578300; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1665580692"""
class Spider(object):

    def __init__(self):
        # 请求的地址
        """
        https://xueqiu.com/P/SP1000000  到  https://xueqiu.com/P/SP1050000
        """
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Host': 'xueqiu.com',
            'Pragma': 'no-cache',
            'Cookie': cookie_str,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }

    def parse_start_url(self):
        """
        解析请求的地址
        """
        for num in range(1000000, 1050001):
            # 请求地址的拼接
            url = 'https://xueqiu.com/P/SP' + str(num)
            response = session.get(url, headers=self.headers).html
            user_url = 'https://xueqiu.com' + ''.join(response.xpath('//*[@id="cube-info"]/div[2]/div/a/@href'))
            user_name = ''.join(response.xpath('//*[@id="cube-info"]/div[2]/div/a/div/div/text()'))
            self.parse_one_response_data(user_url, user_name)
            break

    def parse_one_response_data(self, user_url, user_name):
        """
        解析第一个需求：
        用户ID、用户名、性别、是否认证、认证说明、发帖数、关注股票数、创建组合数、原发布数、问答数、关注数、粉丝数
        """
        print(f"开始处理第一个采集数据的需求")
        # 用户ID
        user_id = user_url[19:]
        # 发送对用户详情页的请求，获取响应
        # response = session.get(user_url, headers=self.headers).html
        # print(response.html.replace(' ', ''))
        # resp = etree.HTML(response.html)
        # # 性别
        # sex = ''.join(response.xpath('//*[@id="app"]/div[2]/div/div[1]/div[1]/div/@class'))[-1]
        # if sex == 'm':
        #     sex = '男'
        # elif sex == 'f':
        #     sex = '女'
        # else:
        #     sex = '保密'
        # snowman = re.findall('SNOWMAN_TARGET=(.*?);', response.html.replace(' ', ''))[0]
        # json_data = json.loads(snowman)
        # print(json_data)
        # # 是否认证
        # verified_infos = json_data['verified_infos']
        # if verified_infos:
        #     verified_yn = True
        #     str1 = ''
        #     for i in verified_infos:
        #         str1 += i['verified_desc'] + '/'
        # else:
        #     # 认证状态  None没有认证
        #     verified_yn = False
        #     str1 = False
        # # 发帖数
        # status_count = json_data['status_count']
        # # 股票数
        # gp_count = ''.join(resp.xpath('//span[@class="stock"]/text()'))
        # # 创建组合数
        # cube_count = json_data['cube_count']
        # # 提取原发布数和问答
        # yfb_count, total = self.parse_yfb_data(user_id)
        # # 获取关注
        # gz_count = json_data['friends_count']
        # # 粉丝数量
        # fs_count = json_data['followers_count']
        # item = [user_id, user_name, sex, verified_yn, str1, status_count, gp_count, cube_count, yfb_count, total, gz_count, fs_count]
        # print(item)

        self.parse_two_response_data(user_id)

    def parse_yfb_data(self, user_id):
        """
        处理源发布
        https://xueqiu.com/v4/statuses/user_timeline.json?page=1&user_id=3340940262&type=0&_=1665583207858
        """
        url = f"https://xueqiu.com/v4/statuses/user_timeline.json?page=1&user_id={user_id}&type=0"
        resp_json = session.get(url, headers=self.headers).json()
        maxPage = resp_json['total']
        ques_url = f"https://xueqiu.com/v4/statuses/user_timeline.json?page=1&user_id={user_id}&type=4"
        resp_json1 = session.get(ques_url, headers=self.headers).json()
        total = resp_json1['total']
        return maxPage, total

    def parse_two_response_data(self, user_id):
        """
        提取第二个数据的需求
        https://xueqiu.com/friendships/groups/members.json?uid=3340940262&page=1&gid=0&_=1665584013832
        """
        url = f"https://xueqiu.com/friendships/groups/members.json?uid={user_id}&page=1&gid=0"
        response = session.get(url, headers=self.headers).json()
        # 提取循环范围
        maxPage = response['maxPage']
        list_data = []
        for i in range(1, maxPage+1):
            url = f"https://xueqiu.com/friendships/groups/members.json?uid={user_id}&page={i}&gid=0"
            response_list = session.get(url, headers=self.headers).json()['users']
            for response in response_list:
                # 粉丝的名称
                domain = response['domain']
                # 粉丝的数量
                followers_count = response['followers_count']
                # 关注数量
                friends_count = response['friends_count']
                # 帖子数量
                status_count = response['status_count']
                item_data = [domain, followers_count, friends_count, status_count]
                list_data.append(item_data)
        print(list_data)


if __name__ == '__main__':
    s = Spider()
    s.parse_start_url()




