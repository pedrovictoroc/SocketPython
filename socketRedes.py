import socket

skt = socket.socket()
print('Socket criado com sucesso')

port = 8080

# Aqui vamos fazer bind do socket a uma porta
# note que passamos uma string vazia, isso permite
# que computadores da rede possam acessar
skt.bind(('',port))
print('Socket ligado à porta {}'.format(port))

# Socket limita a 5 conexões da fila
# isso pode parecer pouco, mas é o padrão
# com uma boa implementação, será suficiente
skt.listen(5)

# Criaremos um loop infinito que irá parar apenas
# quando quisermos ou um erro ocorra
while True:


    # Estabelece conexão com um client
    client, address = skt.accept()

    print('Conexão estabelecida com {}'.format(address))

    # Envia mensagem para o cliente
    #client.send('Obrigado por se conectar!'.encode('utf-8'))

    filenameString = client.recv(1024).decode('utf-8')

    filenames = filenameString.split(',')

    for fileName in filenames:
        try:
            
            file = open('./arquivos/{}'.format(fileName), 'r')

            toSendFile = file.read()

            print('Página encontrada')

            # Seta o status no header para 200
            responseHeader = "HTTP/1.1 200 OK\r\n"
            
            # Envia o header
            client.send(responseHeader.encode('utf-8'))
            client.send('\n'.encode('utf-8'))

        

            # Envia página requisitada para o client
            for i in range(0,len(toSendFile)):
                client.send(toSendFile[i].encode('utf-8'))

            # Fecha a conexão com o client
            client.close()
        
        except IOError as err:
            print("Arquivo não encontrado")
            print(err)

            # Seta no header o status de erro para o client
            errorHeader = "HTTP/1.1 404 Not Found\r\n"

            # Envia o header
            client.send(errorHeader.encode('utf-8'))
            client.send('\n'.encode('utf-8'))

            # Prepara página de erro para ser enviada
            errorPage = open('./arquivos/error.html','r')
            responseError = errorPage.read()

            # Envia página de erro para o client
            for i in range(0,len(responseError)):
                client.send(responseError[i].encode('utf-8'))
            
            # Fecha a conexão
            client.close()
