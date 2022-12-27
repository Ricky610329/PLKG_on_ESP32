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


def savetocsv(filename,data):
    filename = filename + ".csv"
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for csi in data:
            writer.writerow([csi])
    



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
        self.ping_f = 4
    
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
            incoming = read(self.ser)
            if incoming:
                self.lock.acquire()
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
    

    def aquire_csi(self):
        self.stop_monitor()
        savedata = re.findall("CSI_DATA.*?\]",self.queue)
        self.clear_queue()
        return savedata

    def run_collection(self,priority,ping_f,timeout):
        self.set_ping_f(ping_f)
        self.set_timeout(timeout)
        self.start_monitor()
        time.sleep(5)
        if priority:#true runs recv first
            self.send_command("recv")
            time.sleep(timeout+3)
            self.send_command("ping")
        elif not priority:#true runs ping first
            self.send_command("ping")
            time.sleep(timeout+3)
            self.send_command("recv")
        time.sleep(timeout+3)
        self.stop_monitor()
            