from socket import *
from colorama import Fore, Style, init
import random
init()
serverPort = 1202
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind( ('', serverPort))
print("The server is ready to receive")

ascii_arts = [
r"""
.      *    *           *.       *   .                      *     .
               .   .                   __   *    .     * .     *
    *       *         *   .     .    _|__|_        *    __   .       *
  .  *  /\       /\          *        ('')    *       _|__|_     .
       /  \   * /  \  *          .  <( . )> *  .       ('')   *   *
  *    /  \     /  \   .   *       _(__.__)_  _   ,--<(  . )>  .    .
      /    \   /    \          *   |       |  )),`   (   .  )     *
   *   `||` ..  `||`   . *.   ... ==========='`   ... '--`-` ... * jb .

""",
r"""
   .-.                                                   \ /
  ( (                                |                  - * -
   '-`                              -+-                  / \
            \            o          _|_          \
            ))          }^{        /___\         ))
          .-#-----.     /|\     .---'-'---.    .-#-----.
     ___ /_________\   //|\\   /___________\  /_________\  
    /___\ |[] _ []|    //|\\    | A /^\ A |    |[] _ []| _.O,_
....|"#"|.|  |*|  |...///|\\\...|   |"|   |....|  |*|  |..(^).... ldb

""",
r"""
    .--._.--.--.__.--.--.__.--.--.__.--.--._.--.
  _(_      _Y_      _Y_      _Y_      _Y_      _)_
 [___]    [___]    [___]    [___]    [___]    [___]
 /:' \    /:' \    /:' \    /:' \    /:' \    /:' \
|::   |  |::   |  |::   |  |::   |  |::   |  |::   |
\::.  /  \::.  /  \::.  /  \::.  /  \::.  /  \::.  /
 \::./    \::./    \::./    \::./    \::./    \::./
  '='      '='      '='      '='      '='  jgs '='

""",
r"""            *
    *  ':.
         []_____
        /\      \  *
 *  ___/  \__/\__\__
---/\___\ |''''''|__\-- --- *
   ||'''| |''||''|''|
*   ``---`-`--))--`--`   *
            *
"""
]

while True:
    color, clientAddress = serverSocket.recvfrom(2048)
    color = color.decode().strip().lower()
    ascii_art = random.choice(ascii_arts)

    if color == "verde":
        response = Fore.GREEN + ascii_art + Style.RESET_ALL

    elif color == "vermelho":
        response = Fore.RED + ascii_art + Style.RESET_ALL
        
    else:
        response = "Digite uma opção válida."
 
    serverSocket.sendto(response.encode(), 
clientAddress)


