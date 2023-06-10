# '''
# 模块与包
# 模块：一个Python文件   模块放很多代码  功能
# 为什么我的代码要放在不同的文件   方便管理
# 包： 一个文件夹   里面有Python的文件
# python2中，我们规定如果一个文件夹里面有一份文件叫做__init__.py
# 那么我们就叫这个文件夹为一个包
# 在python3没有这个规定，但是我们约定俗称还是会放一个__init__.py的文件
# 包：其实本质上就是一个文件夹
# 模块   将代码分门别类的存放
# 微信  一份文件      分门别类
#     社交相关的功能    更好的管理
#         语音聊天    1份文件才能实现
#         视频聊天
#         文字聊天
#         发短语音
#     和金额相关的功能
# 包的本质也是一个模块
# 使用模块
#     1.  导入模块
# 模块名：Python文件的文件名
# import  模块   as  别名
# 包名：文件夹的名字
# 使用包
#     1. 导入包
# 1. import  包名.模块
# 使用的时候
# 包名.模块都作为前缀
# 导入包就会立即执行 __init__.py 的代码
# 导入包，其实我们真正需要要到的还是包里面的某一份Python文件(里面的某个名字)
# 2. import  包名.模块 as 别名
# 别名。名字
# 3. from 包名 import 模块
# 模块.名字
# 4. from包名 import 模块 as 别名
# 别名.名字
# 5. from 包名.模块  import 名字
# 名字
# 6. from 包名.模块  import 名字 as 别名
# 别名
# 需求：我需要使用到 m2.py 里面的b这个名字
# 导入的问题
# 这个模块需要用到另外一个模块中的名字
# my
#     m1.py     a = 1   需要用到m2.py中的b
#     m2.py     b = 2
# 绝对导入      类似于绝对路径
# from 包名 import 模块
# from 包名.模块名 import 名字
# 好处：可以跨越包  可以导入不同的包的名字
# my          m2.py
# mypackage   m1.py
# 需求：跨过包    我要找不同的包里面的名字
#
# 相对导入   类似于相对路径   了解点   特定的情境下
# 并且只能用于包的内部  不能跨过包
# .        当前目录
# ..       上一级目录
# 缺点：如果写了相对导入，直接运行这份文件会报错
# 所以这种导入的形式，只会是我们在其他的文件导入这个模块的时候去用
# 包
#     1. 是给别人作为一个功能来使用的  而不是直接运行的
#     2. 这个包里面的某份文件需要用到这个包里面的另外一份文件中的名字
#
# 包的使用  我们需要记住的导入包的几个语法
#
#
# 模块/包  本质上都是一堆功能的结合
# 内置的        Python自定给你安装好了    直接导入就可以使用
# 自定义的      自己写的  必须有这个的存在  直接导入可以使用
# 第三方的      需要从网上下载下来的       先下载在导入才能使用
# 如何下载你的第三方模块呢？如何卸载呢？
# 下载  下载一个第三方模块，自动把你安装到python的安装目录里面有个
# Lib\site-packages   这个路径默认就是在sys.path的列表中的
# 所以直接可以找到了
#
# 卸载第三方模块  将你的这个模块文件删除掉
# 在你的cmd终端直接运行
# pip  install  你要下载的第三方模块的名字
# 由于第三方模块默认都是在外网的，受限于网速的原因，经常下载失败，所以我们推荐换源
# pip  install  你要下载的第三方模块的名字 -i  换源网址
# pip  install  你要下载的第三方模块的名字 -i  https://pypi.douban.com/simple
# 例如：
# pip  install  requests -i  https://pypi.douban.com/simple
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
# 还有一种永久换源的方式
# windows：
# 1. 文件管理器文件路径地址栏敲：%APPDATA% 回车，
# 快速进入 C:\Users\电脑用户\AppData\Roaming 文件夹中
# 2. 新建 pip 文件夹并在文件夹中新建 pip.ini 配置文件
# 3. 在pip.ini文件中写如下内容
# [global]
# index-url = http://pypi.douban.com/simple
# [install]
# use-mirrors =true
# mirrors =http://pypi.douban.com/simple/
# trusted-host =pypi.douban.com
# 那么以后，你再下载第三方模块的时候，就可以直接
# pip install 第三方模块
# 卸载第三方模块
# pip uninstall  你要卸载的第三方模块的名字
# 查看你已经安装的所有的第三方模块
# pip list
# 模块与包就讲完了
#
# 加入说你遇到一个问题
# pip  不是内部或外部命令
# 就需要将pip将入环境变量
# 遇到报错：
#     1. 推荐换源安装
#     2. 检查你的命令写错没有
# '''
# # import mypackage.m1
# #
# # print(mypackage.m1.a)
# # import m1
# # print(m1.a)
# # import mypackage.m1 as m
#
# # print(m.a)
# # from mypackage import m1
# # print(m1.a)
# # from mypackage import m1 as m
# # print(m.a)
#
# # 都只能找到模块  不可以直接找到模块里面的名字
# # from mypackage.m1 import a
# #
# # print(a)
# # from mypackage.m1 import a as a1
# #
# # print(a1)
# # import mypackage.my2.m2
# # print(mypackage.my2.m2.b)
# #
# # # from 包名.模块  import 名字 as 别名
# # from mypackage.my2.m2 import b as b1
# #
# # print(b1)
# # from my import m2  # 导入my这个文件夹里面m2.py这个文件
#
"""
import time
time.time()  生成一个从此时此刻到1970.1.1 00:00:00 的秒数
用来计算时间的间隔
time.sleep(数字)   让程序休息几秒钟
"""
# import time
# start = time.time()
# time.sleep(3)
# end = time.time()
# print(end-start)  # 中间间隔了多少秒

