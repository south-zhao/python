# 面向过程
# 面向对象
# 都是一种程序设计的思维
#
# 面向过程的使用场景？
# 那种一旦实现就很少改动的场景。
#
# 面向对象的使用场景？
# 对象的精髓在于“整合”

# 数据：化妆品
# 功能: 化妆工具
# 对象：盒子
# 任务： 化妆


# 所有的程序都是由“数据”与“功能”组成的，编写程序的本质就是定义出一系列的数据，然后定义出一系列的功能来对数据进行操作。在学习“对象”之前，程序中的数据和功能是分离的
# 程序 = 数据结构 + 算法

# 数据：name age sex
# name = "lisi"
# age = 19
# sex = "female"


# # 功能：
# def tell_info(name, age, sex):
#     print("姓名{}年龄{}性别{}".format(name, age, sex))


# tell_info(name, age, sex)

# 学了“对象”之后，我们可以说：对象是把数据和功能整合到一起的产物。


# 狗（类）     软糖老师的那只金毛犬（对象）

# 现实中先有类还是对象？
# 程序中先有类还是对象？
# 先定义类，再通过类实例化对象

# 定义一个狗类
# class Dog:
#     # 属性
#     name = "旺财"
#     age = 10
#     gender = "male"
#
#     # 方法
#     def eat(self):
#         print("狗吃饭")
#
# # 通过类实例化一个对象
# dog1 = Dog()  # 狗对象1
# dog2 = Dog()  # 狗对象2
#
# # print(dog1)
# # print(dog2)
#
# print(dog1.name)
# print(dog1.age)
#
# print(dog2.name)
# print(dog2.age)


# class Dog:
#     # 属性
#     type = "中华田园犬"
#
#     # 初始化方法 （内置方法）
#     # 谁调用，self就指向谁
#     # 该方法会在实例化的时候，自动调用
#     def __init__(self, name, age):
#         self.name = name  # dog1.name = name
#         self.age = age  # dog1.age = age
#
#     # 方法
#     def eat(self):
#         print("狗吃饭")
#
#
# # 实例化
# dog1 = Dog("小白", 10)  # 狗对象1
# dog2 = Dog("小黑", 20)  # 狗对象2
# # dog1.type = "卷毛"  ## 更改变量值
# print(dog1.name)
# print(dog1.type)
# print(dog2.name)
# print(dog2.type)



