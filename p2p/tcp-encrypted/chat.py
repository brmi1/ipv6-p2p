from socket import socket, AF_INET6, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, error
from rsa import newkeys, encrypt, decrypt
from threading import Thread
from get_my_ip import get_my_ip

(pubKey, privKey) = newkeys(1024)

def server():
    global clientPubKey

    HOST = get_my_ip()
    PORT = 1024

    sock = socket(AF_INET6, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(1)
    conn, addr = sock.accept()
    clientPubKey = conn.recv(1024)

    while True:        
        print("Client connection accepted ", addr)
        while True:
            try:
                data = conn.recv(1024)
                print("<<< ", decrypt(data.decode(), privKey))   
            except error as err:
                print("Client connection closed", addr)
                print(err)
                break

def client():
    HOST = "" # адрес получателя
    PORT = 1024

    sock = socket(AF_INET6, SOCK_STREAM)
    sock.connect((HOST, PORT))
    sock.send(pubKey)

    while True:
        data = input(">>> ")
        if len(data) > 85:
            print("Message it too long")
        else:
            sock.send(encrypt(data.encode(), clientPubKey))

Thread(target=server).start()
Thread(target=client).start()