'''
随机模块   
import random
random.randint(1, 3)               大于等于1且小于等于3之间的整数
random.choice([1, '23', [4, 5]])   选择任意一个元素
'''
# import random
# # 用的多点
# print(random.randint(1, 3))  # [1,3]    大于等于1且小于等于3之间的整数
# print(random.choice([1, '23', [4, 5]]))  # 1或者23或者[4,5]  选择任意一个元素

# 了解
# print(random.random())  # (0,1)----float    大于0且小于1之间的小数
# print(random.randrange(1, 3))  # [1,3)    大于等于1且小于3之间的整数
# print(random.sample([1, '23', [4, 5]], 2))  # 列表元素任意2个组合
# print(random.uniform(1, 3))  # 大于1小于3的小数，如1.927109612082716

'''
os 模块    
import os
os.mkdir(路径)   
如果没有这个文件夹，就自动帮你创建，如果有，就报错
os.path.exists(路径)
判断一个路径是不是真的存在，结果为True或False
所以，我们通常这么写  来创建一个文件夹
if not os.path.exists(路径):
    os.mkdir(路径)
如果没有这个路径存在，我就创建，如果有，就算了
os.path.join(路径,路径,路径...)  
会得到一个返回值，这个返回值就是这几个路径拼接之后的路径结果  
拼接生成一个路径，以后我们需要拼接得到一个路径的时候，推荐用这个方式

'''
# import os
# os.mkdir('我是一个文件夹')
# os.mkdir('D:\我是一个文件夹')
# print(os.path.exists('D:\我是一个文件夹'))
# if not os.path.exists('我是一个文件夹'):
# #     os.mkdir('我是一个文件夹')
# a = 'd:/'
# b = '我是一个文件夹'
# c = '1.txt'
# 我要得到1.py的绝对路径
# 不同的操作系统 目录之间的分隔符号不一样
# 为了配合不同的操作系统，我们推荐拼接一个文件的路径的时候
# res = os.path.join(a, b, c)
# print(os.path.exists(res))
'''
sys
import sys
sys.path    # 模块的搜索路径，只有在这个列表里面的元素的目录中有的模块才能被导入
sys.path.append(路径)  # 将某个路径加进来，避免模块找不到的问题  
'''

'''
json  模块
json 是一种通用的数据格式

'''
a = {'name': '老杨', 'age': 18}
with open('1.txt', 'w', encoding='utf-8') as f:
    f.write(str(a))
with open('1.txt', 'r', encoding='utf-8') as f:
    data = f.read()
# print(data['name'])  # 报错
# 可不可以成功保存？
# 为什么不行？     文本文件只能保存字符串形式的数据
# 如果强行啊转成一个字符串，取出来用，字符串
# 有很多种编程语言存在
# 保存文件的目录就是为了永久保存数据  这个数据别的语言也可能用到的
# 有的数据格式只是Python特有的
# 如果和其他的编程语言交流的时候，都需要用到一个数据  就可能出现问题
# 解决思路:

