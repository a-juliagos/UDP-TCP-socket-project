# UDP-TCP-socket-project

# 🎄 Serviço Natalino — TCP e UDP

Projeto acadêmico de **Redes de Computadores** desenvolvido em Python para demonstrar a comunicação **cliente-servidor** utilizando os protocolos **UDP e TCP**, com base nos exemplos de Kurose e Ross.

## 📡 UDP

O cliente envia uma cor (`verde` ou `vermelho`) para o servidor.

O servidor escolhe aleatoriamente uma **arte ASCII natalina**, aplica a cor escolhida e envia a arte de volta para o cliente.

```text
Cliente → "verde" → Servidor
                     ↓
              escolhe uma arte
                     ↓
Cliente ← arte colorida ← Servidor
```

## 🔗 TCP

O cliente envia uma data no formato `DD/MM/AAAA`.

O servidor calcula quantos dias faltam para o próximo Natal e envia o resultado de volta.

```text
Cliente → data → Servidor
                  ↓
           calcula os dias
                  ↓
Cliente ← resposta ← Servidor
```

## 🗂️ Arquivos

```text
UDPserver.py   → servidor UDP
UDPclient.py   → cliente UDP
TCPserver.py   → servidor TCP
TCPclient.py   → cliente TCP
requirements.txt → dependências
```

## 🛠️ Tecnologias

* Python
* Sockets
* UDP e TCP
* Colorama
* ASCII Art
* Docker

### Dependência

```text
colorama==0.4.6
```

O projeto foi desenvolvido para praticar conceitos de **sockets, comunicação cliente-servidor e diferenças entre UDP e TCP**, utilizando uma temática natalina para tornar a aplicação mais interativa. 🎄
