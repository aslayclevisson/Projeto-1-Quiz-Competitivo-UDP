from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread


socket_cliente = socket(AF_INET, SOCK_DGRAM)

iniciar = True

while iniciar:

    mensagem = input("Digite o seu login para se conectar: ")
    if mensagem != "":
        mensagem_codificada = mensagem.encode()
        socket_cliente.sendto(mensagem_codificada, ("localhost", 9090))

        resposta_servidor = socket_cliente.recvfrom(1024)
        if str(resposta_servidor[0].decode()) == "101":
            print("Participante Cadastrado.")
            
    else:
        print("Nome inválido, tente novamente. \r\n")