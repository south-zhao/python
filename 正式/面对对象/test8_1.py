from socket import *


tcp_serve = socket(AF_INET, SOCK_STREAM)

tcp_serve.bind(("", 6799))

tcp_serve.listen(5)


while True:
    new_socket, client_addr = tcp_serve.accept()
    print(client_addr)
    while True:
        recv_data = new_socket.recv(1024)
        send_data = input("information:").encode('gbk')
        if len(send_data) > 0:
            new_socket.send(send_data)
        else:
            break
    break

new_socket.close()

tcp_serve.close()


