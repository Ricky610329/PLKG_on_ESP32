import threading
from socket import socket,gethostbyname,AF_INET,SOCK_DGRAM


SIZE = 1024

class chat:
    def __init__(self,IP,PORT=5000):
        self.IP = IP
        self.PORT = PORT
        self.stop = False
        self.lock = threading.Lock()
        self.queue = b""
        self.recv = 0
        self.recv_thread = 0
        self.send_data = 0
    def receive_task(self):
        while not self.stop:
            (data,addr) = self.recv.recvfrom(SIZE)
            self.lock.acquire()
            self.queue = self.queue + data
            self.lock.release()
    def send_init(self):
        self.send_data = socket(AF_INET,SOCK_DGRAM)
        self.send_data.connect((self.IP,self.PORT))
    
    #start to receiving task, and init send
    def chat_init(self):
        self.stop = False
        self.send_init()
        hostName = gethostbyname( '0.0.0.0' )
        self.recv = socket(AF_INET,SOCK_DGRAM)
        self.recv.bind((hostName,self.PORT))
        self.recv_thread = threading.Thread(target=self.receive_task)
        self.recv_thread.start()

    #stop receive task
    def receive_stop(self):
        self.stop = True
        self.recv_thread.join()

    #data manipulation
    def pop(self):
        self.lock.acquire()
        if self.queue == b'':
            self.lock.release()
            return b''
        else:
            top = self.queue[0]
            self.queue = self.queue[1:]
            self.lock.release()
            return top
    def queue_clear(self):
        self.lock.acquire()
        self.queue = b''
        self.lock.release()
    def read_queue(self):
        self.lock.acquire()
        output = self.queue
        self.queue = b''
        self.lock.release()
        return output

    def send(self,message):
        self.send_data.send(message.encode('utf-8'))