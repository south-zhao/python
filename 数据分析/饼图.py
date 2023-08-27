"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/7/14 20:05
    @Author : south(南风)
    @File : 饼图.py
    Describe:
    -*- coding: utf-8 -*-
"""
import matplotlib.pyplot as plt

labels = ["Chrome", "Internet Explorer", "Firefox", "Edge", "Safari", "Sogou Explorer", "Opera", "Others"]
marketshare = [61.64, 11.98, 11.02, 4.23, 3.79, 1.63, 1.52, 4.19]

explode = (0, 0, 0.5, 0, 0.8, 0, 0, 0)

plt.pie(marketshare, explode=explode, labels=labels, autopct="%.1f%%", shadow=True, startangle=45)
plt.axis("equal")
plt.title("Web Browser Marketshare - 2018")
plt.show()

