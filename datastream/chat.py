import threading
from socket import socket,gethostbyname,AF_INET,SOCK_DGRAM


SIZE = 1024

class chat:
    def __init__(self,IP,PORT=5000):
        self.IP = IP
        self.PORT = PORT
        self.stop = False
        self.lock = threading.Lock()
        self.queue = ""
        self.recv = 0
        self.recv_thread = 0
        self.send_data = 0
    def receive_task(self):
        while not self.stop:
            (data,addr) = self.recv.recvfrom(SIZE)
            self.lock.acquire()
            self.queue = self.queue + data.decode('utf-8')
            self.lock.release()
    def send_init(self):
        self.send_data = socket(AF_INET,SOCK_DGRAM)
        self.send_data.connect((self.IP,self.PORT))
    def initialize(self):
        self.stop = False
        self.send_init()
        hostName = gethostbyname( '0.0.0.0' )
        self.recv = socket(AF_INET,SOCK_DGRAM)
        self.recv.bind((hostName,self.PORT))
        self.recv_thread = threading.Thread(target=self.receive_task)
        self.recv_thread.start()
    def receive_stop(self):
        self.stop = True
        self.recv_thread.join()

    def send(self,message):
        self.send_data.send(message.encode('utf-8'))