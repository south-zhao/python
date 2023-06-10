"""
线程：

"""

#
# def func(i):
#     print(f"我是线程{i}")


# if __name__ == '__main__':
#     for i in range(10):
#         t = Thread(target=func, args=(i, ))
#         t.start()


# 为什么轻量级
# if __name__ == '__main__':
#     start = time.time()
#     for i in range(100):
#         t = Thread(target=func, args=(i, ))
#         t.start()
#         t.join()
#     end = time.time()
#     tt = end - start
#
#     start1 = time.time()
#     for x in range(100):
#         p = Process(target=func, args=(x,))
#         p.start()
#         p.join()
#     pp = time.time() - start1
#
#     print(f"线程的时间{tt}")
#     print(f"进程的时间{pp}")


# 数据共享
# num = 100
#
#
# def func():
#     global num
#     num -= 1
#
#
# t_li = []
# for i in range(100):
#     t = Thread(target=func)
#     t.start()
#     t_li.append(t)
# for t in t_li:
#     t.join()
#
# print(num)

# 守护线程
# import time
# from threading import Thread
#
#
# def func1():
#     while True:
#         time.sleep(0.5)
#         print(123)
#
#
# def func2():
#     print('func2, start')
#     time.sleep(3)
#     print('func2 end')
#
#
# t1 = Thread(target=func1)
# t2 = Thread(target=func2)
# # 设置守护线程
# t1.daemon = True
# t1.start()
# t2.start()
# print('主线程的代码结束了')
# 结论：
# 守护线程是在主线程代码结束之后，还等待了子线程结束才结束的
# 主线程结束，就是意味着主进程的结束
# 主线程等待所有的线程结束
# 主线程结束之后，守护线程随着主进程的结束自然结束的










