import requests
import re


def get_data(url, headers):
    """
    得到数据
    :param url: 请求的网页地址
    :param headers: 浏览器的头信息
    :return: 返回网页的数据
    """
    res = requests.get(url=url, headers=headers, timeout=3)

    return res.text


# 2，解析数据
def parse_data(content):
    """
    解析数据
    :param content: 网页的数据
    :return: 解析数据，得到想要去提取的信息
    """
    z = '<li\sclass="media\sclearfix".*?<img\sclass="subject-cover".*?src="(.*?)"/>.*?<a\sclass="fleft"' \
        '\shref="(.*?)">(.*?)</a>.*?<p\sclass="subject-abstract\scolor-gray">(.*?)</p>.*?' \
        '<span\sclass="font-small\scolor-red\sfleft">(.*?)</span>.*?' \
        '<a\shref=".*?">(.*?)</a>'  # 解析表达式
    result = re.findall(z, content, re.S)

    return result


# 3，保存
def save_data(data):
    """
    保存文件
    :param data: 初步解析后的数据
    :return:
    """
    with open('douban.txt', 'a', encoding="utf-8") as f:
        for i in data:
            name = i[2]
            author = i[3].strip()
            score = i[4]
            price = i[5]
            price1 = re.findall('[\u4e00-\u9fa5]{3}\s(.*?)元', price, re.S)
            author_data = re.findall('(.*?)\s/\s(.*?)\s/\s(.*?)\s/\s(.*?)\s/\s.*?', author)
            for j in author_data:
                author_name = j[0]
                time = j[1]
                store = j[2]
                origin_price = j[3]
            f.write(name + "   " + author_name + "   " + time + "   " + store + "   " + origin_price + "   " + price1[0]
                    + "   " + score + "\n")


if __name__ == '__main__':
    url = 'https://book.douban.com/latest?subcat=%E5%85%A8%E9%83%A8&p={}'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    content = get_data(url, headers)
    res = parse_data(content)
    save_data(res)
    print("over!")
