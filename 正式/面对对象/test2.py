"""
面对对象的相关名词：
    1.类：一个类是对一类拥有相同属性的抽象，蓝图，原型，模板
    2.属性：每个事物的特征（姓名，年龄，身高等等）用程序描述（静态的名词）
        一个类中可以有多个属性
    3.方法：可以做的一些动作行为（吃饭，睡觉，运动等等）用程序描述（运动的动词）
    4.实例（对象）：一个类可以实例化很多对象，每个对象可以有不同的属性（都是人类，但是每一个人和人是不同的）
    5.实例化：把一个类转变成为一个对象的过程



"""


# class Student:
#     # 类属性（公有属性）
#     school = "中职通"
#     count = 0
#     # # 初始化
#     # def __init__(self, name, gender, age):
#     #     self.name = name
#     #     self.gender = gender
#     #     self.age = age
#
#     def __init__(self):
#         Student.count += 1  # 如果使用self.count的话，一直是0，这是实例化对象的值等于类的属性初始化值，计数器的话必须调用类的属性
#         print(self.count)
#
#     def learn(self):
#         print(" is learning")

# 查
# print(Student.school)  # 查看类的属性 print(Student.__dict__)  # print(Student.__dict__['school']) == Student.school
# Student.__dict__返回的是一个字典
# {'__module__': '__main__', 'school': '中职通', 'learn': <function Student.learn at 0x00000254C7D8F6D0>,
# '__dict__': <attribute '__dict__' of 'Student' objects>,
# '__weak ref__': <attribute '__weak ref__' of 'Student' objects>, '__doc__': None}


# 增
# Student.country = "China"  # 增加了属性，也可以增加方法
# print(Student.__dict__)


# 删
# del Student.school  # 这个属性就消失了，不能再次访问


# 改
# Student.school = "大学"  # 此时就更改了类的原本属性 只有通过类来改变属性才会改变原本的值
# 通过类实例化对象改变属性，不改变类的本身属性，只改变这个对象的对应属性


# stu1 = Student()
# print(stu1.__dict__)
# stu1.name = "hong"  # 改
# stu2 = Student()
# print(stu1.school)
# stu1.school = "陕西师范大学"
# print(stu2.school)
# print(stu1.school)
# print(Student.count)


"""
import time
import random


class Hero:
    def __init__(self, nickname, live_value, camp):
        self.nickname = nickname
        self.live_value = live_value
        self.aggressivity = random.randint(350, 550)
        self.camp = camp
        self.init = self.live_value

    def attack(self, enemy):
        enemy.live_value -= self.aggressivity
        print(f"{self.nickname}攻击{enemy.nickname}{self.aggressivity}血量")
        print(f"{self.nickname}HP是{self.live_value}")
        if enemy.live_value < 0:
            enemy.live_value = 0
            print(f"{enemy.nickname}HP是{enemy.live_value}")

    def rescue(self):
        re_live_value = random.randint(70, 90)
        for x in range(4):
            time.sleep(0.1)
            self.live_value += re_live_value
            if self.live_value > self.init:
                self.live_value = self.init
                return


Garen = Hero("大宝剑", 3000, "红")
Riven = Hero("兔女郞", 3210, "蓝")
i = 1
while True:
    print(f"第{i+1}回合")
    Garen.attack(Riven)
    if Riven.live_value <= 0:
        print(f"{Riven.nickname}已经阵亡")
        break
    else:
        Riven.attack(Garen)
        if Garen.live_value <= 0:
            print(f"{Garen.nickname}已经阵亡")
            break
    i += 1
    print("\n")
    print("\n")
    print("游戏结束！")
"""





































































