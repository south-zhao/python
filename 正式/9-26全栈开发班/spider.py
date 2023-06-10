import requests
import re
import os

url = 'https://book.douban.com/latest?subcat=%E5%85%A8%E9%83%A8&p={}'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

# 开始翻页请求
for i in range(1, 16):
    print('====正在下载第{}页'.format(i))
    page_url = url.format(i)
    print(page_url)

    # 开始请求  获取到网页源码
    r = requests.get(page_url, headers=headers)
    if r.status_code == 200:
        html_data = r.text

        # 2，解析数据
        z = '<li\sclass="media\sclearfix">.*?<img\sclass="subject-cover".*?src="(.*?)"/>' \
            '.*?<a\sclass="fleft"\shref="(.*?)">(.*?)</a>.*?<p\sclass="subject-abstract\scolor-gray">(.*?)</p>'
        result = re.findall(z, html_data, re.S)
        # print(result)
        for data in result:
            img_src = data[0]
            href = data[1]
            name = data[2]
            author = data[3].strip()
            print("图片：", img_src)
            print("详情页面：", href)
            print("书籍：", name)
            print("信息：", author)
            print('===' * 15)

            # 3,数据保存
            # 保存文字信息
            with open('db.txt', 'a', encoding='utf-8') as f:
                f.write(img_src + '\n')
                f.write(href + '\n')
                f.write(name + '\n')
                f.write('\n')

            # 保存图片到文件夹
            # 再次发请求 获取图片的二进制数据
            img_data = requests.get(img_src).content
            # print(img_data)
            # 判断文件夹是否存在
            if not os.path.exists('DATA'):
                os.makedirs('DATA')
            with open('DATA/{}.jpg'.format(name), 'wb') as f:
                f.write(img_data)
