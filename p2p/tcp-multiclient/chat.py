from socket import socket, AF_INET6, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, error
from _thread import start_new_thread
from threading import Thread
from get_my_ip import get_my_ip

def server():
    def client_handler(conn, addr):
        while True:
            msg = conn.recv(1024)
            print(addr, " >> ", msg)
        conn.close()

    HOST = get_my_ip()
    PORT = 1024

    sock = socket(AF_INET6, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(5)

    print("Server started!")
    print("Waiting for clients...")

    while True:
        try:
            conn, addr = sock.accept()
            print("Got connection from", addr)
            start_new_thread(client_handler, (conn, addr))
        except error as err:
            print("Client connection closed", addr)
            print(err)

    conn.close()
    sock.close()

def client():
    HOST = "" # адрес получателя
    PORT = 1024

    sock = socket(AF_INET6, SOCK_STREAM)
    sock.connect((HOST, PORT))

    while True:
        data = input(">>> ")
        sock.send(data.encode())

    sock.close()

Thread(target=server).start()
Thread(target=client).start()
