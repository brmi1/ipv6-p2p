from socket import socket, AF_INET6, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR
from threading import Thread
from time import sleep
from get_my_ip import get_my_ip

sock = socket(AF_INET6, SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.bind(("", 1024))

def server():
    my_ip = get_my_ip()

    while True:
        if sock.recvfrom(1024)[1][0] != my_ip:
            print("\n<<<", sock.recvfrom(1024)[0].decode())
        else:
            print("\n<--", sock.recvfrom(1024)[0].decode())
        sleep(0.01)

def client():
    addr = input("Enter address: ")
    port = 1024

    while True:
        message = input(">>>: ")
        if message != "":
            sock.sendto(message.encode(), (addr, port)) 

Thread(target=server).start()
Thread(target=client).start()
