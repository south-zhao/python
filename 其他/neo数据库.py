"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/5/6 9:16
    @Author : south(南风)
    @File : neo数据库.py
    Describe:
    -*- coding: utf-8 -*-
"""
from py2neo import Graph, Node, Relationship


graph = Graph("http://localhost:7474", auth=("neo4j", "20040208"), name="neo4j")

# Person1 = Node("Person", name="a")
#
# graph.merge(Person1, "Person", "name")
# dict1 = {"q": 1, "w": 2}
# Person2 = Node("Person", name="b", **dict1)
#
# graph.merge(Person2, "Person", "name")
# rea = Relationship(Person2, "室友", Person1)
# graph.create(rea)

# graph.delete(Person2)

# a = "match p=(a:movie{name: '肖申克的救赎'})-[c:director]-(b:director) return p"
# b = graph.run(a).to_series()[0]
# print(type(b.relationships[0]).__name__)
# print(b.nodes[1]["name"])
