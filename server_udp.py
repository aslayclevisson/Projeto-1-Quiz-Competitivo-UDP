from socket import  socket, AF_INET, SOCK_DGRAM
from threading import Thread




def comunicacao(dados_cliente, endereco_cliente):

    iniciar_pergunta = True

    while iniciar_pergunta:
        p_r= perguntas_respostas()
        print(p_r[0])
        
        iniciar_pergunta = False

    dados_cliente, endereco_cliente = socket_servidor.recvfrom(4096)
    print(dados_cliente.decode())
    if dados_cliente.decode() != p_r[1]:
  
        print("resposta incorreta")
    else:
        r = "acertou"
        socket_servidor.sendto(r.encode(), (host, port))
        print("Resposta correta")

    socket_servidor.close()
"""
def resposta(dados_cliente,endereco_cliente):
    msg = "cliente conctado"
    socket_servidor.sendto(msg.encode(), (host,port))
    print("respota enviada")


def guardar_dados(dados_cliente, endereco_cliente):
    participantes = {}
    participantes[dados_cliente] = endereco_cliente
    return participantes
"""
def perguntas_respostas():
    p1r1 = ("Qual é a cidade mais lida do mundo ?", "Recife")
    return p1r1
    

host = "localhost"
port = 5556
port_2 =4443

socket_servidor = socket(AF_INET, SOCK_DGRAM)
socket_servidor.bind((host, port))


print("Servidor On")


conexao_start = True

maximo = 0

while conexao_start:
    print("Aguardando requisições... \n")
    
    dados_cliente, endereco_cliente = socket_servidor.recvfrom(4096)
    if dados_cliente.decode() != "":
        print(f"O participante {dados_cliente.decode()} foi cadastrado. \n")
        #resposta(dados_cliente, endereco_cliente)
        #guardar_dados(dados_cliente, endereco_cliente)
        Thread(target=comunicacao, args=(dados_cliente, port)).start()
   
        conexao_start = False



