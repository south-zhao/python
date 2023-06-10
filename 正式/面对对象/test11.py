import time
from multiprocessing import Process, Event


# def func(args):
#     time.sleep(random.random())
#     print(f"第{args}封信件已经发送完毕")
#
#
# if __name__ == '__main__':
#     for i in range(10):
#         Process(target=func, args=(i, )).start()
#     print("10封信件已经发送完毕")
#
# def func(args):
#     time.sleep(random.random())
#     print(f"第{args}封信件已经发送完毕")
#
#
# if __name__ == '__main__':
#     # p_li = []
#     for i in range(10):
#         p = Process(target=func, args=(i,))
#         p.start()
#         # p_li.append(p)
#     # for p in p_li:
#         p.join()  # 阻塞 直到p进程的任务结束才解除阻塞
#     print("10封信件已经发送完毕")


# def task():
#     print('%s is task' % os.getpid())
#     time.sleep(random.randrange(1, 3))
#     print('%s is task end' % os.getpid())
#
#
# if __name__ == '__main__':
#     p = Process(target=task)
#     p.start()
#     p.join()
#     print('主')

# 守护进程

# def func():
#     print("start")
#     time.sleep(3)
#     print("end")
#
#
# if __name__ == '__main__':
#     p = Process(target=func)
#     p.daemon = True
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
#     time.sleep(10)
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
#
# def check(person):
#     with open("ticket.txt", 'r', encoding='utf-8') as f:
#         dic = json.load(f)
#     time.sleep(0.5)
#     print(f"{person}查询余票：{dic['ticket']}")
#
#
# def get(person):
#     with open('ticket.txt', 'r', encoding='utf-8') as f:
#         dic = json.load(f)
#     time.sleep(0.2)  # 有延迟的话所有的同时进行就会结果错误   如果没有延迟的话，这个没有错误
#     if dic['ticket'] > 0:
#         print(f"{person}抢到票了")
#         dic['ticket'] -= 1
#         time.sleep(0.2)  # 有延迟的话所有的同时进行就会结果错误   如果没有延迟的话，这个没有错误
#         with open('ticket.txt', 'w', encoding='utf-8') as f1:
#             json.dump(dic, f1, ensure_ascii=False)
#     else:
#         print(f"{person}没抢到票，没票了")
#
#
# if __name__ == '__main__':
#     for i in range(10):
#         # p = Process(target=check, args=(f"person{i}",))
#         # p.start()
#         p1 = Process(target=get, args=(f"person{i}",))
#         p1.start()


# def check(person):
#     with open("ticket.txt", 'r', encoding='utf-8') as f:
#         dic = json.load(f)
#     time.sleep(0.5)
#     print(f"{person}查询余票：{dic['ticket']}")
#
#
# def get(person, lock):
#     lock.acquire()
#     with open('ticket.txt', 'r', encoding='utf-8') as f:
#         dic = json.load(f)
#     time.sleep(0.2)  # 有延迟的话所有的同时进行就会结果错误   如果没有延迟的话，这个没有错误
#     if dic['ticket'] > 0:
#         print(f"{person}抢到票了")
#         dic['ticket'] -= 1
#         time.sleep(0.2)  # 有延迟的话所有的同时进行就会结果错误   如果没有延迟的话，这个没有错误
#         with open('ticket.txt', 'w', encoding='utf-8') as f1:
#             json.dump(dic, f1, ensure_ascii=False)
#     else:
#         print(f"{person}没抢到票，没票了")
#     lock.release()
#
#
# if __name__ == '__main__':
#     lock = Lock()
#     for i in range(10):
#         # p = Process(target=check, args=(f"person{i}",))
#         # p.start()
#         p1 = Process(target=get, args=(f"person{i}", lock))
#         p1.start()


# def ktv(person, sem):
#     # 加锁
#     sem.acquire()
#     print('%s走进ktv' % person)
#     time.sleep(3)
#     print('%s走出ktv' % person)
#     # 释放锁
#     sem.release()
#
#
# if __name__ == '__main__':
#     # 创建一个信号量
#     sem = Semaphore(2)
#     p_li = []
#     for i in range(10):
#         p = Process(target=ktv, args=('person%s' % i, sem))
#         p.start()
#         p_li.append(p)
#     for p in p_li:
#         p.join()


def traffic_light(e):
    print('\033[31m红灯亮\033[0m')

    # flag = False
    while True:
        # if flag:
        if e.is_set():
            time.sleep(2)
            e.clear()
            print('\033[31m红灯亮\033[0m')
        else:
            time.sleep(2)
            e.set()
            print('\033[32m绿灯亮\033[0m')


def car(e, i):
    if not e.is_set():
        print('car %s 在等待' % i)
        e.wait()
    print('car %s 通过了' % i)


if __name__ == '__main__':
    # 事件
    e = Event()  # flag属性（默认是fales）
    # print(e.is_set())
    # 守护进程（红绿灯循环）
    p1 = Process(target=traffic_light, args=(e,))
    p1.daemon = True
    p1.start()
    p_lst = []
    for i in range(20):
        time.sleep(1)
        p2 = Process(target=car, args=(e, i))
        p2.start()
        p_lst.append(p2)
    for p in p_lst:
        p.join()
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


# def re_print(e):
#     print("开始打印")
#     while True:
#         if e.is_set():
#             time.sleep(2)
#             e.clear()
#             print("开始打印")
#         else:
#             time.sleep(2)
#             e.set()
#             print("停止打印")
#
#
# def prt(e, i):
#     if not e.is_set():
#         print(f"{i}")
#         e.wait()
#     print(f"error{i}")
#
#
# if __name__ == '__main__':
#     e = Event()
#
#     p1 = Process(target=re_print, args=(e,))
#     p1.daemon = True
#     p1.start()
#     p_li = []
#     for i in range(10):
#         time.sleep(1)
#         p2 = Process(target=prt, args=(e, i))
#         p2.start()
#         p_li.append(p2)
#     for p in p_li:
#         p.join()













