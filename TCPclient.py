from socket import *
from colorama import Fore, Style, init
init()
serverName = 'localhost'
serverPort = 1202
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print(Fore.RED + """
-------------------------------------------
|  *          *           *             * |
|    QUANTOS DIAS FALTAM PARA O NATAL?    |
|       *  + Mensagem natalina        *   |
----------          *          -----------|
-------------------------------------------
""" + Style.RESET_ALL)
data = input("Entre com a data de hoje no formato dd/mm/aaaa: ")
clientSocket. send(data.encode())
response = clientSocket.recv(1024).decode()
print(response)
clientSocket.close()