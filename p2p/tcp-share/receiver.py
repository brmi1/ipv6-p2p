from socket import socket, AF_INET6, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, error
from get_my_ip import get_my_ip

HOST = get_my_ip()
PORT = 1024

sock = socket(AF_INET6, SOCK_STREAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.bind((HOST, PORT))
sock.listen(1)

conn, addr = sock.accept()
recv_filepath = "" # имя получаемого файла
file = open(recv_filepath, "wb")

print("Receiving...")
data = conn.recv(1024)
while data:
    file.write(data)
    data = conn.recv(1024)
file.close()
print("Done Receiving")

conn.close()
sock.close()
