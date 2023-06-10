"""
用户交互
    什么叫用户交互
    输入  将信息给计算机     input()   输入时默认为str
    输出  计算机将信息给我    print()
输入的目的：  得到一个数据并使用
"""

# a = input("请输入数字:")
# print(a)
# print(1, 2, 3, sep="+")  # sep表示分隔符

"""
格式化输出

"""
#
# name = "name"
# money = "money"
#
# print("%s is %s" % (name, money))
# print("{0} is {1}".format(name, money))
# print(f"{name} is {money}")

"""
链式赋值
    变量名 = 变量名 = 值
交叉赋值
    a, b = b, a
"""
# a = 10
# b = 8
# b, a = a, b
# print(a, b)

"""
解压赋值
"""

a = [1, 2, 3]
b, c, d = a
print(b, c, d)



