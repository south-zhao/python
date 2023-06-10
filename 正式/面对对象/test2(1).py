# 定义一个类
# 定义类就要用python里面造类的方法 class
class Student:  # 类名的首字母推荐大写
    # 类里面应该特征和技能(属性\方法)

    # 类属性（公有属性）
    school = '中职通'

    # 初始化
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def learn(self):
        print('is learning')

# 产生对象
# 实例化一个对象
stu1 = Student("查运卓", "male", 20)

# stu1.height = "1.75"


# print(stu1.__dict__)
# stu2 = Student()
# stu1.name = "郑俊杰"
# print(stu1.name)
# print(stu1.__dict__)
# print(stu1)
# print(stu2)
# print(stu1.height)




# 面向对象（优点）：可扩展性强

# print(Student.__dict__)
# 查
# print(Student.school)  # Student.__dict__["school"]
# 增
# Student.county = "China"
# print(Student.__dict__)
# 删
# del Student.school
# print(Student.school)
# print(Student.__dict__)
# 改
# Student.school = "职通教育"
# # print(Student.__dict__)
# print(stu1.school)

# print(Student.school)
# Student.learn(stu1)


# 练习
# 编写一个学生类，产生一堆学生对象
# 要求：有一个计数器（属性），统计总共实例化了多少个学生对象

class Student:
    # 类属性
    school = '中职通'
    count = 0

    # 初始化
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        Student.count += 1
        print("这是第{}个学生对象,他{}岁".format(self.count, self.age))

    # 类方法
    def learn(self):
        print('is learning')

stu1 = Student("郑俊杰", "male", 10)
stu2 = Student("甄浩", "male", 18)
stu3 = Student("谢佳坤", "male", 20)
stu4 = Student("饭团", "male", 27)




# 模仿lol定义两个英雄类
# 要求：
# 1、英雄有昵称、生命值、攻击力
# 2、实例化出两个英雄对象
# 3、英雄之间可以互殴，被殴打的一方掉血、血量小于0就判断死亡


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

print("兔女郎的生命值", r1.life_value)
print("大宝剑的生命值", g1.life_value)
g1.attack(r1)
r1.attack(g1)
print("兔女郎的生命值", r1.life_value)
print("大宝剑的生命值", g1.life_value)





