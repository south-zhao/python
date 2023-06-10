# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/11/16 10:46
# @Author : south(南风)
# @File : chart.py
# Describe:
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from pyecharts import options as opts
from pyecharts.charts import Pie, Bar

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 13]
data = [list(z) for z in zip(attr, v1)]
pie = Pie()
pie.add("", data)
pie.set_global_opts(title_opts=opts.TitleOpts(title="售卖表"))
pie.render()
bar = Bar()
bar.add_xaxis(attr)
bar.add_yaxis("", v1)
bar.set_global_opts(title_opts=opts.TitleOpts(title="前十"))
bar.render("render1.html")

