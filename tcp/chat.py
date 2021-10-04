from socket import socket, AF_INET6, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, error
from threading import Thread
from get_my_ip import get_my_ip

def server():
    HOST = get_my_ip()
    PORT = 1024

    sock = socket(AF_INET6, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(1)

    while True:
        conn, addr = sock.accept()
        print("Client connection accepted ", addr)
        while True:
            try:
                data = conn.recv(1024)
                print("<<< ", data.decode())   
            except error as err:
                print("Client connection closed", addr)
                print(err)
                break

def client():
    HOST = "" # адрес получателя
    PORT = 1024

    sock = socket(AF_INET6, SOCK_STREAM)
    sock.connect((HOST, PORT))

    while True:
        data = input(">>> ")
        sock.send(data.encode())

Thread(target=server).start()
Thread(target=client).start()
