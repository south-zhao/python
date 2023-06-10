"""
property的使用：一种特殊的属性，访问的时候会执行一段功能（函数），会有返回值

"""

"""
class People(object):
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    @property  # 将一个类的函数定义成为特性，对象去使用的时候直接使用obj.name
    # 目的是根本无法查觉自己的name是执行一个函数，遵循统一访问的原则
    def bmi(self):
        return self.weight / (self.height ** 2)


p = People('xiaozhao', 54, 1.55)
print(p.bmi)
"""
"""
绑定方法与非绑定方法：
1.绑定方法：绑定给谁，就由谁来调用，谁来调用就当做一个参数自动传入
    对象的绑定方法（默认）
    类中默认绑定为对象使用
    
"""
"""

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def tall_info(cls):
        print('1223')


obj = People('精神小伙', 18)
People.tall_info()
"""
"""
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def tall_info():
        print('1223')


obj = People('精神小伙', 18)
obj.tall_info()
People.tall_info()
"""
import hashlib
import time
from pathlib import Path
import json


class Account:
    def __init__(self):
        while True:
            self.name, self.age, self.password, self.height, self.weight = self.information()
            self.password = self.hash_password(self.password)
            self.id = self.create_id()

            # Path(Path.cwd() / f"{self.name}.txt").write_text(str(new_information))
            # print(Path(Path.cwd() / f"{self.name}.txt").read_text())
            path = Path.cwd()/'user_information'/f'{self.name}.txt'
            if path.exists():
                print("已经存在")
                break
            new_information = {
                "name": self.name,
                "age": self.age,
                "password": self.password,
                "id": self.id,
                "height": self.height,
                "weight": self.weight
            }
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(new_information, f, ensure_ascii=False)
            with open(path, 'r', encoding='utf-8') as f:
                print(json.load(f))
            print("创建成功!")

    @staticmethod
    def information():
        print("姓名:")
        name = input().strip()
        print('年龄:')
        age = input().strip()
        print('身高:')
        height = input().strip()
        print('体重:')
        weight = input().strip()
        while True:
            print('密码:')
            password = input().strip()
            print("请再次输入密码:")
            re_password = input().strip()
            if password == re_password:
                return name, age, password, height, weight
            print("两次密码不同")

    @staticmethod
    def create_id():
        m = hashlib.md5(str(time.time()).encode('utf-8'))
        return m.hexdigest()

    @property
    def bmi(self):
        return float(self.weight) / (float(self.height) ** 2)

    def bmi_condition(self):
        if self.bmi <= 18.5:
            print(f"你的BMI为{self.bmi}，BMI数值过轻")
        elif 18.5 < self.bmi <= 23.9:
            print(f"你的BMI为{self.bmi}，BMI数值正常")
        elif 24 < self.bmi <= 27:
            print(f"你的BMI为{self.bmi}，BMI数值过重")
        elif 27 < self.bmi <= 32:
            print(f"你的BMI为{self.bmi}，BMI数值肥胖")
        else:
            print(f"你的BMI为{self.bmi}，BMI数值非常肥胖")

    @staticmethod
    def hash_password(password):
        obj = hashlib.md5()
        salt = "小赵"
        obj.update(password.encode('utf-8'))
        obj.update(salt.encode('utf-8'))
        return obj.hexdigest()


a = Account()
# print(a.bmi)
a.bmi_condition()






