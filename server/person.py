class Persons:
    def __init__(self, socket, address):
        self.name = None
        self.socket = socket
        self.address = address

    def set_name(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.address} : {self.name}"
