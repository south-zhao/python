import re
from datetime import datetime, timedelta
from dateutil.parser import parse
import jieba.posseg as psg

UTIL_CN_NUM = {
    '零': 0, '一': 1, '二': 2, '两': 2, '三': 3, '四': 4,
    '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '十': 10,
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10, '28': 28, '30': 30, '26': 26,
    '11': 11
}

UTIL_CN_UNIT = {'十': 10, '百': 100, '千': 1000, '万': 10000}


def time_extrace(text):
    d = datetime.today()
    ti = []
    date = d.replace(hour=0, minute=0, second=0)
    keyDate = {'今天': 0, '明天': 1, '后天': 2}
    keyTime = {"上午": 0, "下午": 12}
    for i, j in psg.cut(text):
        if i == "到" or i == "至" or i == "直到":
            ti.append(date)
            date = d.replace(hour=0, minute=0, second=0)
            continue
        else:
            if j == "t":
                if i in keyDate.keys():
                    date = date + timedelta(days=keyDate.get(i, 0))
                elif i in keyTime.keys():
                    date = date + timedelta(hours=keyTime.get(i, 0))
            elif j == "m":
                if i.isdigit():
                    a = text.split(i)[1][0]
                    if a == "点":
                        date = date + timedelta(hours=UTIL_CN_NUM.get(i, 0))
                    elif a == "天":
                        date = date + timedelta(days=UTIL_CN_NUM.get(i, 0))
                    elif a == "月":
                        date = date.replace(month=UTIL_CN_NUM.get(i, 0))
                    else:
                        date = date.replace(day=UTIL_CN_NUM.get(i, 0))
                else:
                    if i[-1] == "点":
                        date = date + timedelta(hours=UTIL_CN_NUM.get(i[0], 0))
                    elif i[-1] == "号":
                        date = date.replace(day=UTIL_CN_NUM.get(i[0], date.day))
                    elif i[-1] == "天":
                        date = date + timedelta(days=UTIL_CN_NUM.get(i[0], 0))
    ti.append(date)
    for da in ti:
        print(da.strftime('%Y年%m月%d日 %H:%M:%S'))


text1 = '我要住到明天下午3点'
print(text1, sep=':')
time_extrace(text1)
text2 = '预定28号的房间'
print(text2, sep=':')
time_extrace(text2)
text3 = '我要从26号下午4点住到11月2号'
print(text3, sep=':')
time_extrace(text3)
text4 = '我要预订今天到30的房间'
print(text4, sep=':')
time_extrace(text4)
text5 = '今天30号呵呵'
print(text5, sep=':')
time_extrace(text5)
