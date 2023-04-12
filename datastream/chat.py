import threading
from socket import socket,gethostbyname,AF_INET,SOCK_DGRAM
import re

SIZE = 8000

class chat_manager:
    def __init__(self,IP,PORT=5000):
        self.IP = IP
        self.PORT = PORT
        self.stop = False
        self.queue = b""
        self.recv = 0
        self.recv_thread = 0
        self.send_data = 0
    def receive_task(self):
        while not self.stop:
            (data,addr) = self.recv.recvfrom(SIZE)
            self.queue = self.queue + data
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

    #close socket
    def close_socket(self):
        self.stop = True
        self.recv_thread.join()
        self.send_data.close()
        self.recv.close()

    #data manipulation
    def pop(self):
        if self.queue == b'':
            return b''
        else:
            top = self.queue[0]
            self.queue = self.queue[1:]
            return top
    #return string
    def pop_line(self):
        output = self.queue
        if output == b'':
            return 'FAIL'
        else:
            output = output.decode('utf-8')
            output = re.search(".*?-end",output).group()
            self.queue = self.queue[len(output.encode('utf-8')):]
            return output[:-4]

    def queue_clear(self):
        self.queue = b''
    def read_queue(self):
        output = self.queue
        self.queue = b''
        return output
    

    def send(self,message):
        self.send_data.send(message.encode('utf-8'))

    def send_line(self,message):
        line = message+'-end'
        self.send_data.send(line.encode('utf-8'))