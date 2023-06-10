'''
函数剩余的一些边边角角都讲完
迭代器
循环  for  while  只能保留一个  应该保留哪一个？  ===》 while
for 能做到的，while循环都能搞定  
假设没有了for循环会发生什么事情？

有多个元素的都有什么东西  字符串  列表 元祖 集合 字典 文件 
依赖于索引可以依次得到多个值，但是字典，文件有多个值，但不能用索引
python肯定就提供了一种不需要索引也能够依次得到每一个值的语法
可迭代对象： 迭代是一个重复的过程，但不是单纯的重复，每次重复都是基于上一次的结果出来的
字符串  列表 元祖 集合 字典 文件  都有多个内容元素，都属于可迭代对象
在python中，这些数据都有一个内置的方式  iter()   
iter(字符串/列表/元祖/集合/字典/打开的文件 ) 会得到一个结果
这个结果是一个迭代器
这个迭代器 有两个方法  一个是iter()   一个是next()   
iter(迭代器)    得到自己本身，没改变
next(迭代器)    可以得到下一个值了   迭代器的作用   可以得到下一个值   
没调用一次next就可以得到下一个值，如果没有值了，再调用，就报错了 

不需要for循环也能搞定  下一个值  可以解决这个问题  ===》依次得到每一个值
利用迭代器，不需要for循环我们也能实现这个需求了 

for循环的方式更好的解决了
for x in d:
    pass 
for 循环的原理：
# 1. d.__iter__() 得到一个迭代器对象
# 2. 迭代器对象.__next__() 拿到一个返回值，然后将该返回值赋值给k
# 3. 循环往复步骤2,直到抛出异常，for循环户捕捉异常然后结束循环
  
'''''
# a = '123'
# a  = [1,2,3]
# a = (1,2,3)
# a = {'name':1,'age':2}
# # 我需要依次的获取
# i = 0
# while i<len(a): # len()
#     print(a[i])  # 借助于索引去实现
#     i+=1
# a = '123'
# a = (1,2,3)
# for x in a:
#     print(x)
# a = {'name':1,'age':2}
# b = iter(a)  # 这个b 就是一个迭代器
# while True:  # 为什么会报错？
#     print(next(b))
# # print(iter(b)  is b)  # iter(迭代器)  等于自己本身
# # print(next(b))
# # print(next(b))
# print(next(b))
# print(next(b))
# a.__iter__()
'''
生成器  自定义的迭代器    
在函数中只要出现了一个yield 这个字，那么这个函数就变成了生成器
执行这个函数，函数代码不会执行，而是返回一个生成器（自定义的迭代器）   

迭代器 ：next()   执行这个next() 就可以得到下一个值  for循环结合起来使用的  

生成器  执行一次next()  就开始执行函数里面的代码，然后将yield后面的数据 返回出来
卡在这个地方
下一次在执行next() 就从卡住的地方继续往下执行，执行到下一个yield,  然后将yield后面的数据 返回出来

和return的区别  return  是直接退出了这个函数  
yield 暂停在这里  下一次next()的时候，继续往下执行  
生成器以后什么情况下可能需要用到，好处，作用是什么
'''
# def a():
#     print(1)
#     return 1
#     print(2)
#     return 2
#
# print(a())
# 在函数中  一旦执行到return  就会立即结束，后面的代码不会继续执行了
# def a():
#     print(1)
#     yield 1     # 卡在这里
#     print(2)
#     yield 2


# b = a() # 生成器  就是一个自定义的迭代器
# print(next(b))
# print(next(b))
# print(next(b)) # 报错
# for x in a():
#     print(x)   # print(next(a()))
# def a():
#     with open('1.txt','r',encoding='utf-8') as f:
#         data = f.read()
#     return data
#
# a()    # 假设这份文件有100G   内存中就需要100G    对内存的消耗很大
# def a():  #
#     f = open('1.txt','r',encoding='utf-8')  # 打开文件  10000000000
#     while True:
#         data = f.read(3)  # 每次最多读取24个字符  内存消耗很小
#         if not data:
#             break
#         yield data   # 24个字符
#     f.close()

# b = a()   #
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# for x in a():
#     print(x)

# for  x in '123':
#     print(x)
# # 断点只是方便我们查看运行程序中的步骤  555
# 减少你的内存消耗

