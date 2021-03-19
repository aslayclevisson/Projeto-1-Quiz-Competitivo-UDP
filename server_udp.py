from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
import random




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


def iniciar_partida(mensagem_cliente, participantes, valor):
    
    for endereco in participantes.keys():
        socket_servidor.sendto(str.encode(mensagem_cliente), (endereco))
        print("A pergunta foi enviada aos jogadores \n")

   
    perguntar(participantes, perguntas_e_respostas, valor)
    

def perguntar(participantes, perguntas_e_respostas, valor):

    lista = [0,1]
    pegar = random.choice(lista)
    

    for endereco in participantes:

        pergunta = str.encode(perguntas_e_respostas[pegar][0])
        
        socket_servidor.sendto(pergunta, (endereco))

    qtd_msg = 0
    dic_resposta = {}
    while qtd_msg < 2:#valor vai aumentar para 5
        mensagem_cliente, endereco_cliente = socket_servidor.recvfrom(1024)
        dic_resposta[endereco_cliente] = mensagem_cliente.decode()
        print(f"MSG: {mensagem_cliente.decode()} do(a) jogador(a) {participantes[endereco_cliente][0].decode()}")
        qtd_msg +=1

    for k, v in dic_resposta.items():
        if v == perguntas_e_respostas[pegar][1]:
            print(f"O(A) jogador(a) {participantes[k][0].decode()} acertou a resposta")
            participantes[k][1] += 25
            resposta_1_cliente = str.encode(f"Você acertou a resposta sua pontuação atua é {participantes[k][1]}")
            socket_servidor.sendto(resposta_1_cliente, (k))
        else:
            print(f"O(A) jogador(a) {participantes[k][0].decode()} errou a resposta")
            participantes[k][1] -= 5
            resposta_1_cliente = str.encode(f"Você errou a resposta sua pontuação atua é {participantes[k][1]}")
            socket_servidor.sendto(resposta_1_cliente, (k))

    del lista[pegar]
    valor +=1
    if valor != 2:#mudar para 5 depois
        Thread(target=perguntar, args=(participantes, perguntas_e_respostas, valor)).start()
    else:
        resposta = "500"
        resposta_cliente = str.encode(resposta)
        for x, y in dic_resposta.items():
            socket_servidor.sendto(resposta_cliente, x)
        print("FINISH")

# implementar o time
            


socket_servidor = socket(AF_INET, SOCK_DGRAM)
socket_servidor.bind(("localhost", 9090))
conexao_start = True
valor = 0
participantes = {}
perguntas_e_respostas = ler_arquivo()

# testando com 2

while conexao_start and len(participantes) < 2:
    print("Aguardando requisições... \r\n")

    mensagem_cliente, endereco_cliente = socket_servidor.recvfrom(1024)
    participantes[endereco_cliente] = [mensagem_cliente, 0]
    print(f"O/A participante {mensagem_cliente.decode()} entrou")

    resposta = "101"
    resposta_cliente = str.encode(resposta)
    socket_servidor.sendto(resposta_cliente, endereco_cliente)
    print("Resposta enviada para o/a participante \r\n")


if len(participantes) == 2:
    print("200 OK \r\n")
    mensagem_start = "O jogo vai começar!"
    
    Thread(target=iniciar_partida, args=(mensagem_start, participantes, valor)).start()
