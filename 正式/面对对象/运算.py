class C(str):
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls, string)


class New(int):
    def __add__(self, other):
        return int.__sub__(self, other)

    def __sub__(self, other):
        return int.__add__(self, other)


a = C("I love Fish")
print(a)
b = New(3)
c = New(5)
print(b - c)
print(c + b)
