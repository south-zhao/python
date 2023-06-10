"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/4/29 12:55
    @Author : south(南风)
    @File : 初始SymPy.py
    Describe:
    -*- coding: utf-8 -*-
"""
from sympy import *

# x, y, z = symbols('x y z')  # "x,y,z"  ["x", "y", "z"]

# print(symbols('a:3'))
# print(symbols("c0(1:4)"))
# print(symbols(":d"))
# print(symbols("(x:y)(0:2)"))

# 创建数学公式
# x = symbols('x')  # positive=True 默认化简
#
#
# print(1 / sqrt(x) - sqrt(1 / x))


# print(Rational(1, 3))


# 数学公式
x = symbols("x")
#
eq = 2 * x**3 + 5 * x - 4
print(eq.args)
print(eq.args[2].args)

y = symbols("y")

# print((x + x * y).subs(x, y))
z = symbols("z")

# print((x + y).subs({x: z ** 2, y: sqrt(z)}))





