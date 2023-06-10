"""
# 盖伦类
class Garen:
    # 你用的盖伦 我用的盖伦 是不同的对象
    # 阵营
    camp = "Demacia"   # 属性

    # 初始化
    def __init__(self, nickname, life_value, aggressivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggressivity = aggressivity

    def attack(self, enemy):
        # 攻击目标的生命值减等于我们的攻击力
        enemy.life_value -= self.aggressivity


# 瑞文类
class Riven:
    # 阵营
    camp = "Noxus"  # 属性

    # 初始化
    def __init__(self, nickname, life_value, aggressivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggressivity = aggressivity

    def attack(self, enemy):
        # 攻击目标的生命值减等于我们的攻击力
        enemy.life_value -= self.aggressivity



g1 = Garen("大宝剑", 100, 30)
r1 = Riven("兔女郎", 100, 50)

while True:
    g1.attack(r1)
    print("{}还剩{}血".format(r1.nickname, r1.life_value))
    r1.attack(g1)
    print("{}还剩{}血".format(g1.nickname, g1.life_value))
    if g1.life_value <= 0:
        print("{}血量低于等于0".format(g1.nickname))
        break
    if r1.life_value <= 0:
        print("{}血量低于等于0".format(r1.nickname))
        break
"""


# class Parent1:  # 定义一个父类
#     pass
#
# class Parent2:  # 定义一个父类
#     pass
#
# class Sub1(Parent1):   # 单继承， 父类Parent1  子类Sub1
#     pass
#
# class Sub2(Parent1, Parent2):   # 多继承， 父类Parent1，Parent2  子类Sub2
#     pass
#
# class Dog(object):
#     pass

# def func():
#     print("我是func函数")
#
# func()


class func(object):
    num = 100
    print("我是func类")

    def add(self):
        pass

"""
# 英雄类
class Hero:

    camp = "峡谷"

    # 初始化
    def __init__(self, nickname, life_value, aggressivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggressivity = aggressivity

    def attack(self, enemy):
        # 攻击目标的生命值减等于我们的攻击力
        enemy.life_value -= self.aggressivity

    def __str__(self):  # 描述对象的信息
        # 返回值一定是字符串的形式
        return "我是{}，我的生命值是{}，我的攻击力是{}".format(self.nickname, self.life_value, self.aggressivity)


# 盖伦类
class Garen(Hero):
    # 你用的盖伦 我用的盖伦 是不同的对象
    # 阵营
    camp = "Demacia"   # 属性
    pass


# 瑞文类
class Riven(Hero):
    # 阵营
    camp = "Noxus"  # 属性
    pass


g1 = Garen("大宝剑", 100, 20)
r1 = Riven("兔女郎", 100, 40)

print(g1.camp)
print(r1.camp)

# g1.attack(r1)
# print(r1.life_value)


# print(g1)
# print(r1)



class A:
    pass

class B:
    pass

class C:
    pass

class D(A):
    pass

class E(B):
    pass

class F(C):
    pass

class G(D, E, F):
    pass



"""












