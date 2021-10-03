from socket import socket, AF_INET6, SOCK_STREAM

HOST = "" # ip получателя
PORT = 1024

sock = socket(AF_INET6, SOCK_STREAM)

sock.connect((HOST, PORT))
send_filepath = "" # имя отправляемого файла
file = open(send_filepath, "rb")

print("Sending...")
data = file.read(1024)
while data:
    sock.send(data)
    data = file.read(1024)
file.close()
print("Done Sending")

sock.close()
