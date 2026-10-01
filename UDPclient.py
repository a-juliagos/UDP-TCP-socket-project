from socket import *
from colorama import Fore, Style, init
init()
serverName = 'localhost'
serverPort = 1202
clientSocket = socket(AF_INET, SOCK_DGRAM)
print(Fore.YELLOW +"""
===========================================
|  *          *           *             * |
|   SERVIDOR DE ARTES NATALINAS ASCII     |
|       *             *          *        |
========      *                   ========|
|   *         [1] Verde                *  |
|          *  [2] Vermelho    *           |
===========================================
""" + Style.RESET_ALL)
message = input("Digite 'verde' ou 'vermelho': ")
clientSocket. sendto(message.encode(), (serverName, serverPort))
response, serverAddress = clientSocket.recvfrom(2048)
print(response.decode ())
clientSocket.close() 