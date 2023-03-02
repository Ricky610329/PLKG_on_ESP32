import threading
from socket import socket,gethostbyname,AF_INET,SOCK_DGRAM

SIZE = 1024

class chat_manager():
    def __init__(self):
        self.sender = socket(AF_INET,SOCK_DGRAM).connect((socket.gethostbyname(socket.gethostname()),5000))
        self.reciver = socket(AF_INET,SOCK_DGRAM).bind((socket.gethostbyname("0.0.0.0"),5000))
        self.lock = threading.Lock()
        self.queue = ""
        self.recv = 0
        self.recv_thread = 0
        self.send_data = 0
