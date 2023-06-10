'''
课堂目标：
     -- 1.区分同步和异步网站
     -- 2.jsonpath解析模块
     -- 3.数据保存为Excel文件
     -- 4.基于IP的反反爬 ，芝麻代理平台：http://jahttp.zhimaruanjian.com/?utm-source=bdtg&utm-keyword=?ocpc1806&bd_vid=5384375158028493684
     -- 5.浏览器更换代理（SwitchyOmega插件的安装与使用）
         安装教程： https://www.cnblogs.com/shyzh/p/11684159.html


1，什么是同步加载？
    同步模式，又称阻塞模式，会阻止浏览器的后续处理，停止了后续的解析，因此停止了后续的文件加载（如图像）,渲染,代码执行。
2，什么是异步加载？
    异步加载又称非阻塞，浏览器在下载执行Js同时，还会继续进行后续页面的处理

3，网页数据返回的方式：
    -- 直接返回网页文本
    -- ajax加载  -- JSON
    -- JavaScript渲染  -- JSON

4，我们去抓取网站，大致分为两种类别：
    -- 直接返回网页文本  -- HTML
    -- 通过接口（数据包）返回数据的  -- JSON

5，同步加载和异步加载的区分
  观察刷新按钮  动了 -- 同步    未动 -- 异步

作业：
爬取腾讯社招   https://careers.tencent.com/search.html
需求：
1.爬取岗位标题和详情链接
2.应用上课中所学的挂IP 切换UA
3.数据保存为Excel


'''
import requests
from jsonpath import jsonpath  # pip install jsonpath
from openpyxl import workbook  # pip install openpyxl
import sys

wb = workbook.Workbook()  # 创建Excel对象
ws = wb.active  # 激活当前表
ws.append(['标题', '链接', '媒体'])


# 请求函数  请求网站获得源码
def get_html():
    try:
        ips = {'http': '122.246.92.98:4213', 'https': '122.246.92.98:4213'}
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
        }
        r = requests.get(url, headers=headers, params=data, proxies=ips)
        if r.status_code == 200:
            json_data = r.json()
            # print(json_data)
            return json_data
    except:
        sys.setrecursionlimit(8)  # 设置递归限制
        return get_html()


# 解析
def parse_data(data_j):
    try:
        # $表示根节点 ..表示跳过中间任意层级
        title = jsonpath(data_j, '$..title')
        url = jsonpath(data_j, '$..url')
        media_name = jsonpath(data_j, '$..media_name')
        for titles, urls, media_names in zip(title, url, media_name):
            print(titles)
            print(urls)
            print(media_names)
            print('=====================')
            save_data(titles, urls, media_names)
    except:
        sys.exit(1)  # 退出程序 0为正常退出  （1-127）为不正常退出


# 保存函数
def save_data(t, u, m):
    my_list = [t, u, m]
    ws.append(my_list)
    wb.save('腾讯.xlsx')


if __name__ == '__main__':
    url = 'https://i.news.qq.com/trpc.qqnews_web.kv_srv.kv_srv_http_proxy/list'
    for i in range(0, 162, 20):
        # print(i)
        # 构建相关参数
        data = {
            'sub_srv_id': '24hours',
            'srv_id': 'pc',
            'offset': '{}'.format(i),
            'limit': '20',
            'strategy': '1',
            'ext': '{"pool":["top"],"is_filter":7,"check_type":true}',
        }
        print('翻页参数为{}'.format(i))
        json_data = get_html()
        # print(json_data)
        parse_data(json_data)
