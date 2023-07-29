from socket import *

# 1、创建套接字udp
udp_socket = socket(AF_INET, SOCK_DGRAM)

sendaddr = ("192.168.234.1", 3344)

while True:
    senddata = input("请输入你要发送的内容:").encode("gbk")
    udp_socket.sendto(senddata, sendaddr)

    # 等待对方发送数据
    recv_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数

    # 打印接收到的信息
    print(recv_data[0].decode("gbk"))



