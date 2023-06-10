# -*- coding: utf-8 -*-
# @Time : 2022/8/18 14:15
# @Author : south(南风)
# @File : network.py
# Describe:
# -*- coding: utf-8 -*-
# 对网络编程的总结
from socket import *
# udp
socket1 = socket(AF_INET, SOCK_DGRAM)

send_addr = ("10.139.117.188", 8080)

send_data = input("你要发送的内容:").strip().encode('gbk')

socket1.sendto(send_data, send_addr)

socket1.close()

# tcp服务端


# tcp_serve = socket(AF_INET, SOCK_STREAM)
#
# tcp_serve.bind(("", 8899))
#
# tcp_serve.listen(5)
#
# new_socket, client_addr = tcp_serve.accept()
# print(new_socket, client_addr)
#
# recv_data = new_socket.recv(1024)
# print(recv_data.decode("gbk"))
#
# new_socket.send(b"hello world")
#
# new_socket.close()
#
# tcp_serve.close()

# tcp客户端

# tcp_client = socket(AF_INET, SOCK_STREAM)
#
# tcp_client.connect(("192.168.10.5", 7799))
# send_data = input("information:").encode('gbk')
# if len(send_data) > 0:  # 解码也要同样的
#     tcp_client.send(send_data)
# recv_data = tcp_client.recv(1024)
# print(recv_data.decode("gbk"))
#
# tcp_client.close()

"""
三次握手
    建立连接
四次挥手
    断开连接
三次握手术语：
    SYN
    ACK
    ack
    seq
    FIN
"""
