'''
面向对象  主题    互动的形式
1. 面向对象不是一种技术，只是一种编程思想   跨域语言来存在
高大上 牛逼   为什么要用函数：  简化代码  解耦合  扩展
面向过程
    终极奥义：  过程
    流水线
面向对象
    终极奥义： 对象
    我给总结：整合
程序都有什么：  数据     功能
            变量      函数
面向对象的核心思想就在于  将程序整合在一起
写程序的时候，有一些数据和一些功能是相关联的，功能

'''


# 发现一个问题： 代码混乱
# 学生的数据
# stu_name = '老杨'
# stu_age = 18
# # 学生的功能
# print(f'名字:{stu_name},年龄:{stu_age}')
# stu_name = '老杨1'
# stu_age = 19
#
# # 课程的数据
# course_name = 'python'
# course_score = 100
# # 课程的功能
# print(f'课程名字:{course_name},成绩:{course_score}')
# course_name = '面向对象'
# course_score = 99

# 用函数封装一下
# 学生的数据
# stu_name = '老杨'
# stu_age = 18
# 学生的功能
# def tell_info(obj):
#     print(f'名字:{obj["stu_name"]},年龄:{obj["stu_age"]}')
# def set_info(obj,x,y):
#     # global stu_name  #
#     # global stu_age
#     obj["stu_name"] = x
#     obj["stu_age"] = y
# # 课程的数据
# course_name = 'python'
# course_score = 100
# # 课程的功能
# def tell_course():
#     print(f'课程名字:{course_name},成绩:{course_score}')
# def set_course(x,y):
#     global course_name
#     global course_score
#     course_name = x
#     course_score = y
# # 利用函数简化代码了
# # 有的数据和功能是有关联的，没有整合到一起去
# # 学生的容器 = 学生的数据 + 学生的功能
# # 课程的容器 = 课程的数据 + 课程的功能
# # 有没有办法去实现这个目的？
# # 文件  stu.py   class.py
# # 整合  将数据和功能整合到一起去
# # 思想  语法     文件  一个程序  蒂尼
# # stu_obj = ['老杨',18,tell_info,set_info]
# stu_obj = {
#     'stu_name' : '老杨',
#     'stu_age'  :18,
#     'tell_info':tell_info,
#     'set_info':set_info
# }
#
# stu_obj['tell_info'](stu_obj)
# stu_obj['set_info'](stu_obj,'木易',20)
# stu_obj['tell_info'](stu_obj)
# 学生相关的   课程数据是不能使用的  别人想用就能直接使用
# def tell_info(obj):
#     print(f'名字:{obj["stu_name"]},年龄:{obj["stu_age"]}')
# def set_info(obj,x,y):
#     obj["stu_name"] = x
#     obj["stu_age"] = y
# stu_obj = {
#     'stu_name' : '老杨',
#     'stu_age'  :18,
#     'stu_school':'中职通',
#     'tell_info':tell_info,
#     'set_info':set_info
# }
# stu_obj1 = {
#     'stu_name' : '张三',#
#     'stu_age'  :19,
#     'stu_school':'中职通',
#     'tell_info':tell_info,
#     'set_info':set_info
# }
# 是自己独有的  别人查不到
# stu_obj['tell_info'](stu_obj)
# stu_obj['set_info'](stu_obj,'木易',20)
# stu_obj['tell_info'](stu_obj)
# # 数据是stu_obj1自己独有的
# stu_obj1['tell_info'](stu_obj)
# stu_obj1['set_info'](stu_obj,'木易',20)
# stu_obj1['tell_info'](stu_obj)
# 字典的方式  还是存在一些问题
# 还有没有更好的方式 一点点的优化得来

# 通过字典的方式，不能很好的高度的整合一些数据和功能
# 每个字典中有共有的数据，也有自己独有的数据
# Python这门语言他是如何替我么解决这几个问题的
# 对象    用来保存数据和功能的
# 类     用来保存对象的公用的数据和功能的

# class Student:
#     # print('我是student类')
#
#     stu_school = '中职通'  # 共有的数据搞定了吧
#
#     def tell_info(self):
#         # 我要查看obj这个内存里面的某个数据
#         print(f'名字:{self.stu_name},年龄:{self.stu_age}')
#
#     def set_info(self, x, y):
#         # 我要修改obj这个内存里面的数据
#         self["stu_name"] = x
#         self["stu_age"] = y

# 调用对象以后  开辟一个新的内存空间 自动的执行这个方法
# __dict__  特殊作用的
# ____  只要达到什么条件，就自动的出发这个方法
# def __init__(self, x, y):
#     # 3个参数
#     # 意思值得是
#     # 给obj这个对象的内存空间的里面放x y 这两个数据
#     # 自动的将这个内存空间作为第一个参数自动的传递进来了
#     self.stu_name = x
#     self.stu_age = y
# Student容器 = 数据+功能
# 文字总结：
# 类是对象相似的数据和功能的集合体
# 所以  数据 值得是变量
# 功能值得是  函数
# 那么在类中应该存放的是
# 变量(属性/数据属性)和函数(方法/函数属性)
# 但是在类中其实是可以存放任意的代码的  没必要而已

