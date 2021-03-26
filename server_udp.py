from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
import random
import multiprocessing
import time

def tempoLimite():
    for _ in range(5):
        time.sleep(1)
    print("fim")
    return True

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


def perguntas(mensagem_cliente, participantes, valor):
    
    for endereco in participantes.keys():
        socket_servidor.sendto(str.encode(mensagem_cliente), (endereco))
        print("A pergunta foi enviada aos jogadores \n")
    

   
    respostas(participantes, perguntas_e_respostas, valor)
    


def respostas(participantes, perguntas_e_respostas, valor):


    lista = [0,1]
    pegar = random.choice(lista)
    random.choices

    #CORRIGIR AS PERGUNTAS
    """
    for x in range(5):
        pegavalor= random.choice(lista)
        print(pegavalor)
        del lista[pegavalor]


    """

    for endereco in participantes:

        pergunta = str.encode(perguntas_e_respostas[pegar][0])
        
        socket_servidor.sendto(pergunta, (endereco))

    qtd_msg = 0
    dic_resposta = {}
    while qtd_msg < 1:  # testando 2 cliente
        
        mensagem_cliente, endereco_cliente = socket_servidor.recvfrom(1024)
        if endereco_cliente in participantes.keys():
            dic_resposta[endereco_cliente] = mensagem_cliente.decode()
            print(f"MSG: {mensagem_cliente.decode()} do(a) jogador(a) {participantes[endereco_cliente][0].decode()}")
            qtd_msg +=1
            

        else:
            resposta_negação = "410"
            print(">>>Jogador tentando se conetar, mas foi recusado<<<")
            socket_servidor.sendto(resposta_negação.encode(),(endereco_cliente))

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
    
   
    if valor != 3:#aq define a quantidade de perguntas
        
        Thread(target=respostas, args=(participantes, perguntas_e_respostas, valor)).start()
    else:

        lista_pontos = []

        for k, v in participantes.items():
            pontuação = v[1]
            lista_pontos.append(pontuação)

        lista_pontos_ordenada = sorted(lista_pontos)
        lista_ordenada = []
        cont = 0
        
        
        while len(lista_ordenada) < len(participantes):
            for v in participantes.values():
                if v[1] == lista_pontos_ordenada[cont]:
                    lista_ordenada.append(v[1])
            cont +=1

        
        resposta = "500"
        resposta_cliente = str.encode(resposta)
        for x, y in dic_resposta.items():
            socket_servidor.sendto(resposta_cliente, x)
        
        listão = []
        for x in participantes.values():
            listão.append(x)

        listão_ord = sorted(listão, key=lambda listao:[1])
       
         
        for x in  listão_ord:
            for y in participantes.keys():
                classificacao = str.encode( f"A pontuação do(a) jogardor(a) {x[0].decode()} foi de: {x[1]} pontos.")
                socket_servidor.sendto(classificacao, y)


# implementar o time



perguntas_e_respostas = ler_arquivo()
socket_servidor = socket(AF_INET, SOCK_DGRAM)
socket_servidor.bind(("localhost", 9090))

conexao_start = True
valor = 0
participantes = {}



# testando com 2

while conexao_start and len(participantes) < 1:  # testando 2 cliente
    
    print()
    print("Aguardando requisições... \r\n")
    
    mensagem_cliente, endereco_cliente = socket_servidor.recvfrom(1024)
    participantes[endereco_cliente] = [mensagem_cliente, 0]
    print(f"O/A participante {mensagem_cliente.decode()} entrou")

    resposta = "101"
    resposta_cliente = str.encode(resposta)
    socket_servidor.sendto(resposta_cliente, endereco_cliente)
    print("Resposta enviada para o/a participante \r\n")


if len(participantes) == 1:  # testando 2 cliente
    print("200 OK \r\n")

    mensagem_start = "O jogo vai começar!"
    
    Thread(target=perguntas, args=(mensagem_start, participantes, valor)).start()


