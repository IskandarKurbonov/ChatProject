import socket
import threading
import os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 27017))
print("\t\t====>  UDP CHAT  <=====")
print("==============================================")
nm = input("Введите имя: ")
print("\nВведите \q для выхода.")

ip = '127.0.0.1'
port = '27017'

def send():
    while True:
        ms = input(">>> ")
        if ms == "\q":
            os._exit(1)
        sm = "{}  : {}".format(nm, ms)
        s.sendto(sm.encode(), (ip, int(port)))

def rec():
    while True:
        msg = s.recvfrom(1024)
        print("\t\t\t\t >>> " + msg[0].decode())
        print(">>> ")
x1 = threading.Thread(target = send)
x2 = threading.Thread(target = rec)

x1.start()
x2.start()