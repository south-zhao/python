"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time :  2023/11/2 16:46
    @Author : south(南风)
    @File : 操作系统.py
    Describe:
    -*- coding: utf-8 -*-
"""
import time


# 定义一个进程类
class Process:
    def __init__(self, name, arrival, service):
        self.name = name  # 进程名
        self.arrival = arrival  # 到达时间
        self.service = service  # 服务时间
        self.start = 0  # 开始时间
        self.finish = 0  # 完成时间
        self.turnaround = 0  # 周转时间
        self.weighted_turnaround = 0  # 带权周转时间

    def __str__(self):
        return f"{self.name}: arrival={self.arrival}, service={self.service}, start={self.start}, finish={self.finish}, turnaround={self.turnaround}, weighted_turnaround={self.weighted_turnaround}"


# 定义一个函数，根据给定的进程列表和算法类型，进行调度并输出结果
def schedule(processes, algorithm):
    n = len(processes)  # 进程个数
    time = 0  # 当前时刻
    queue = []  # 就绪队列
    running = None  # 正在运行的进程
    finished = []  # 完成的进程
    total_turnaround = 0  # 总周转时间
    total_weighted_turnaround = 0  # 总带权周转时间

    print(f"开始使用{algorithm}算法进行调度")
    while len(finished) < n:  # 当还有未完成的进程时，循环执行以下步骤
        # 将到达的进程加入就绪队列
        if len(queue) + len(finished) != 5:
            for p in processes:
                if p.arrival == time:
                    queue.append(p)
                    print(f"时刻{time}：进程{p.name}到达系统，加入就绪队列")

        # 如果没有正在运行的进程，从就绪队列中选择一个进程运行
        if running is None and queue:
            if algorithm == "FCFS":  # 如果是先来先服务算法，选择就绪队列中最早到达的进程
                running = queue.pop(0)
            elif algorithm == "SJF":  # 如果是短作业优先算法，选择就绪队列中服务时间最短的进程
                running = min(queue, key=lambda p: p.service)
                queue.remove(running)
            else:  # 如果是其他算法，返回错误信息
                return f"错误：不支持的算法类型{algorithm}"
            running.start = time  # 设置运行进程的开始时间
            print(f"时刻{time}：进程{running.name}开始运行")

        # 如果有正在运行的进程，检查是否完成运行
        if running is not None:
            if time - running.start + 1 == running.service:  # 如果运行时间等于服务时间，表示完成运行
                running.finish = time + 1  # 设置运行进程的完成时间
                running.turnaround = running.finish - running.arrival  # 计算运行进程的周转时间
                running.weighted_turnaround = running.turnaround / running.service  # 计算运行进程的带权周转时间
                finished.append(running)  # 将运行进程加入完成列表
                total_turnaround += running.turnaround  # 累加总周转时间
                total_weighted_turnaround += running.weighted_turnaround  # 累加总带权周转时间
                print(f"时刻{time + 1}：进程{running.name}完成运行，加入完成列表")
                running = None  # 清空运行进程

        time += 1  # 更新当前时刻

    print(f"结束使用{algorithm}算法进行调度")
    print(f"所有进程的平均周转时间为：{total_turnaround / n:.2f}")
    print(f"所有进程的平均带权周转时间为：{total_weighted_turnaround / n:.2f}")
    print("每个进程的详细信息如下：")
    for p in finished:
        print(p)


# 测试数据
processes = [
    Process("A", 0, 3),
    Process("B", 2, 6),
    Process("C", 4, 4),
    Process("D", 6, 5),
    Process("E", 8, 2)
]

# 调用函数，分别使用FCFS和SJF算法进行调度
t = time.time()
schedule(processes, "FCFS")
print()
schedule(processes, "SJF")
t1 = time.time()
print(t1-t)
