import threading
import socket as s

SIZE = 1024

class chat_manager():
    def __init__(self):
        self.sender = s.socket(s.AF_INET,s.SOCK_DGRAM)
        self.port = 5000
        self.receiver = s.socket(s.AF_INET,s.SOCK_DGRAM)
        self.lock = threading.Lock()
        self.receive_thread = None
        self.run_receive = True
        self.queue = b''
    
    def chat_init(self):
        self.sender.setsockopt(s.SOL_SOCKET, s.SO_BROADCAST, 1)
        self.receiver.setsockopt(s.SOL_SOCKET, s.SO_BROADCAST, 1)
        self.receiver.bind(('255.255.255.255', self.port))
        print('Listening for broadcast at ', self.receiver.getsockname())


    #data receive task
    def receive_task(self):
        self.run_receive = True
        while self.run_receive:
            data, address = self.receiver.recvfrom(1024)
            self.lock.acquire()
            self.queue = self.queue + data
            self.lock.release()
    def receive_start(self):
        self.receive_thread = threading.Thread(target = self.receive_task)
        self.receive_thread.start()
    def receive_stop(self):
        self.run_receive = False
        self.receive_thread.join()
    
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

    #data send task
    def sendto(self,message):
        interfaces = s.getaddrinfo(host=s.gethostname(), port=None, family=s.AF_INET)
        allips = [ip[-1][0] for ip in interfaces]
        for ip in allips:
            print(ip)
            self.sender.sendto(message.encode('utf-8'), (ip, self.port))
        #self.sender.sendto(message.encode('utf-8'), ('255.255.255.255', self.port))
        print(message)