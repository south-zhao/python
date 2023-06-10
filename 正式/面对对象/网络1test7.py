"""
什么是网络？
    辅助双方或者多方能够连接在一起的工具
使用网络的目的
    为了联通多方然后进行通信，把数据从一方传递给另一方
"""
from socket import *

# s1 = socket(AF_INET, SOCK_DGRAM)
# # s1.bind(('192.168.10.6', 8080))  # 作为接收方
#
# sendaddr = ("192.168.10.6", 9999)
#
# send_data = input("shuru:").encode("gbk")
# s1.sendto(send_data, sendaddr)
# # while True:
# #     re = s1.recvfrom(1024)
# #     print(re[0].decode('gbk'))
#
# s1.close()

s1 = socket(AF_INET, SOCK_DGRAM)

# s1.bind(("", 8899))

sendaddr = ("192.168.10.5", 6789)
while True:

    send_data = input("information:").encode("gbk")
    if send_data == "拜拜":
        break
    s1.sendto(send_data, sendaddr)
    re = s1.recvfrom(1024)
    print(re[0].decode('gbk'))
    if re == "拜拜":
        break

s1.close()