# 思考一个问题
# 类中有名字  这个名字放哪里呢？  名称空间
# 当你定义了一个类的时候，马上就会做几件事情
# print(Student.__dict__)
# # 表示的是这个类中的名称空间中的东西   是个字典
# # 我要打印这个student类中的stu_school
# print(Student.__dict__['stu_school']) # Python提供的特殊的函数
# print(Student.stu_school) # 简写的形式   本质上分析
# s=Student('老杨',18)  # 内存一旦开辟 马上就可以里面有东西
# s=Student('老杨',18)  # 调用类的时候  自动的执行__init__
# # s.__init__('老杨11',18111)
# print(s.__dict__)
# s = Student()
# s1 = Student()
# Student.tell_info()  # 类来调用本来就应该属于对象的方法
# # python 就不会惯着你了，该传递几个参数，就要传递几个参数
# s.tell_info()
# print(id(Student.set_info))  # 查看类的这个方法
# print(id(s.set_info))  # 查看对象的这个方法
# print(id(s1.set_info))  # 查看对象的这个方法

# python默认自动的帮助你传递进去的对象的内存空间了


# 类里面存放的是公共的数据
# 函数内存地址又不一样了呢？
# 方法/函数  逻辑上面讲  就是给对象使用的    操作对象
# Python自动的将你这个对象当做参数传递进去了

# 类中所有的函数  都是操作自己这个对象的内存空间里面的东西的

# s1=Student()
# 调用类  得到一个空对象  实例化
# 类是一个内存空间  调用类得到一个新的内存空间
# 内存空间和类是有关联的
# s.__init__('老杨',18)  # python做了简化

# print(id(s.stu_name))
# print(id(s1.stu_name))


# print(s.__dict__)   # 是个啥  {}  数据
# print(s1.__dict__)  # 是个啥  {}
# print(id(Student.stu_school))  # 能  '中职通'
# print(id(s.stu_school))   # 能  '中职通'
# print(id(s1.stu_school))  # 能  '中职通'

# 自己独有的  按照内存   共有的类中  类的内存空间中
# 独有的放在那里   自己这个对象自己的内存空间里
# 自己的名称空间中

# 总结：
#     1. 定义类就是开辟一个内存空间，用来存放对象中共有的数据
#     2. 调用类会生成对象，就是产生一个新的内存空间，
#         这个内存空间和类有关联
#     3. 自己这个内存空间里面没有的东西，就去类中找

# 查找顺序
# class A:
#     stu = '老杨'
#
# a = A()  # {}
# b = A() # {}
# A.stu = '我变了'
# a.stu = '我是a'
# print(a.stu)
# print(b.stu)
# print(A.stu)
# 本质
# 酒店房间1   对象    双开门冰箱
# 酒店房间2   对象
# 大厅  类    冰箱
# 封装
# 1. 只要类中的名字前面加上 __ 在对象中就不能直接使用了
# 2. 是真的不可以用吗？   有办法去解决  只是换了个套路而已
# 只是做了一个变形操作而已，这个变形操作
# 只是发生在 创建定义类的时候统一转换的
# 换言之，在其他时候，不会这么转换

# class A:
#     __stu = '老杨'  # _A__stu
#     def __ha(self):
#         print('我是属于你的哈哈')
# # print(A.__dict__)
# a = A()
# b = A()
# a.__age = 18
# print(a.__age)
# print(a._A__stu)
# print(b.stu)
# a.ha()
# b.ha()

# 有什么作用呢？
# 隐藏数据   目的所在     2
class Foo:
    def __init__(self, name):
        self.__name = name

    def set_name(self, name):
        if type(name) is not str:
            print('不能改')
            return
        self.__name = name


f = Foo('老杨')
f.set_name(1000)
# print(f.__name)
# f.name = [1,2,3]  #
# print(f.name)
# 隐藏函数
# 减低复杂程度的   有一些功能不能直接给你使用 你要想使用 必须想怎么
# class ATM:
#     def __card(self): # 插卡
#         print('插卡')
#
#     def __auth(self): # 身份认证
#         print('用户认证')
#
#     def withdraw(self): # 取款功能
#         self.__card()
#         self.__auth()
# obj=ATM()
# obj.withdraw()

# 讲到这里了
# a = [1,2,3]   # 定义一个列表
# a = str(1)  # str  init
# print(a)

# 录播和笔记要不要上传？
# 会不会看回放？
# 百度网盘  链接发在群里
# 辛苦 金嗓子

# 散朝？晚安？    好说好说
# 下节课见  待定
