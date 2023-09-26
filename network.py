import socket,select
 
class Network:
    def __init__(self):

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.server = "127.0.0.1"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.masgs = self.connect()
        print(self.masgs)

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()

        except:
            pass
    def send(self,data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)
            


    def recv(self):

        self.client.setblocking(0)
        ready = select.select([self.client],[],[],1)
        if ready[0]:
            pass
        try:
            return self.client.recv(2048)      
        except socket.error as e:
            print(e)
        
