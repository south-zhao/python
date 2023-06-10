# import urllib.request
#
# res = urllib.request.urlopen("https://www.db-book.com/slides-dir/PDF-dir/ch1.pdf")
# book = res.read()
# with open('1.pdf', 'wb') as f:
#     f.write(book)
import requests
import os
import bs4

# import re
# from lxml import etree
#
url = "https://cxy521.com/object.html"
# url = "https://www.db-book.com/slides-dir/PDF-dir/ch1.pdf"
#
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 '
                  'Safari/537.36 '
}
#
response = requests.get(url=url, headers=headers)
# print(response)
#
#
response.encoding = response.apparent_encoding
# # print(response.text)
#

bs = bs4.BeautifulSoup(response.text)
obj = bs.find_all("div", {"class": {"icons"}})
objHtml = []
objImg = []
for s in obj:
    objHtml.append(s.find("img"))

# print(objHtml)
for o in objHtml:
    objImg.append("https://cxy521.com" + o.get("src").strip("."))

# print(objImg)
for img in objImg:
    with open("img/" + os.path.basename(img), 'wb') as f:
        f.write(requests.get(img).content)
    print(os.path.basename(img)+"保存成功")
# print(content)

#
# imgs = etree.HTML(content).xpath('//*[@id="catalog_8"]/section/ul/li/div/div[1]')

# imgs = re.findall('<div class="icons">(.*?)</div>', content)

# print(imgs)
# for i in imgs:
#     print(i.text)
# import bs4
# import requests
# import os
# req = requests.get(r"http://www.umei.cc/bizhitupian/diannaobizhi/1.htm")
# req.encoding="utf-8"
# bs = bs4.BeautifulSoup(req.text)
# obj = bs.find_all("a",{"class":{"TypeBigPics"}})
# objHtml=[]
# objImg=[]
# for s in obj:
#     objHtml.append(s.find("img"))
# for o in objHtml:
#     objImg.append(o.get("src"))
# for img in objImg:
#     with open("D:\\pics22223\\"+os.path.basename(img),'wb') as f:
#         f.write(requests.get(img).content)
#     print(os.path.basename(img)+"保存成功");
