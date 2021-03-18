from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
import random



def iniciar_partida(mensagem_cliente, participantes):
   
    for endereco in participantes.keys():
        socket_servidor.sendto(str.encode(mensagem_cliente), endereco)
    print("A resposta foi enviada aos jogadores \n")

    perguntar(participantes, perguntas_e_respostas)


def ler_arquivo():

    arquivo = open("perguntas_respostas.txt", "r")
    dados = arquivo.readlines()

    dadosModificado = []

    lista_tuplas = []

    for x in dados:
        dadosModificado.append(x.strip())

    cont = 0
    while cont < len(dadosModificado)-1:
        lista_tuplas.append((dadosModificado[cont], dadosModificado[cont+1]))
        cont += 2

    return lista_tuplas


def perguntar(participantes, perguntas_e_respostas):
 
    if len(perguntas_e_respostas) != 0:
        num_aleatorio = random.randint(0,1)
        for endereco in participantes:
            
            pergunta = str.encode(perguntas_e_respostas[num_aleatorio][0])
            socket_servidor.sendto(pergunta, (endereco))
       
        mensagem_cliente, endereco_cliente = socket_servidor.recvfrom(1024)
                
 
        if mensagem_cliente.decode() == perguntas_e_respostas[num_aleatorio][1]:
            for pessoa in participantes.keys():
                if pessoa == endereco_cliente:
                    print(f"O(A) Jogadoror(a) {participantes[endereco_cliente].decode()} acertou")
          

# Falta implementar receber a resposta de vários jogadores
  
        

socket_servidor = socket(AF_INET, SOCK_DGRAM)
socket_servidor.bind(("localhost", 9090))
conexao_start = True

participantes = {}
perguntas_e_respostas = ler_arquivo()
#testando com 2 

while conexao_start and len(participantes) < 2:
    print("Aguardando requisições... \r\n")

    mensagem_cliente, endereco_cliente = socket_servidor.recvfrom(1024)
    participantes[endereco_cliente] = mensagem_cliente
    print(f"O/A participante {mensagem_cliente.decode()} entrou")

    resposta = "101"
    resposta_cliente = str.encode(resposta)
    socket_servidor.sendto(resposta_cliente, endereco_cliente)
    print("Resposta enviada para o/a participante \r\n")


if len(participantes) == 2:
    mensagem_cliente = "O jogo vai começar! '200 ok'"
    Thread(target=iniciar_partida, args=(mensagem_cliente, participantes )).start()
