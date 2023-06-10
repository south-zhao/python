# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/10/6 11:56
# @Author : south(南风)
# @File : wifi.py
# Describe: 
# -*- coding: utf-8 -*-
from pymongo import MongoClient

client = MongoClient()
database = client["demo1"]
collection = database["demo"]
collection.insert_many([
    {"name": "尽快升级到", "age": 30, "address": "房价多少"},
    {"name": "尽快升级", "age": 27, "address": "房价多"},
    {"name": "尽快升", "age": 22, "address": "房"}
])
rows = collection.find({})
for i in rows:
    print(i)

collection.update_many({"name": "尽快升级到"}, {"$set": {"address": "的角色", "work": "教师"}})



