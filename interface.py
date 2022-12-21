import serial
import time
import platform
import threading

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
        return ""


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
        self.channel = 11
        self.ping_f = 100
    
    #change defult incase of you needed to.
    def set_port(self,port,baud):
        self.ser.close()
        self.port = port
        self.baud = baud
        self.ser = serial.Serial(port,baud)
    
    def set_channel(self,channel):
        self.channel = channel
    
    def set_ping_f(self,ping_f):
        self.ping_f = ping_f

    def set_timeout(self,t):
        self.timeout = t

    
    
    #Monitor serial input
    def __monitor(self):#thread
        while not self.stop:
            self.lock.acquire()
            incoming = read(self.ser)
            self.queue = self.queue + incoming
            print(incoming,end='')
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
    
    #send command that is been preset in system
    def send_command(self,command):
        if command == "ping":
            self.send("ping --timeout="+str(self.timeout) + " --c="+str(self.channel) + " --f=" + str(self.ping_f))
        elif command == "recv":
            self.send("recv --timeout="+str(self.timeout) + " --c="+str(self.channel))
        elif command == "check":
            self.send("check")
        elif command == "restart":
            self.send("restart")
        

