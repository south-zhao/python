class Student:
    __age = 15
    name = "土豆"
    number = 42112111

    def stef(self, name, age, number):
        self.name = name
        self.__age = age
        self.number = number

    def show(self):
        print(f'我叫{self.name},噢~，谁踢我,我今年{self.__age}，我的学号是{self.number}')

    def set(self, name, age, number):
        self.name = name
        self.__age = age
        self.number = number


class Chile(Student):
    pass


b = Student()
b.show()
print(b.number)
b.set("团队之星", 20, 41212803)
b.show()
print(b.number)
print(b.name)
a = Chile()
a.show()
