# import socket
from socket import *

# socket方法有两个参数
# 1、adderss family：可以选择AF_INET（用于internet进程间通信）或者AF_UNIX(用于同一台机器进程间通信)
# 实际工作中常用AF_INET
# 2、Type: 套接字类型，可以是SOCK_STREAM（流式套接字，主要用于TCP协议）或者SOCK_DGRAM（数据报套接字，主要用于UDP协议）

# 创建udp套接字
s1 = socket(AF_INET, SOCK_DGRAM)

# 创建tcp套接字
# s2 = socket(AF_INET, SOCK_STREAM)

local_addr = ('', 3344)
s1.bind(local_addr)

recv_data = s1.recvfrom(1024)





