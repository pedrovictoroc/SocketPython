import socket

skt = socket.socket()

port = 8080

# Conecta ao socket servidor
skt.connect(('127.0.0.1',port))

filenameString = 'dbshjabdhjsbaj.txt, main.html, teste.html'

skt.send(filenameString.encode('utf-8'))

filenameArray = filenameString.split(', ')

for i in filenameArray:
    # socket irá ler até 2048 bytes de Header
    print(skt.recv(2048).decode('utf-8'))

    # socket irá ler até 2048 bytes de conteúdo
    print(skt.recv(2048).decode('utf-8'))

    # quebra de linha
    print(skt.recv(2048).decode('utf-8'))


skt.close()