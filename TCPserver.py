import random
from socket import *
from datetime import datetime
from colorama import Fore, Style, init
init()
serverPort = 1202
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print(' The server is ready to receive ')

xmas_quotes = [
"🎄O natal é todo dia. 🎁", 
"❄️ A magia do Natal está nos pequenos gestos. 🦌", 
"🎅 A verdadeira magia do Natal acontece de dentro para fora. 🕯️",
"🎁 Que a sensibilidade do Natal permaneça com a gente por todos os meses.⛄"
]

while True :

    connectionSocket, addr = serverSocket.accept()
    data = connectionSocket.recv(1024).decode().strip()
    c_date = datetime.strptime(data, "%d/%m/%Y")
    natal = datetime(c_date.year, 12, 25)
    rem_days = (natal - c_date).days

    response = Fore.YELLOW + f"""   
                   *
   * {random.choice(xmas_quotes)}        *
*     Faltam {rem_days} dias para o Natal!!!                      
                       *                     * """ + Style.RESET_ALL

    connectionSocket.send(response.encode())
    connectionSocket.close()