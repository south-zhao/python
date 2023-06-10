"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/4/13 18:49
    @Author : south(南风)
    @File : spark分析.py
    Describe:
    -*- coding: utf-8 -*-
"""
from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
sc = SparkContext(conf=conf)
print(sc.version)
sc.stop()





