"""
闭包函数：
    闭：内嵌函数  在函数里面定义函数
    包：里面的函数使用了外层函数的名字
闭包函数：
    在函数内部定义一个函数，函数用到了外层函数的名字

闭包函数的意义：
    1.为了装饰器
    2.得到了为函数传递参数的另外一种方式
"""

# def a(c):
#     def b():
#         print(c)
# 闭包函数

"""
装饰器：        器：功能    就是特殊的函数         装饰：添加额外的东西，不影响以前的功能
    1.什么是装饰器？
        一个可以将你原来的函数添加一些功能的函数
    2.为什么有装饰器？
       不更改源代码的基础上，增加一些函数
       
开发中有个规范     开放封闭原则      对功能开放   对修改是封闭的 
不能直接修改原来的代码
"""


# def a(**kwargs):
#     print(kwargs)
#
#
# a(c=2, d=4)


# def a(*args,**kwargs):  #
#     print(args)
#     print(kwargs)
#
#
# s = {'c':1,'b':2}   # 在调用函数的实参前面加一颗星  相当于炸开了 打散了
# a(**s)

#
# def inner(wraper):
#     def outer(*args, **kwargs):
#         print(123)  # 可以接收任意多个，任意形式的参数
#         res = wraper(*args, **kwargs)
#         print(567)  # 这里需要一个动态变化的名字  这个名字哪里来？
#         return res
#     return outer
#
#
# # @inner
# def a():
#     print('正在观看Python学习视频')
#
#
# def b():
#     print('正在观看前端学习视频')
#
#
# # @inner
# def c(d):  # 有参数的函数了
#     print(f'正在观看{d}学习视频')
#     return 666
#
#
# # a = inner(a)
# # a()
# c = inner(c)  # 执行函数inner 得到inner的返回值   绑定给c
# # c('Django')  # inner的返回值()      内存地址
# d = c('Django')      # 执行函数c 得到函数c的返回值   2
# print(d)
