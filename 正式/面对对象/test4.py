"""
多态：一类事物有多种形态
多态性：向不同的对象发送同一个指令，不同的对象在接受时会产生不同的行为，这就是方法
    每个对象可以用自己的方式去响应这个指令

封装
    第一层：类就是一个袋子，里面可以放属性和方法
    第二层：类中定义私有的属性和方法，只有类的内部可以使用，外部没办法访问
        在Python中用双下划线的方式隐藏属性和方法(私有化就是在类的定义阶段，对属性名或者方法名进行变形)
"""

"""
class Animal:
    def talk(self):
        pass


class Cat:
    def talk(self):
        print("huahua")


class Dog:
    def talk(self):
        print()


class Pig:
    def talk(self):
        print()
"""


class A:
    num = 100
    __x = 200

    def __foo(self):
        print("1")

    def foo(self):
        print("2")
        # a.__foo() 内部可以调用
        # print(a.__x)


a = A()
print(a.num)
a.foo()
# print(a._A__x)
# a._A__foo()
# print(A.__dict__)

# a = 3
# isinstance(a, int)  # 判断变量的类型


