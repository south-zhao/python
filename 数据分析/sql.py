# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/11/12 16:51
# @Author : south(南风)
# @File : sql.py
# Describe:
# -*- coding: utf-8 -*-
import os

import pymysql
from pyecharts import options as opts
from pyecharts.charts import Pie, Bar, Map
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


class Sql:
    def __init__(self):
        self.font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=10)
        self.db = pymysql.connect(user='root', password='root', database='watersystem', charset='utf8')
        self.cursor = self.db.cursor()

    def ten(self):
        sql = "select name,SUM(num) sum from customer_action group by name order by sum DESC limit 10;"
        self.cursor.execute(sql)  # 执行sql语句
        data = self.cursor.fetchall()
        user = []
        num = []
        for i in data:
            user.append(i[0])
            num.append(i[1])
        data = [list(z) for z in zip(user, num)]
        pie = Pie()
        pie.add("", data)
        pie.set_global_opts(title_opts=opts.TitleOpts(title="售卖表"))
        a = pie.render("render1.html")
        src = os.path.split(a)[1]
        return src

    def all_t(self, mon):
        sql = f"select name,SUM(num) sum from customer_action where MONTH(time) = {mon} group by name order by sum DESC limit 10;"
        self.cursor.execute(sql)  # 执行sql语句
        data = self.cursor.fetchall()
        user = []
        num = []
        for i in data:
            user.append(i[0])
            num.append(i[1])
        data = [list(z) for z in zip(user, num)]
        pie = Pie()
        pie.add("", data)
        pie.set_global_opts(title_opts=opts.TitleOpts(title="售卖表"))
        a = pie.render("render_zt.html")
        src = os.path.split(a)[1]
        return src

    def all(self):
        sql = "select name,SUM(num) sum from customer_action group by name order by sum DESC;"
        self.cursor.execute(sql)  # 执行sql语句
        data = self.cursor.fetchall()
        user = []
        num = []
        for i in data:
            user.append(i[0])
            num.append(i[1])
        plt.title("购水表", fontproperties=self.font)
        plt.xlabel("姓名", fontproperties=self.font)
        plt.ylabel("购水数", fontproperties=self.font)
        plt.xticks(np.arange(0, len(user), 1), user, rotation=45, fontproperties=self.font)
        plt.plot(num, marker='P')
        plt.show()

    def water(self, time):
        sql1 = f"select water.type,kS.* from water,(select kind,SUM(num) sum from customer_action where MONTH(time)={time}  group by kind) as kS " \
               "where water.wid = kS.kind order by sum DESC "
        self.cursor.execute(sql1)
        data1 = self.cursor.fetchall()
        com = []
        num1 = []
        for j in data1:
            com.append(j[0])
            num1.append(j[2])
        bar = Bar()
        bar.add_xaxis(com)
        bar.add_yaxis("", num1)
        a = bar.render("render_w.html")
        src = os.path.split(a)[1]
        return src

    def work(self):
        sql = "select name,SUM(num) sum from work_action group by name order by sum DESC;"
        self.cursor.execute(sql)  # 执行sql语句
        data = self.cursor.fetchall()
        user = []
        num = []
        for i in data:
            user.append(i[0])
            num.append(i[1])
        bar = Bar()
        bar.add_xaxis(user)
        bar.add_yaxis("", num)
        a = bar.render("render_wo.html")
        src = os.path.split(a)[1]
        return src

    def yue(self):
        sql = "select kind,SUM(num) sum,MONTH(time) from customer_action group by kind,MONTH(time);"
        self.cursor.execute(sql)  # 执行sql语句
        data = self.cursor.fetchall()
        total = [30, 50, 10, 20, 10]
        mon = [1, 2, 3, 4, 5]
        total1 = [40, 20, 0, 20, 30]
        bar = Bar()
        bar.add_xaxis(mon)
        bar.add_yaxis("10月", total)
        bar.add_yaxis("11月", total1)
        a = bar.render("render-Yue.html")
        src = os.path.split(a)[1]
        return src

    def map(self):
        map = Map()
        provinces = ["广东", "北京", "上海", "辽宁", "湖南", "四川", "西藏"]
        value = [300, 100, 2000, 800, 10000, 400, 5000]
        # china可改为world或各省市名称
        map.add("", [list(i) for i in zip(provinces, value)], "china")

        # 表名称；max_为最大值，超过此值都为最大值颜色;split_number,is_piecewise可以将颜色分块显示
        map.set_global_opts(title_opts=opts.TitleOpts(title="title"),
                            visualmap_opts=opts.VisualMapOpts(max_=5000, split_number=8, is_piecewise=True))

        map.render('map.html')

    def run(self):
        # self.ten()  # 用户前十名
        # self.all()  # 所有用户
        self.water(11)  # 水销量
        # self.work()
        # self.yue()
        # self.all_t(10)
        # self.map()
        self.db.commit()
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    sql1 = Sql()
    sql1.run()





