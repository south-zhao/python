from socket import *


def send_msg(socket):
    senddata = input("输入信息:")
    send_addr = ("192.168.1.10", 6789)
    socket.sendto(senddata.encode('gbk'), send_addr)


def recv_msg(socket):
    re = socket.recvfrom(1024)
    print(re[0].decode('gbk'))


def mian():
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind(("", 8899))
    while True:
        print("*******udp聊天系统*******")
        print("Q:退出")
        print("1:发送")
        print("2:接受")
        op = input("输入选项:").strip()
        if op == 'Q':
            break
        elif op == '1':
            send_msg(udp_socket)
        elif op == '2':
            recv_msg(udp_socket)
        else:
            print("error")


if __name__ == "__main__":
    mian()






