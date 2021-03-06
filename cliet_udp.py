from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
from inputimeout import inputimeout, TimeoutOccurred
import multiprocessing
import time


def esperar(partita_iniciada):
    print()

    if partita_iniciada == qtd_clientes:
        print("Aguardando Jogadores \r\n")
        resposta_servidor = socket_cliente.recvfrom(1024)

        print(str(resposta_servidor[0].decode()))
        print()
        responder()


def responder():

    resposta_servidor = socket_cliente.recvfrom(1024)

    if str(resposta_servidor[0].decode()) != "500":
        print(str(resposta_servidor[0].decode()))
        try:
            mensagem = inputimeout(prompt="Digite sua resposta: ", timeout=5)
        except TimeoutOccurred:
            mensagem = "nao respondeu"

        mensagem_codificada = mensagem.encode()
        socket_cliente.sendto(mensagem_codificada, ("localhost", 9090))
        print("Resposta enviada... \r\n")
        resposta_servidor = socket_cliente.recvfrom(1024)
        print(str(resposta_servidor[0].decode()))
        responder()

    else:

        print("\nFim de jogo. \n")
        ranking()


def ranking():

    print("Ranking")
    for _ in range(2):  # testando 2 cliente
        resposta_servidor = socket_cliente.recvfrom(1024)
        print(str(resposta_servidor[0].decode()))
    socket_cliente.close()


iniciar = True
socket_cliente = socket(AF_INET, SOCK_DGRAM)

qtd_clientes = 2

partita_iniciada = []
while iniciar:
    print()
    mensagem = input("Digite o seu login para se conectar: ")
    if mensagem != "":
        mensagem_codificada = mensagem.encode()
        socket_cliente.sendto(mensagem_codificada, ("localhost", 9090))
        resposta_servidor = socket_cliente.recvfrom(1024)

        if partita_iniciada == []:
            cont = 0
            partita_iniciada.append(cont)

        if str(resposta_servidor[0].decode()) == "101":
            print(f"O(A) jogadoror(a) {mensagem} foi Cadastrado(a).")

            iniciar = False

            partita_iniciada[0] += qtd_clientes
            # tentando com 2 mudar para 5 depois
            if partita_iniciada[0] <= qtd_clientes:
                Thread(target=esperar, args=(partita_iniciada)).start()

        else:

            if resposta_servidor[0].decode() == "410":  # nega????o de acesso
                print("\nPartida em andamento, tente novamente mais tarde.\n")
                socket_cliente.close()
                iniciar = False

    else:
        protocolo_erro = "401"
        print("Nome inv??lido, tente novamente.  \r\n")
        print(f"Nega????o de acesso {protocolo_erro}.  \r\n")
