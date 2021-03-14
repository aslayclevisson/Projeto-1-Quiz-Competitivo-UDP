from socket import  socket, AF_INET, SOCK_DGRAM
from threading import Thread

#falta corrigir a continuação das perguntas obs remoer perguntas ja feitas


def comunicacao(dados_cliente, endereco_cliente, participantes):

    iniciar_pergunta = True
    arquivo_quiz = ler_arquivo()
    cont = 0
    while iniciar_pergunta:
       print(arquivo_quiz[cont][0])
       cont+=1
       iniciar_pergunta = False

    dados_cliente, endereco_cliente = socket_servidor.recvfrom(4096)


    print(f"O participante {participantes[endereco_cliente]} respondeu {dados_cliente.decode()}")

    if dados_cliente.decode() != arquivo_quiz[0][1]:
  
        print("resposta incorreta")
    else:
        
        print("Resposta correta")
    Thread(target=comunicacao, args=(dados_cliente, port, participantes)).start()

   


def pr():
    p1r1 = ("Qual é a cidade mais lida do mundo ?", "Recife")
    return p1r1


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


host = "localhost"
port = 5556
port_2 =4443

socket_servidor = socket(AF_INET, SOCK_DGRAM)
socket_servidor.bind((host, port))

participantes = {}

print("Servidor On")


conexao_start = True



while conexao_start and len(participantes) < 2:
    print("Aguardando requisições... \n")
    
    dados_cliente, endereco_cliente = socket_servidor.recvfrom(4096)
    participantes[endereco_cliente] = dados_cliente.decode()
    
    if dados_cliente.decode() != "":
        print(f"O participante {dados_cliente.decode()} foi cadastrado. \n")
 
if len(participantes) == 2:
    print("*********", participantes)
        
            #Thread(target=comunicacao, args=(dados_cliente, port)).start()

        
    Thread(target=comunicacao, args=(dados_cliente, port, participantes)).start()




