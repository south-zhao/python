from socket import *


# 发送数据函数
def send_msg(socket):
    # 输入发送的内容
    dest_ip = input("请输入对方的ip：")
    dest_port = int(input("请输入对方的port："))
    dest_data = input("请输入发送的信息：")
    socket.sendto(dest_data.encode('gbk'), (dest_ip, dest_port))


# 接收数据函数
def recv_msg(socket):
    # 接收
    recv_data = socket.recvfrom(1024)
    # 打印
    print(recv_data[0].decode("gbk"))


# 主函数
def main():
    # 1、创建套接字
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    # 2、绑定ip和port
    # udp_socket.bind(("", 3399))
    # 循环收发数据
    while True:
        print("===udp聊天器===")
        print("0：退出")
        print("1：发送")
        print("2：接收")
        op = input("请输入你要的功能：")
        if op == "0":
            break
        elif op == "1":
            send_msg(udp_socket)
        elif op == "2":
            recv_msg(udp_socket)
        else:
            print("输入有误")


if __name__ == '__main__':
    main()
