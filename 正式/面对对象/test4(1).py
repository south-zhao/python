"""
取款是功能,而这个功能有很多功能组成:
插卡、密码认证、输入金额、打印账单、取钱
#对使用者来说,只需要知道取款这个功能即可,
其余功能我们都可以隐藏起来,很明显这么做
隔离了复杂度,同时也提升了安全性
"""


# # 动物
# class Animal:
#     def talk(self):
#         pass
#
# class Cat:
#     def talk(self):
#         print("miaomiao")
#
# class Dog:
#     def talk(self):
#         print("wangwang")
#
# class Pig:
#     def talk(self):
#         print("aoaoaoao")


# class A:
#     num = 100
#     __x = 200  # 隐藏属性
#
#     def __foo(self):  # 方法也能隐藏
#         print("run foo")
#
#     def fun(self):
#         print(self.__x)  # 在类的内部可以访问私有属性
#
#     def bar(self):
#         self.__foo()
#
#
# a = A()
#
# print(a._A__x)

# 在类的外部访问属性
# print(a.num)
# print(a.__x)  # __x 是私有的
# a.fun()
# a.__foo()  # __foo 是一个私有方法，外部无法访问
# a.bar()
# print(A.__dict__)


# 枪类
# 属性：类型type  子弹数量count
# 方法：发射子弹shoot  填充子弹add

# 士兵类
# 属性：姓名name   枪gun
# 方法：开火fire

# 火箭炮类
# # 发射 shoot
#
#
# class Gun:
#     def __init__(self, type, count):
#         self.type = type
#         self.count = count   # 子弹数量
#
#     # 发射子弹
#     def shoot(self):
#         if self.count == 0:
#             print("没有子弹了")
#         else:
#             self.count -= 2
#             print("正在开火  哒  哒")
#
#     # 填充子弹
#     def add(self, num):
#         self.count += num
#         print("子弹填充完毕")
#
#
# class Soldier:
#     def __init__(self, name):
#         self.name = name
#         self.gun = None   # 没有枪的状态
#
#     def fire(self):  # 拿枪射击
#         if self.gun == None:
#             print("没有枪")
#         else:
#             self.gun.shoot()
#
#
# # 实例化一把枪
# m41 = Gun("m41", 30)
# # 实例化士兵
# s1 = Soldier("方炜")
# # 给士兵一把枪
# s1.gun = m41  # 组合
# for i in range(20):
#     s1.fire()
#
#


# 私有化就是在类的定义阶段，对属性名或者方法名 进行变形
# 变形的规则：_类名__属性名、_类名__方法名
class ATM:
    # 对于用户来说，没必要关心这些流程
    # 我只取钱，我只要调用一个取款的方法就好了
    def __card(self):
        pass

    def __auth(self):
        pass

    def __input(self):
        pass

    def __print_bill(self):
        pass

    def __take_money(self):
        pass

    def withdraw(self):
        self.__card()
        self.__auth()
        self.__input()
        self.__print_bill()
        self.__take_money()


# 实例化一个对象（取款的事件）
a = ATM()
a.withdraw()
# 对于使用者来说，类内部的流程隐藏了

# class People:
#     def __init__(self, name, age):
#         self.__name = name  # 把传进来的两个数据属性封装起来
#         self.__age = age
#
#     def __str__(self):
#         return "我是{},年龄是{}".format(self.__name, self.__age)
#
#     # 操作姓名和年龄
#     def set_info(self, name, age):
#         # 在这个间接操作的过程中，我们可以做一些判断
#         if not isinstance(name, str):
#             print("姓名必须是字符串")
#             return
#         if not isinstance(age, int):
#             print("年龄必须是整型")
#             return
#         self.__name = name
#         self.__age = age
#
# p1 = People("郑俊杰", 18)
# print(p1)
# # p1.__name = "黄之程"
# # print(p1)
#
# p1.set_info("祝伟", 20)
# print(p1)
