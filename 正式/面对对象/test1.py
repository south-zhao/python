import random
# name = "lili"
# age = 19
# sex = "男"
#
#
# def talk(a, b, c):
#     print(f"姓名:{a}\n年龄:{b}\n性别:{c}")
#
#
# talk(name, age, sex)
"""
定义类，关键字：class 类名：
类名 一般首字母大写，其余小写
面对对象的核心就是  将程序整合到一起


"""


class Dog:
    # name = "金毛"
    # age = 10
    # gender = "male"

    def __init__(self, food=None):
        self.name = "金毛"
        self.age = 10
        self.gender = "male"
        self.food = food

    def eat(self):
        print(f"{self.name}eat{self.food}")

    def walk(self):
        a = random.randint(1, 20)
        print(f"{self.name}走了{a}米")

    def talk(self):
        print(f"姓名:{self.name}\n"
              f"年龄:{self.age}\n"
              f"性别:{self.gender}\n"
              f"食物:{self.food}\n")


dog = Dog("狗粮")
# dog.name = "yis"
# dog.n = 19
dog.eat()
dog.walk()
dog.talk()
print(dog.name)
# print(dog.__dict__)
# print(Dog.__dict__)




