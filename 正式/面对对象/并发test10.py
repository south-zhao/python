"""
进程
    1.进程是计算机中的程序关于某数据集合的一次运行活动，是系统进行资源分配和调度的基本单位，是操作系统结构的基础。
    在早期面向进程设计的计算机结构中，进程是程序的基本执行实体；
    在当代面向进程设计的计算机结构中，进程是线程的容器。
    程序是指令、数据及其组织形式的描述，进程是程序的实体。
    狭义定义：进程是正在运行的程序的实例。
    广义定义：进程是一个具有一定独立功能的程序关于某个数据集合的一次运行活
    动。它是操作系统动态执行的基本单元，在传统的操作系统中，进程既是基本的分
    配单元，也是基本的执行单元。
    注意：同一个程序执行两次，就会在操作系统中出现两个进程，所以我们可以同时
    运行一个软件，分别做不同的事情也不会混乱。
线程
协程
"""
# import time
# from multiprocessing import Process

#
# def func(name):
#     time.sleep(1)
#     print(f"{name}开始进程")
#
#
# if __name__ == '__main__':
#     p = Process(target=func, args=(1, ))
#     p.daemon = True
#     p.start()
#     time.sleep(2)
#     print("主进程")



# import os
# import time
# from multiprocessing import Process
#
#
# def func():
#     for x in range(10):
#         time.sleep(0.5)
#         print("子进程", os.getpid(), os.getppid())   # 获取当前进程的进程ID，获取当前进程主进程的ID
#
#
# if __name__ == '__main__':
#     print("主进程", os.getpid(), os.getppid())
#     # 创建一个进程对象
#     p = Process(target=func)
#     # 开启进程
#     p.start()
#     for i in range(10):
#         time.sleep(0.3)
#         print("*" * i)
#     print("123")
#     p.join()
#     print("456")


# 数据之间不共享
# from multiprocessing import Process
# import time
#
# count = 100
#
#
# def func():
#     global count
#     count -= 2
#     print("子进程", count)
#
#
# if __name__ == '__main__':
#     p = Process(target=func)
#     p.start()
#     time.sleep(5)
#     count -= 1
#     print("主进程", count)

# 多进程
# import os
# from multiprocessing import Process
#
#
# def func(name):
#     print(f"我是学院{name}", os.getpid(), os.getppid())
#
#
# if __name__ == '__main__':
#     name_li = [1, 2, 4, 7]
#     for i in range(4):
#         p = Process(target=func, args=(name_li[i], ))
#         p.start()


from multiprocessing import Process
import time
import os


# 子进程和父进程之间的关系
def func(arg):
    print('子进程%s：' % arg, os.getpid(), os.getppid())


if __name__ == '__main__':
    time.sleep(5)
    print('子进程end')
    for i in range(10):
        Process(target=func, args=(i,)).start()
        print('父进程***********')

# 父进程和子进程的启动是异步的
# 父进程只负责通知操作系统启动子进程
# 接下来的工作由操作系统接手， 父进程继续执行
# 父进程的代码执行完毕之后并不会直接结束程序
# 而是会等待所有的子进程都执行完毕之后才结束
# 父进程要负责回收子进程的资源
