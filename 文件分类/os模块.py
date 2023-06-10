import os
import time

# print(os.getcwd())   # 获取当前路径

# print(os.listdir(os.getcwd()))  # 获取定义目录下的所有文件和文件夹

# os.walk(path)
# 含义 ：传入任意一个path路径，深层次遍历指定路径下的所有子文件夹，返回的是一个由路径、文件夹列表、文件列表组成的元组。我代码中写的方式属于元组拆包；
# 元组拆包：就是将一个元组中的每个值，赋值给不同的变量；
# path = r"C:\Users\黄伟\Desktop\publish\os模块\test_os模块"
# for path,dirs,files in os.walk(os.getcwd()):
#     print(path)
#     print(dirs)
#     print(files)
#     print("\n")
# os.mkdir(path) ## 创建一个文件夹
# os.rmdir(path) ## 删除一个文件夹

# print(os.path.split(os.getcwd()))  # 将路径的最后一个文件或文件夹分离
# print(__file__)  # 得到当前的文件路径

# print(os.path.splitext(os.path.split(__file__)[1])) # 讲文件名与拓展名分离
# os.path.split()得到的是两个值，要用检索的方式得到其中的值

# f = "os模块.py"   # 与os.path.splitext()相似
# print(f.split("."))

# print(os.path.isfile(__file__))  # 判断是不是文件
# print(os.path.isdir(os.getcwd()))  # 判断是不是文件夹

# print(os.path.basename(__file__))  # 返回文件名
# print(os.path.dirname(os.getcwd()))  # 返回文件夹的名字
# os.path.exists()
# os.path.join()

# print(os.path.getsize(__file__))  # 获取大小
# print(os.path.getatime(__file__))   # 上一次访问的时间
# print(os.path.getmtime(__file__))   # 上一次修改的时间
time1 = time.ctime(os.path.getctime(__file__))
print(time1)   # 创建的时间
# print(os.path.abspath(__file__))  # 获得绝对路径