# 我  只看懂中文
# A   只看懂日语
# B   只看懂法语
# C   只看懂德语
# 四个人相互交流   1   每一个人都掌握所有的语言   通用的方式
# 选择一种大家都能接受的语言    进行交互了
# json    可以用于跨语言的数据交互
# 1. 将Python换便成为json
# json.dumps(Python的数据)
# 将Python的数据转成json数据，有返回值
# 2. 将json换便成为python
# json.loads(json数据)
# 将json数据转成Python的数据，有返回值

data = {'name': '老杨'}
# print(type(data))
# # res = json.dumps(data)
# res = json.dumps(data,ensure_ascii=False) # 可以展示中文
# print(res)
# res1 = json.loads(res)
# print(res1)
# print(type(res1))
# print(res1['name'])

# 可以将数据保存成json的文件
# 将python的数据转变成json数据，json数据就是字符串的形式
# with open('1.json','w',encoding='utf-8') as f:
#     f.write(json.dumps(data,ensure_ascii=False))
# # 将json的数据取出来，转变成python的数据
# with open('1.json','r',encoding='utf-8') as f:
#     data1 = json.loads(f.read())
# print(data1)
# 简写的形式  直接写进文件中
# json.dump(要写进文件的数据,文件对象,ensure_ascii=False)
# with open('1.json','w',encoding='utf-8') as f:
#     json.dump(data,f,ensure_ascii=False)
# 将json的数据取出来，转变成python的数据
# json.load(文件对象)
# 将json的数据直接转成Python数据
# with open('1.json','r',encoding='utf-8') as f:
#     # data1 = json.loads(f.read())
#     data1 = json.load(f)
# print(data1)
'''
1. json.dumps(Python的数据)   
将Python转成json
2. json.loads(json的数据)
将json转成python
将Python写入文件
3. json.dump(要写进文件的数据,文件对象,ensure_ascii=False)
读取json文件
4. json.load(文件对象)
'''

'''
加密  hash  
hash是一个算法
特点
1.只要传入的内容一样，得到的hash值必然一样=====>要用明文传输密码文件完整性校验
2.不能由hash值返解成内容=======》把密码做成hash值，不应该在网络传输明文密码
3.只要使用的hash算法不变，无论校验的内容有多大，得到的hash值长度是固定的 

123   yyyryryryryyyryyryry  不能破解  
1. 所有的加密都是有算法的   
2. 如果我将世界上所有的字符都加密一下形成更一个表格，对应起来

  



思考:为什么要加密？什么时候需要加密？

假设 我现在开发一个程序    这个程序是和金额相关的

用户A   账户是  123  密码是  123  金额是10000000
123  
123 
这些要不要保存？ 必须永久的保存  文件  这份文件我作为程序员能不能看到？
对密码加密了呢？
注册的时候：
对密码先加密，再讲加密后的密码    保存起来加密后的数据 
123  
登录的时候 
输入密码  对密码加密  和保存起来的加密的密码对比  
对比成功就登录成功
对比的是加密后的数据和保存好的加密的数据的对比
再扩展一点:
    1. 只需要对密码就可以了  账户不需要加密的  
    2. 加密其实也可以破解，信息没有绝对的安全，只有相对的安全
加盐
注册的时候
1, 用户输入密码     123
2. 程序自动给你拼接一个随机字符串   456
3. 将这个拼接起来的字符串加密
对123456加密 ，保存
登录的时候
1. 用户输入密码   123
2. 程序自动给你拼接一个随机字符串   456  盐值  加密
3. 将这个拼接起来的字符串加密
4. 对比

有问题就提问题  

'''
import hashlib

# 使用md5的加密算法进行加密，得到一个返回值
m = hashlib.md5()
# 对某个数据加密
data = '123'
slat = '我是老杨，是个盐值'
pwd = data + slat
# m.update(pwd.encode())  # 必须是二进制
m.update(data.encode())
m.update(slat.encode())
res = m.hexdigest()  # 得到解密后的结果
print(res)
# 9683844afc80cb9f7f6989a88713b04f  将这个保存起来
# 盐值是你自己决定的啊
# 并且每一个账户注册和登录的过程，这个盐值必须是一样的
# 因为换了就登录不成功了
