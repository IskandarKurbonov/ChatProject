import socket
import threading

def read_sok():
    while 1:
        data = sor.recv(1024)
        print(data.decode('utf-8'))

server = 'localhost', 5551  # Данные сервера
alias = input('Введите имя: ')  # Ввод имени
sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sor.bind(('', 0))  # Задаем сокет как клиент
sor.sendto((alias + ' Connect to server').encode('utf-8'), server)  # Уведомление сервера о подключении
potok = threading.Thread(target=read_sok)
potok.start()
while 1:
    mensahe = input('Введите сообщение: ')
    sor.sendto(('\n[' + alias + ']' + mensahe).encode('utf-8'), server)