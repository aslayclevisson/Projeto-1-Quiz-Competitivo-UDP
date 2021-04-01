from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
from inputimeout import inputimeout, TimeoutOccurred
import random
import multiprocessing
import time


def quicksort(vetor, indiceinicial=0, indiceparada=None):
    if indiceparada == None:
        indiceparada = len(vetor) - 1

    if indiceinicial < indiceparada:
        pivor = particao(vetor, indiceinicial, indiceparada)
        quicksort(vetor, indiceinicial, pivor - 1)
        quicksort(vetor, pivor + 1, indiceparada)


def particao(vetor, indiceinicial, indiceparada):
    indice_de_inicio = indiceinicial
    pivor = vetor[indiceparada][1]
    for i in range(indiceinicial, indiceparada):
        if vetor[i][1] >= pivor:
            vetor[indice_de_inicio], vetor[i] = vetor[i], vetor[indice_de_inicio]
            indice_de_inicio += 1

    else:
        vetor[indice_de_inicio], vetor[indiceparada] = vetor[indiceparada], vetor[indice_de_inicio]

    return indice_de_inicio


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

    respostas(participantes, perguntas_e_respostas,
              valor, contador_indice_pergunta, sub_lista_n_pergunta)

# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA


def respostas(participantes, perguntas_e_respostas, valor, contador, indicesP):

    for endereco in participantes:
        pergunta = str.encode(
            perguntas_e_respostas[indicesP[contador]][0])
        socket_servidor.sendto(pergunta, (endereco))

    qtd_msg = 0
    dic_resposta = {}
    while qtd_msg < qtd_clientes:  # testando 2 cliente

        mensagem_cliente, endereco_cliente = socket_servidor.recvfrom(1024)
        if endereco_cliente in participantes.keys():
            dic_resposta[endereco_cliente] = mensagem_cliente.decode()
            print(
                f"MSG: {mensagem_cliente.decode()} do(a) jogador(a) {participantes[endereco_cliente][0].decode()}")
            qtd_msg += 1

        else:
            resposta_negação = "410"
            print(">>>Jogador tentando se conetar, mas foi recusado<<<")
            socket_servidor.sendto(
                resposta_negação.encode(), (endereco_cliente))

    for k, v in dic_resposta.items():
        if v == perguntas_e_respostas[indicesP[contador]][1]:

            print(
                f"O(A) jogador(a) {participantes[k][0].decode()} acertou a resposta")
            participantes[k][1] += 25
            resposta_1_cliente = str.encode(
                f"Parabéns! Você acertou a resposta e ganhou 25 pontos. Sua pontuação atual é {participantes[k][1]}")

            socket_servidor.sendto(resposta_1_cliente, (k))
        else:
            print(f'contador {contador}, valor {valor}')
            print(
                f"O(A) jogador(a) {participantes[k][0].decode()} errou a resposta")
            participantes[k][1] -= 5
            resposta_1_cliente = str.encode(
                f"Infelizmente, você errou a resposta e perdeu 5 pontos. Sua pontuação atual é {participantes[k][1]}\n")
            socket_servidor.sendto(resposta_1_cliente, (k))

    valor += 1
    contador += 1

    if valor != 3 and contador != 3:  # aq define a quantidade de perguntas

        Thread(target=respostas, args=(participantes,
               perguntas_e_respostas, valor, contador, indicesP)).start()

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
            cont += 1

        resposta = "500"
        resposta_cliente = str.encode(resposta)
        for x, y in dic_resposta.items():
            socket_servidor.sendto(resposta_cliente, x)

        listao = []
        for x in participantes.values():
            listao.append(x)

        ordena_listao = quicksort(listao)

        for x in listao:
            for y in participantes.keys():
                classificacao = str.encode(
                    f"A pontuação do(a) jogardor(a) {x[0].decode()} foi de: {x[1]} pontos.")
                socket_servidor.sendto(classificacao, y)


# implementar o time


perguntas_e_respostas = ler_arquivo()
socket_servidor = socket(AF_INET, SOCK_DGRAM)
socket_servidor.bind(("localhost", 9090))

# implementação randomificação
sub_lista_n_pergunta = []
while len(sub_lista_n_pergunta) < 3:
    indice_aleatorio = random.randint(0, 2)

    if indice_aleatorio not in sub_lista_n_pergunta:
        sub_lista_n_pergunta.append(indice_aleatorio)

# -------------------------------------------------

contador_indice_pergunta = 0
conexao_start = True
valor = 0
participantes = {}
qtd_clientes = 2


# testando com 2

while conexao_start and len(participantes) < qtd_clientes:  # testando 2 cliente

    print()
    print("Aguardando requisições... \r\n")

    mensagem_cliente, endereco_cliente = socket_servidor.recvfrom(1024)
    participantes[endereco_cliente] = [mensagem_cliente, 0]
    print(f"O/A participante {mensagem_cliente.decode()} entrou")

    resposta = "101"
    resposta_cliente = str.encode(resposta)
    socket_servidor.sendto(resposta_cliente, endereco_cliente)
    print("Resposta enviada para o/a participante \r\n")


if len(participantes) == qtd_clientes:  # testando 2 cliente
    print("200 OK \r\n")

    mensagem_start = "O jogo vai começar!"

    Thread(target=perguntas, args=(mensagem_start, participantes, valor)).start()

# Até aqui deu certo, amém
