"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/5/4 11:39
    @Author : south(南风)
    @File : 类比建模.py
    Describe: 以地球上的模型为例，推理相关星球的模型
    -*- coding: utf-8 -*-
"""
from sympy import *


v0, g, t, x = symbols("v0 g t x")
a = -g*t**2/2 + v0*t + 0.85 - x
a = a.subs(t, v0/g)
res = solve(a.subs({g: 9.8, x: 1.70}), v0)
print(Float(res[1], 4))


