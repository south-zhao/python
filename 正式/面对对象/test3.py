"""
面对对象的三大特征：封装，继承，多态
1.继承：可以通过继承解决类与类之间代码重用的问题
    继承指的是类与类的关系
怎么实现继承
    在Python中新建的类可以继承一个或多个类，被继承的类称为父类，基类或超类
    新建的类成为派生类或子类
2.派生：
    子类可以添加自己的属性和方法
"""

# class Parent1:  # 定义一个父类
#     pass
#
#
# class Parent2:
#     pass
#
#
# class Child1(Parent1):  # 单继承   父类为括号里面的类，本身为子类，继承了父类的全部属性
#     pass
#
#
# class Child2(Parent1, Parent2):  # 多继承
#     pass


# print(Child2.__bases__)  # 查看继承了哪些类


# class Dog(object):  # object python本身的类属性
#     pass
"""

import time
import random


class Hero:
    color = "red"

    def __init__(self, nickname, live_value, camp):
        self.nickname = nickname
        self.live_value = live_value
        self.aggressivity = random.randint(350, 550)
        self.camp = camp
        self.init = self.live_value

    def __str__(self):  # 返回一个字符串，不加的话，返回一个地址
        return f"我是{self.nickname},HP是{self.live_value}"

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


class Garen(Hero):
    color = "blue"


class Riven(Hero):
    color = "purple"


g1 = Garen("大宝剑", 3000, "红")
r1 = Riven("兔女郞", 3210, "蓝")

# print(g1)
# print(g1.color)
"""

import random


class Gun:
    def __init__(self, name, bullet_number, lethality):  # 初始化 枪名，子弹数量，杀伤力
        self.name = name
        self.bullet_number = bullet_number
        self.lethality = lethality

    def fire(self):
        x = random.randint(1, 40)
        print("开火，打机敌方目标")
        for i in range(x):
            self.bullet_number -= 1
            if self.bullet_number <= 0:
                x = 30
                break
        print("发射了{0}发子弹，剩余{1}发子弹，造成{2}伤害".format(x, self.bullet_number, x * self.lethality))

    def add(self):
        add_bullte_number = 30 - self.bullet_number
        self.bullet_number += add_bullte_number
        print("添加了{}发子弹".format(add_bullte_number))


class Solider:
    def __init__(self, name, army_species, gun_name=None, bullet_number=0, lethality=0):
        self.name = name
        self.army_species = army_species
        self.gun = Gun(gun_name, bullet_number, lethality)

    def __str__(self):
        return f"我叫{self.name}，隶属于{self.army_species}, 使用{self.gun.name},剩余{self.gun.bullet_number}子弹，" \
               f"杀伤力为{self.gun.lethality}"


solider = Solider("小赵", "陆军", 'ak47', 30, 50)
solider.gun.fire()
print(solider)
solider.gun.add()
print(solider)
