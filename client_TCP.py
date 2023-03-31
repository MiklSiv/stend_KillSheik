import socket
import time


class Client():
    def __init__(self, adress_server, port_server):
        self.adress = adress_server
        self.port = port_server
        self.client = None
        self.flag = True
        self.client = socket.socket()

    def hello_server(self):
        while True:
            try:
                self.client.connect((self.adress, self.port))
                break
            except:
                pass
            time.sleep(0.5)


    def send_to_server(self, vvod):
        while self.flag:
            try:
                self.client.send(vvod.encode('UTF-8'))
                if vvod == 'close':
                    self.flag = False
                    break
            except:
                pass


    def read_from_serevr(self):
        while self.flag:
            try:
                data = self.client.recv(1024).decode('utf-8')
                return data
            except:
                pass




client = Client('127.0.0.1', 5000)
client.hello_server()

