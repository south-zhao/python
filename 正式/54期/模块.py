"""
模块
    内置的       安装了python就已经有的文件
    自定义的     自己写的文件
    第三方的模块    Python指定网站可以下载的别人写的文件
在python中，一份Python的文件，就是一个模块
模块的作用：
    大大的提升我们的效率  避免我们自己写这些代码了
如何使用模块：
必须先导入模块，才能使用这个模块里面的功能
没有存在的模块，导入不了的

当我们导入模块的时候
1. 执行模块.py这份文件里面的代码
2. 会产生一个局部作用域，将模块.py里面的名字都放到这个局部作用域中去
3. 在当前执行的文件中，得到一个名字 模块，这个名字指向的就是模块.py里面的
名字，所以需要使用模块.py里面的名字的时候，需要模块作为前缀


第一种方式：
import 模块名
模块名就是Python文件的名字,不包括后缀
使用的时候需要
模块.名字

可以导入多个模块  推荐这种    可读性更好
import 模块名1
import 模块名2
import ...

也可以用另外一种
import 模块名1,模块名2

还可以起别名
import 模块名1 as 别名
别名.名字

第二种  单独导入模块里的具体的那个功能
from  模块名  import  名字
只能够导入这个模块里面的这个名字，其他的名字用不了
from  模块名  import  名字 as 别名
别名
可以同时导入模块中的多个名字
from  模块名  import  名字1,名字2
from  模块名  import  名字 as 别名,名字 as 别名

容易出现名字被覆盖的问题
并不是说我们就完全不用这种方式  很多情况下也会使用这个方式

有个特殊的形式   不推荐使用
from 模块名  import  *
* 表示所有，等于将模块里面所有的不是以下划线开头的名字都导入了，不需要加前缀
这个方式，我们基本不会使用 ，不能起别名，所以很容易出现重名的情况
下划线开头的名字导入不进去
如果我只希望一些名字被导入 可以在模块中定义一个变量
__all__ = ['名字','名字']
这里的名字必须是字符串，通过这个方式以下划线开头的名字也能导入了
这种方式只针对 from 模块名  import  * 起作用


导入模块，其实只会导入一次，将模块里面的代码导入到内存中了
以后你写导入这个模块的代码，也不会导入了，因为内存中已经有了

666   以后设计的  将公用的数据放在一个单独的文件里面


模块的搜索路径与优先级
1. 模块先查内存     内存中存在这个模块，就不会继续去查找
2. 通过 sys.path这个列表的先后顺序去查看的
这是一个列表，程序会按照从左到右的顺序，去找列表中的每一个元素的
路径里面看有没有这个模块
1. 查找顺序的问题  第一个元素  默认就是你现在这份文件的当前目录
2. 如果我有一个模块，我不想放在Python的安装目录，又不想放在当前目录
就意味着模块找得到吗？   对不对？
肯定找不到啊
要想找到一个模块，那么这个模块必须出现在sys.path这个列表的元素的
文件路径里面
如果我希望一个模块，既不想出现在当前目录，又不想出现在Python安装目录
给 sys.path   这个列表添加元素    不就解决了吗
保存这个模块的文件夹 必须是sys.path列表里面的元素

D:\\Tool\\python\\lib\\site-packages

1. 一个模块要想找到，那么这个模块必须存在于sys.path这个列表的元素
的路径里面
2. 这个sys.path的列表其实只有两类的文件路径
    1. 你现在这个程序的当前目录
    2. 你Python的安装目录
3. 将你这个模块的文件路径添加进sys.path的列表


一份Python文件的两个用途
    1. 直接运行文件
        执行里面的代码
    2. 当做一个模块导入
        里面的代码不是直接运行的，而是作为工具给别人用的

__name__
    直接运行文件，那么这个__name__ 永远等于 __main__
如果一份文件，被当做模块导入了，这个__name__的结果就是模块名

所以我们通常有如下写法
if __name__ == '__main__':
    pass
这个代码表示，如果当前这份文件是当做程序直接运行的，就执行if判断里面的代码
如果这个文件适当做模块运行的，那么if里面的代码不会执行
所以通常，我们写这个代码用来作为主程序的入口

最后一个知识点  规范问题  非必须做的
导入模块的代码  通常写在文件的最上方  书写顺序问题

内置模块
内置模块

第三方模块
第三方模块

自定义模块
自定义模块

包 应该要将包讲完的   周一的时候  提前一点上课  推迟一点下课
下周一常用模块  包讲完
json  hash  os  time  最最常用的  ATM 项目一起去讲了
下周2,3,4  三天的时间   ATM 项目  有点绕 装饰器
模拟从0开始开发一个项目的流程  大量的会涉及到思想  架构这个层面
上身一个境界

走路  掌握单个知识点
ATM 项目  飞   '升华'    不是一个境界
这个周末  所有的基础的知识点  一定要回顾依次
ATM 项目中
    sys.path    模块搜索路径
    函数 的使用   玩来玩去     返回值  参数



''"""
# import m1
# import sys
# sys.path.append(r'D:\54期Python的代码\haha\xix')
# print(sys.path)
# import muyi
# 这里报错的原因是  在sys.path这个列表中
# 找不到任意一个路径下存在muyi.py的文件

