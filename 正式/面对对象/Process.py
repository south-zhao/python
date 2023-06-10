# -*- coding: utf-8 -*-
# @Time : 2022/8/16 10:48
# @Author : youzi(柚子)
# @File : Process.py
# Describe:
# -*- coding: utf-8 -*-
# 进程的相关内容
# import sys
# import 乘法表


# count = 100
#
#
# def func(i):
#     # time.sleep(0.3)
#     print(f"进程{i}已经开始启动")


# def fun():
#     乘法表.a()


# if __name__ == '__main__':
#     p_li = []
#     for i in range(10):
#         p = Process(target=func, args=(i, ))
#         p.start()
#         p_li.append(p)
#     for p in p_li:
#         p.join()
    # p1 = Process(target=fun)
    # p1.start()
    # print(sys.path)


# 数据在子进程和主进程之间并不共享
# def func1(i):
#     global count
#     # time.sleep(0.3)
#     count -= 1
#     print(f"进程{i}已经开始启动, {count}")
#
#
# if __name__ == '__main__':
#     p = Process(target=func1, args=(1, ))
#     p.start()
#     time.sleep(3)
#     count -= 2
#     print(count)


# def func(args):
#     time.sleep(random.random())
#     print(f"第{args}封信件已经发送完毕")
#
#
# if __name__ == '__main__':
#     for i in range(10):
#         Process(target=func, args=(i, )).start()
#     print("10封信件已经发送完毕")


# def func(args):
#     time.sleep(random.random())
#     print(f"第{args}封信件已经发送完毕")
#
#
# if __name__ == '__main__':
#     p_li = []
#     for i in range(10):
#         p = Process(target=func, args=(i,))
#         p.start()
#         p_li.append(p)
#     for p in p_li:
#         p.join()  # 阻塞 直到p进程的任务结束才解除阻塞,解除阻塞才能继续程序的运行
#     print("10封信件已经发送完毕")


# 守护进程

# def func():
#     print("start")
#     time.sleep(3)
#     print("end")
#
#
# if __name__ == '__main__':
#     p = Process(target=func)
#     p.daemon = True  # 将一个函数设置为守护进程
#     p.start()
#     time.sleep(2)
#     print("zhu end")


# def func1():
#     count = 1
#     while True:
#         time.sleep(0.5)
#         print("*" * count)
#         count += 1
#
#
# def func2():
#     print("start")
#     time.sleep(5)
#     print("end")
#
#
# if __name__ == '__main__':
#     p1 = Process(target=func1)
#     p1.daemon = True
#     p1.start()
#     p2 = Process(target=func2)
#     p2.start()
#     time.sleep(3)
#     print("zhu end")


# def traffic_light(e):
#     print('\033[31m红灯亮\033[0m')
#
#     # flag = False
#     while True:
#         # if flag:
#         if e.is_set():
#             time.sleep(2)
#             e.clear()
#             print('\033[31m红灯亮\033[0m')
#         else:
#             time.sleep(2)
#             e.set()
#             print('\033[32m绿灯亮\033[0m')
#
#
# def car(e, i):
#     if not e.is_set():
#         print('car %s 在等待' % i)
#         e.wait()
#     print('car %s 通过了' % i)
#
#
# if __name__ == '__main__':
#     # 事件
#     e = Event()  # flag属性（默认是fales）
#     # print(e.is_set())
#     # 守护进程（红绿灯循环）
#     p1 = Process(target=traffic_light, args=(e,))
#     p1.daemon = True
#     p1.start()
#     p_lst = []
#     for i in range(20):
#         time.sleep(1)
#         p2 = Process(target=car, args=(e, i))
#         p2.start()
#         p_lst.append(p2)
#     for p in p_lst:
#         p.join()
"""
对象.set()
    作用：设置一个事件的状态为True
对象.clear()
    作用：设置一个事件的状态为False
对象.is_set()
    作用：查看当前事件的状态
对象.wait()
    根据事件的状态，判断是否阻塞
    若状态为True,则不阻塞
    若状态为False，则阻塞
    注意：阻塞的是 对象.wait()后面的内容
"""






