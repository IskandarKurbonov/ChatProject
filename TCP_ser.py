import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 5551))
client = []  # Массив где храним адреса клиентов
print('Start Server')
while 1:
    data, addres = sock.recvfrom(1024)
    print(addres[0], addres[1])
    if addres not in client:
        # Если такого клиента нету , то добавить
        client.append(addres)
    for clients in client:
        if clients == addres:
            # Не отправлять данные клиенту, который их прислал
            continue
        sock.sendto(data, clients)