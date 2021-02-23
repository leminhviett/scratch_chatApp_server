# import socket
# import threading
# import time
#
# HOST = "localhost"
# PORT = 5500
# BUFSIZ = 512
# ADDR = (HOST, PORT)
#
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(ADDR)
#
# def receive_msg():
#     #always listen to the message, otherwise error will be raised
#     while True:
#         try:
#             msg = client.recv(BUFSIZ).decode('utf-8')
#             print(msg)
#         except Exception as e:
#             print("[EXCEPTION] ",e)
#             break
#
# def send_msg(msg):
#     client.send(bytes(msg, 'utf8'))
#     if msg == '{quit}':
#         #properly close the connections
#         client.close()
#
# threading.Thread(target=receive_msg).start()
#
# namme = input('your name ?')
#
# send_msg(namme)
# time.sleep(2)
# msg = input('1st msg: ')
# send_msg(msg)
# time.sleep(2)
#
# send_msg("{quit}")
#

from client import Client
import time
c1 = Client("Viet")
# c2 = Client("Le")

c1.send_msg("hi")
time.sleep(1)
c1.send_msg("{quit}")
# c2.send_msg("hello")

time.sleep(2)
print(c1.get_messages())
# print(c2.get_messages())