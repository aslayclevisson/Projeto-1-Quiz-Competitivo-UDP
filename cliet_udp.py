from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread


def esperar():
    print("Aguardando Jogadores")
    resposta_servidor = socket_cliente.recvfrom(1024)
   
    print(str(resposta_servidor[0].decode()))
    responder()
        
   



def responder():
    resposta_servidor = socket_cliente.recvfrom(1024)
    if str(resposta_servidor[0].decode()) != "500":
        print(str(resposta_servidor[0].decode()))
        mensagem = input("Digite sua resposta: ")
        mensagem_codificada = mensagem.encode()
        socket_cliente.sendto(mensagem_codificada, ("localhost", 9090))
        print("Resposta enviada \r\n")
        resposta_servidor = socket_cliente.recvfrom(1024)
        print(str(resposta_servidor[0].decode()))
        responder()
    else:
        print("Fim de jogo")
    
    
    



socket_cliente = socket(AF_INET, SOCK_DGRAM)

iniciar = True

while iniciar:

    mensagem = input("Digite o seu login para se conectar: ")
    if mensagem != "":
        mensagem_codificada = mensagem.encode()
        socket_cliente.sendto(mensagem_codificada, ("localhost", 9090))

        resposta_servidor = socket_cliente.recvfrom(1024)
        if str(resposta_servidor[0].decode()) == "101":
            print(f"O(A) jogadoror(a) {mensagem} foi Cadastrado(a) '101 Confirmado'.")
            iniciar = False

    else:
        print("Nome inválido, tente novamente. \r\n")

if iniciar == False:

    Thread(target=esperar, args=()).start()


