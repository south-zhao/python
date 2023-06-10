import os

Path = "E:\\python源码"
path = os.getcwd()
file = os.listdir(Path)
file1 = os.listdir(path)
for i in file1:
    x = os.path.splitext(i)
    print(x)
print("------------------------------")
for y in file:
    z = os.path.splitext(y)
    print(z)
