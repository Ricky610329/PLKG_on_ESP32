import serial
import time
import platform
import threading
import re
import csv

Enter = '\n' 
if platform.system() == 'Windows':
    Enter = '\r\n'
elif platform.system() == 'Darwin':
    Enter = '\r'


def send(ser,s):
    ser.write((s +Enter).encode())

def read(ser):
    try:
        return ser.read(ser.in_waiting).decode()
    except UnicodeDecodeError:
        return False

class com_esp():
    def __init__(self,port,baud):
        self.port = port
        self.baud = baud
        self.timeout = 10
        self.ser = serial.Serial(port,baud)
        self.lock = threading.Lock()
        self.queue = ""
        self.monitorThread = False
        self.stop = False
    
    def set_timeout(self,t):
        self.timeout = t
    
    def __monitor(self):#thread
        start = time.time()
        while not self.stop:
            timestamp = time.time() - start
            timestamp = "{:.2f},".format(timestamp)
            incoming = timestamp + read(self.ser)
            if incoming:
                self.lock.acquire()
                self.queue = self.queue + incoming
                #show probing result
                #print(incoming,end='')
                self.lock.release()
            time.sleep(0.1)
    
    def start_monitor(self):
        self.stop = False
        self.monitorThread = threading.Thread(target=self.__monitor)
        self.monitorThread.start()
    
    def stop_monitor(self):
        self.stop = True
        self.monitorThread.join()

    #clear queue
    def clear_queue(self):
        self.lock.acquire()
        self.queue = ""
        self.lock.release()
    
    #send raw data to ESP32
    def send(self,message):
        self.lock.acquire()
        send(self.ser,message)
        self.lock.release()
        time.sleep(0.1)

class rssi_massive_collection(com_esp):
    def __init__(self, port, baud):
        super().__init__(port, baud)
        self.filename = ''
    
    def csv_setup(self,filename):
        self.csv_object =  open(filename, 'a+')
        self.writer = self.csv_object.writer(self.csv_object)
    
    def csv_close(self):
        self.csv_object.close()
    
    def csv_save(self):
        hold = self.queue
        self.clear_queue()
        hold.split('\n')
        for i in range(len(hold)):
            hold[i] = [hold[i]]
        self.writer.writerows(hold)