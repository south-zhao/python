from socket import *

# 1、创建套接字udp
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 2、准备接收方的地址信息
sendaddr = ("192.168.234.1", 3344)

# 3、输入信息
senddata = input("请输入你要发送的内容:").encode("gbk")

# 4、发送
# sendto有两个参数 1.发送的信息（经过编码）2.对方的地址（元组的类型）
udp_socket.sendto(senddata, sendaddr)

# 5、接收对方的数据
recv_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数
# recv_data会接收到两个信息
# 1、对方发送的数据
# 2、对方的地址信息
print(recv_data)
print(recv_data[0].decode("gbk"))


# 关闭套接字
udp_socket.close()

