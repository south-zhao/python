class Student:
    def __init__(self, num, name, age, sex):
        self.num = num
        self.name = name
        self.age = age
        self.sex = sex

    def show(self):
        print("学号:", self.num)
        print("姓名:", self.name)
        print("年龄:", self.age)
        print("性别:", self.sex)

    def change(self, num, name, age, sex):
        self.num = num
        self.name = name
        self.age = age
        self.sex = sex


class Birthday:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def show(self):
        print("年份:", self.year)
        print("月份:", self.month)
        print("日期:", self.day)


class Information:
    def __init__(self, num, name, age, sex, year, month, day):
        self.w = Student(num, name, age, sex)
        self.h = Birthday(year, month, day)

    def show_1(self):
        return self.w.show(), self.h.show()


stu = Student(42112003, "赵鑫杰", 18, "男")
stu.show()
print("\n")
stu.change(42221103, "是否", 38, "女")
stu.show()
print("\n")
bir = Birthday(2004, 4, 23)
bir.show()
print("\n")
a = Information(42112003, "赵鑫杰", 18, "男", 2004, 4, 23)
a.show_1()
