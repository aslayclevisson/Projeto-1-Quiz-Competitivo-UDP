from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread


def receber_dados():
    dados, endereco = socket_cliente.recvfrom(4096)
    print(dados.decode())
 


host = "localhost"
port = 5556


socket_cliente = socket(AF_INET, SOCK_DGRAM)


socket_cliente.connect((host, port))

iniciar = True


while iniciar:
    mensagem = input("Digite o seu nickname: ")
    

    if mensagem != "":
        socket_cliente.sendto(mensagem.encode(), (host, port))
        print("Cadastro efetuado com sucesso.\n")
        iniciar = False
    else:
        print("Nickname inválido, nickname vázio, digite novamente.")



def comunicar():
    
    resposta = input("Digite a resposta: ")
    socket_cliente.sendto(resposta.encode(), (host, port))
    print("Resposta enviada. \n")

Thread(target= comunicar, args=()).start()
