#################### BIBLIOTECAS ###########################
import socket
import time
import Adafruit_BBIO.UART as UART
import serial
from threading import Thread
import funcoes as f

#################### VARIAVEIS #############################
texto = 'ACK'
msg = ' '

##################### FUNCOES ##############################


####################SERVIDOR##################################
HOST = ''  # Endereco IP do Servidor
PORT = 12345  # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria o mecanismo de Socket para receber a conecao
orig = (HOST, PORT)
while True:
    try:
        tcp.bind(orig)
        print('Aguardando comunicacao...')
    except:
        print('Tentando conectar!')
        time.sleep(2)
    else:
        break
tcp.listen(1)  # Define o limite de conexoes

########################### Loop #############################
while True:
    con, cliente = tcp.accept()  # Deixa o Servidor na escuta aguardando as conexoes
    print('Conectado por', cliente)  # Printa o ip do cliente conectado
    while True:
        try:
            recebe = Thread(target=f.recebe_mensagens, args=(con,))
            recebe.start()
            msg = ' '
            texto = input('Digite sua mensagem: ').upper()
            enviar = Thread(target=f.envia_mensagens, args=(con, texto))
            enviar.start()
        except:
            print('Perda de comunicacao')
            time.sleep(2)
            break
        else:
            if (texto == 'BREAK'):
                print('Finalizando conexão do cliente'.format(cliente))
                print('Aguardando nova conexao...')
                con.close()
                break
        try:
            print("Mensagem recebida do servidor: {}".format(f.mensagem.decode("utf-8")))
        except:
            print('Sem mensagem do cliente')