'''
列表表达式/推导式   
    就是用来快速的生成一个列表的，看做简化代码的一种方式
生成器表达式
    快速生成一个生成器  将列表推导式的中括号变为小括号
休息5分钟      
'''
# 需求: 将所有的小写字母转成大写字母    形成一个新的列表
# l = ['muyi_nb', 'yimu_nb', 'lao_nb']
# l1 = []
# for x in l:
#     l1.append(x.upper())
# print(l1)
# b = [x.upper() for x in l]
# b = (x.upper() for x in l)
# print(b)
# for x in b:
#     print(x)
# # 取出所有的_nb
# b = [x.split('_')[0] for x in l]
# print(b)
# 字典表达式   快速生成一个字典
# items = [('name','muyi'),('age',18),('sex','man')]
# res = {k:v for k,v in items if k!='sex'}
# a = {}
# for k,v in items:
#     if k != 'sex':
#         a[k] = v
# print(a)
'''
三元表达式    
    简化代码的方式
值1 if 条件 else 值2
如果条件满足，就得到值1，否则得到值2   
'''
# def a(x,y):
#     if x>y:
#         return x
#     return y
# x = 1
# y  = 2
# # print(a(1,2))
# b = x if x>y else y
# print(b)
'''
函数的递归     没有这些    
    函数自己调用了自己   不管是直接或者间接的调用了自己  
    如果一直调用，就变成死循环了      
    如果一直这么循环递归调用自己  会发生什么？ ==》 
    性能大大的降低，Python做了限制的，最多递归1000次  
    要避免死循环  递归函数，要有个退出的条件      
'''
# def b():
#     a()
#
# def a():
#     b()
#
# a()    # 执行函数a
# import sys
# # 查看最多递归多少次
# res = sys.getrecursionlimit()
# print(res)
# # 设置最多递归多少次   虽然可以改，但是不要去改
# sys.getrecursionlimit(1000)
# a = [1,[2,[3,[4,[5,[6]]]]]]
# # 我需要将这里的每一个元素打印出来
# def func(data):
#     for x in data:
#         if type(x) is list:
#             func(x)
#         else:
#             print(x)
#
# func(a)
'''
匿名函数     以前定义函数的方式  
def  函数名(参数):
    函数体
    return 
没有名字的函数  只要用于使用一次就不用了，主要用来配合其他的函数使用的 
lambda 参数1,参数2...:表达式  
结合三个其他的函数来举例子
map   reduce   filter
例子:
需求1：对每一个元素做平方处理，可以map函数   
需求2：求和
'''
a = [1,2,3,4,5]
# res = map(lambda x:x**2,a)
# print(list(res))
# 原理:map(匿名函数,可迭代对象)
# 将可迭代对象的每一个数据  作为参数传递给匿名函数  得到的结果是个迭代器 需要转换成list
# from functools import reduce
# res = reduce(lambda x,y:x+y,a)
# print(res)
# def func(x,y):
#     return x+y
# res = func(1,2)
# print(res)
# # 第一种方式：(匿名函数)(实参)
# res = (lambda x,y:x+y)(1,2)
# print(res)
# # 第二种方式
# a = lambda x,y:x+y
# res = a(1,2)
# print(res)
'''
今天的都属于优化代码的方式   看到了知道即可
生成器  : 一个函数中 出现了yield 关键字 就变成生成器了
        执行这个函数，不会触发函数里面的代码 而是得到一个生成器
        这个生成器执行next() 才会执行这个函数里面的代码 遇到yield就暂停在这里
        将yield后面的数据返回，等待下一次的next()
        好处：节省内存
表达式  
    列表表达式   简化代码的方式  快速得到一个列表
    字典表达式   简化代码的方式  根据得到一个字典 
    生成器表达式   简化代码的方式  根据得到一个生成器 
    三元表达式   简化代码的方式  根据条件快速得到某个值 
匿名函数   简化代码的方式
lambda 参数,参数:表达式  
'''

'''
模块
    什么是模块 
        多个功能的集合
    在python中，一份Python的文件就是一个模块  
对于模块有几个种类
    内置的模块         安装了python 就自带的模块  
    第三方的模块        网上别人写的Python的文件
    自定义的模块        自己写的Python的文件
买了电脑装了操作系统：
    1. 记事本 画图工具   自带的     数量是最少的
    2. 从网下下载的工具  第三方的    一定有数量         
    3. 自定义的        完全取决于你   
为什么要用模块
    1. 分门别类，方便管理
    2. 拿来主义，提升开发效率  
我写了一份Python文件，里面写python的代码，自定义的模块
我写的这个文件是用来实现某个功能的，我觉得这个功能很好，代码很好
我上传到Python的一个网站，下载就好了          第三方模块  
正是由于Python有大量的模块  Python具备大量的功能
web开发方向  爬虫方向      数据分析   
想过为什么是这两个方向   工作岗位  前景  综合考虑  
软件开发的方向很多    大体上   
web开发涉及到的知识点来看的说   比例是最大的  
'''
