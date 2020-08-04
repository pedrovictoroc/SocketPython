import socket

skt = socket.socket()

port = 8080

# Conecta ao socket servidor
skt.connect(('127.0.0.1',port))

skt.send('main.html'.encode('utf-8'))

#socket irá ler até 1024 bytes
print(skt.recv(2048).decode('utf-8'))

print(skt.recv(2048).decode('utf-8'))

skt.close()