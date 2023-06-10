"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/5/9 23:07
    @Author : south(南风)
    @File : 微分积分.py
    Describe:
    -*- coding: utf-8 -*-
"""
# 微分
import sympy as sy

# x = sy.symbols("x")
# eq = sy.cos(x**2) + x
# y1 = sy.diff(eq, x)  # 一阶导
# y2 = sy.diff(eq, (x, 2))  # 二阶导
# print(y2)

# 对两个变量的导函数
# y = sy.symbols("y")
# eq = x**3 * y + x**2 * y**2
# y1 = sy.diff(eq, (x, 2), y)
# print(y1)
# n = sy.symbols("n")
# y2 = sy.diff(eq, (x, n))
# print(y2)

# 积分
# a, b, x, y = sy.symbols("a b x y")
# eq = sy.Function("f")(x)
#
# y1 = sy.integrate(eq, (x, a, b))
# print(y1)
# print(sy.integrate(x*sy.exp(-x), (x, 0, sy.oo)))

# 微分方程求解
x = sy.symbols("x")
y = sy.Function("y")
# eq = y(x).diff(x, 3) - y(x).diff(x, 2) - x
# con = {y(1): 8, y(x).diff(x).subs(x, 1): 7, y(x).diff(x, 2).subs(x, 2): 4}
# s = sy.dsolve(eq, ics=con)
# print(s)

eq = sy.sqrt(1+y(x).diff(x)*y(x).diff(x)) / 5 - (1 - x) * y(x).diff(x, 2)
con = {y(0): 0, y(x).diff(x).subs(x, 0): 0}
s = sy.dsolve(eq, ics=con)
print(s)

