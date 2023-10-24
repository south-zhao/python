"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time :  2023/10/17 9:34
    @Author : south(南风)
    @File : 操作1.py
    Describe:
    -*- coding: utf-8 -*-
"""
import multiprocessing
import os



def fork():
    print('执行子进程, pid={} ppid={}'.format(os.getpid(), os.getppid()))


if __name__ == '__main__':
    t1 = multiprocessing.Process(target=fork)
    if t1.pid is None:
        t1.start()

    else:
        print(os.getpid(), os.getppid())

