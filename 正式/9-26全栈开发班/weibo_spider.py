'''
分析：
微博移动端接口需要登录才能爬取，采用cookie登录方式
移动端访问接口:https://m.weibo.cn/detail/4813628149072458  (切换成移动端后再浏览器导航栏访问即可)

'''
import requests
from jsonpath import jsonpath
import time
import re
import sys
import random


class WeiBo():
    def __init__(self):
        # 一级评论接口信息
        # https://m.weibo.cn/comments/hotflow?id=4813628149072458&mid=4813628149072458&max_id_type=0
        self.one_url = 'https://m.weibo.cn/comments/hotflow'
        self.one_data = {
            'id': '4813628149072458',  # 博主ID
            'mid': '4813628149072458',  # 博主ID
            'max_id_type': '0',
            'max_id': None  # 翻页参数
        }

        # 二级评论接口信息
        self.two_url = 'https://m.weibo.cn/comments/hotFlowChild'
        self.two_data = {
            'cid': '4813643344774141',  # 来源哪条一级评论的ID
            'max_id': '0',  # 二级的翻页ID
            'max_id_type': '0'
        }
        self.headers = {
            'Referer': 'https://m.weibo.cn/detail/4813628149072458?cid=4816884848924963',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            'cookie': '      '
        }

    # 1，请求并解析一级评论
    def get_one_data(self, url, data):
        response = requests.get(url, headers=self.headers, params=data)
        if response.status_code == 200:
            data_json = response.json()  # 一级接口的网页源码
            one_name = jsonpath(data_json, '$..data[0:20].user.screen_name')
            one_text = jsonpath(data_json, '$..data[0:20].text')
            # 3.1 为了知道二级评论来自哪条一级评论 获取rootid
            cid = jsonpath(data_json, '$..data[0:20].rootid')  # 解析跟评ID cid
            # print(one_text)
            for one_names, one_texts,cids in zip(one_name, one_text,cid):
                one_textss = re.sub('<.*?>', '', one_texts)
                print('-----一级评论-----')
                print(one_names,'--->',one_textss)
                print('=========')
                print('跟评cid:',cids)
                # 有些一级评论下无跟评
                try:
                    # 3.2 切换跟评cid
                    self.two_data['cid'] = cids
                    self.get_two_data(self.two_url, self.two_data)
                except:
                    self.two_data['max_id'] = 0
                    print('====当前 一级评论无跟评，将继续爬取下一一级评论')
            # 2,开始对一级评论进行翻页爬取
            # 2.1 经过分析：翻页id （max_id在上一页接口数据中可以找到）
            max_id = jsonpath(data_json, '$..max_id')[0]
            try:
                time.sleep(random.randint(3, 5))
                # 2.2 切换翻页参数
                self.one_data['max_id'] = max_id
                # 2.3 递归调用实现翻页爬取
                self.get_one_data(self.one_url, self.one_data)
            except:
                print('当前用户一级评论全部爬取完毕~')
                sys.exit('当前用户一级评论全部爬取完毕~')

    # 3，请求二级评论接口并解析二级评论内容
    def get_two_data(self,url,data):
        response = requests.get(url, headers=self.headers, params=data)
        if response.status_code == 200:
            data_json = response.json()  # 二级接口的网页源码
            two_name = jsonpath(data_json,'$..data..screen_name')
            two_text = jsonpath(data_json,'$..data..text')
            for two_names,two_texts in zip(two_name,two_text):
                two_textss = re.sub('<.*?>', '', two_texts)
                print('\t\t','------二级评论----')
                print('\t\t\t',two_names)
                print('\t\t\t',two_textss)
            # 4， 实现二级翻页
            max_ids = jsonpath(data_json,'$..max_id')[0]
            if max_ids ==0:
                print('!!!!!!!二级翻页结束，当前翻页ID为{}！！'.format(max_ids))
                self.two_data['max_id'] = 0
            else:
                time.sleep(random.randint(2,6))
                self.two_data['max_id'] = max_ids
                # 4.1 递归调用自己 实现翻页
                self.get_two_data(self.two_url,self.two_data)

    def main(self):
        self.get_one_data(self.one_url, self.one_data)
        # self.get_two_data(self.two_url,self.two_data)

if __name__ == '__main__':
    s = WeiBo()
    s.main()
