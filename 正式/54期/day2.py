# 变量：用来记录数据

# 变量名的规范
# 1.只能是英文字母，数字，英文的下划线
# 不能是数字开头
# 不能和python的关键字冲突

import keyword

print(keyword.kwlist)

b = 54689
a = 54689
print(a)
print(type(a))
print(id(a))
print(type(b))
print(id(b))
print(a is b)

