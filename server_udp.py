from socket import  socket, AF_INET, SOCK_DGRAM
from threading import Thread




def comunicacao(dados_cliente, endereco_cliente):

    iniciar_pergunta = True

    while iniciar_pergunta:
        p_r= perguntas_respostas()
        print(p_r[0])
        
        iniciar_pergunta = False
    dados_cliente, endereco_cliente = socket_servidor.recvfrom(4096)
  
    if dados_cliente.decode() != p_r[1]:
        print("resposta incorreta")
    else:
        print("Resposta correta")
    
    #dados_cliente, endereco_cliente = socket_servidor.recvfrom(4096)
    #rint(f"O cliente falou {endereco_cliente}: {dados_cliente.decode()} ")
    #Thread(target=comunicacao, args=(dados_cliente, endereco_cliente)).start()
       

guardar_participantes(dados_cliente, endereco_cliente):

    pass
    
def perguntas_respostas():
    p1r1 = ("Qual é a cidade mais lida do mundo ?", "Recife")
    return p1r1
        

host = "localhost"
port = 5556


socket_servidor = socket(AF_INET, SOCK_DGRAM)
socket_servidor.bind((host, port))


print("Servidor On")


conexao_start = True


while conexao_start:
    print("Aguardando requisições... \n")
    dados_cliente, endereco_cliente = socket_servidor.recvfrom(4096)
    if dados_cliente.decode() != "":
        print(f"O participante {dados_cliente.decode()} foi cadastrado. \n")
        Thread(target=comunicacao, args=(dados_cliente, endereco_cliente)).start()
        conexao_start = False

