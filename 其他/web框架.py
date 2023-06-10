# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/10/26 20:32
# @Author : south(南风)
# @File : web框架.py
# Describe: web框架
# -*- coding: utf-8 -*-
import socket

server = socket.socket()

server.bind(('127.0.0.1', 8080))
server.listen(5)

while True:
    conn, addr = server.accept()
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    data = conn.recv(1024).decode('utf-8')
    # print(data)
    cur_path = data.split(' ')[1]
    print(cur_path)
    conn.send(b'hello python')
    if cur_path == '/index/':
        conn.send(b'index')
    else:
        conn.send(b'bai')
    conn.close()



