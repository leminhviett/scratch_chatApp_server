from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from person import Persons


HOST = "localhost"
PORT = 5500
BUFSIZ = 512
ADDR = (HOST, PORT)
MAX_CONNS = 10

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

persons = []

def broadcast(msg, name=""):
    real_msg = f"{name} : {msg}"
    print("[BROACAST] {}".format(real_msg))
    for person in persons:
        person.socket.send(bytes(real_msg, "utf8"))

def client_communication(person):
    addr = person.address
    client = person.socket

    name = client.recv(BUFSIZ).decode("utf8")
    person.set_name(name)
    broadcast("has joined", name)
    while True:
        msg = client.recv(BUFSIZ).decode("utf8")

        if msg == "{quit}":
            persons.remove(person)
            client.close()
            broadcast("quit", name)
            break
        else:
            broadcast(msg, name)


def wait_for_connections(SERVER):
    while True:
        try:
            socket, client_addr = SERVER.accept()
            socket.send(bytes(f"Hi, welcome! Now what s ur name ?", "utf8"))
            person = Persons(socket, client_addr)
            persons.append(person)
            Thread(target=client_communication, args=(person, ), name='client_com').start()

        except Exception as e:
            print('[Failure] when a client try to join...', e)



if __name__ == "__main__":
    SERVER.listen(MAX_CONNS)

    print("Waiting for connection...")

    ACCEPT_THREAD = Thread(target=wait_for_connections, args=(SERVER, ))
    ACCEPT_THREAD.start()  # Starts the infinite loop.
    ACCEPT_THREAD.join()
    SERVER.close()
