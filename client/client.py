import socket
import threading
import time
class Client:
    HOST = "localhost"
    PORT = 5500
    BUFSIZ = 512
    ADDR = (HOST, PORT)

    def __init__(self, name):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)
        self.messages = []
        receive_thread = threading.Thread(target=self.receive_msg)
        receive_thread.start()

        self.send_msg(str(name))



    def receive_msg(self):
        while True:
            try:
                msg = self.client.recv(self.BUFSIZ).decode('utf8')
                self.messages.append(msg)
                print(msg)
            except Exception as e:
                print("[EXCEPTION] ", e)
                break

    def send_msg(self, msg):
        self.client.send(bytes(msg, 'utf8'))
        if msg == '{quit}':
            # properly close the connections
            self.client.close()

    def get_messages(self):
        return self.messages