# import sys
#
# print(sys.path)
# import file
# 自定义的
# 内置的    我自己没写过这个模块  但是我直接导入可以用
# 这个模块存在  sys.path 这个列表里面的元素的文件路径里面
# 第三方的   第三方模块下载   Python /


# import file
# import time
#
# print(file.a)
# time.sleep(6)  # 让程序休息6秒钟
# import file
# print(file.a)


# print(file.c)
# from file import c
# print(c)
# print(_d)
# import m
# import file,m
# # a = 2
# # print(file.a)  # 打印 file.py 中的a
# # print(a)       # 打印当前这份文件中的a
# file.b()              #
# m.b()
# import lihailewodegenizhendehenbangbangbang  as l
# print(l.a)
# file.b()
# from file import b as b1
# b1()
# print(a)
# from file import a,b
# print(a)
# b()
# from file import b as b1,a as a1
# print(a1)
# b1()
# from file import a
# a = 3
# print(a)  #
# 我就是想用file.py里面的那个a
# 容易出现名字覆盖的现像
# from file import a,b
#
# print(a)
# b()
# print(c)   # 报错，因为没导入
# from file import *
# #
# print(a)
# b()
# print(c)
# print(_d)
# import file  # 777
# import file  # 777
# 循环导入的问题
# import m1
# m1.f1()
# 执行m1.py里面的代码
# 有什么解决方式
# 1. 不太好的方案
# 导入语句放在最后，保证在导入的时候，所有的名字都已经加载了
# 通常我们的导入模块的语句，是写在文件的最开始的
# 2. 不太好的方案
# 导入语句放在函数中，只有在调用函数的时候才会执行代码
# 推荐的方案是什么
# 大家需要用到的数据，单独放在一个文件中，谁需要就谁去要
# print(__name__)
# import m1  # 去执行m.py的代码  print(__name__)

# if __name__ == '__main__':
#     pass
# 编写程序的时候， 写一个这个  用来判断
# 你这份文件是作为模块来给大家使用的还是作为一个程序去执行的
# if 里面的代码  就是你要作为程序执行的代码
# 不会被当做模块的时候 去执行了
# import wordcloud
# import jieba
#
#
# font = 'C:\\Users\\赵鑫杰\\Downloads\\Fzxbsjt_V3.00_XiTongZhiJia\\FZXBSJW.TTF'
# file = open("第十三天.py", encoding='utf-8')
# string = str(file.read())
# file.close()
#
# w = wordcloud.WordCloud(font_path=font, max_words=500, max_font_size=40, background_color='white')
#
# w.generate(" ".join(jieba.lcut(string)))
# w.to_file('e.jpg')

