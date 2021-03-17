from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread


socket_servidor = socket(AF_INET, SOCK_DGRAM)
socket_servidor.bind(("localhost", 9090))
conexao_start = True

participantes = {}

while conexao_start and len(participantes) < 2:
    print("Aguardando requisições... \r\n")

    mensagem_cliente, endereco_cliente = socket_servidor.recvfrom(1024)
    participantes[endereco_cliente] = mensagem_cliente
    print(f"O/A participante {mensagem_cliente.decode()} entrou")

    resposta = "101"
    resposta_cliente = str.encode(resposta)
    socket_servidor.sendto(resposta_cliente, endereco_cliente)
    print("Resposta enviada para o/a participante \r\n")

    #Thread(target=comunicacao, args=(dados_cliente, port, participantes)).start()
