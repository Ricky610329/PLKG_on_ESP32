import datastream.csi_interface as csi_interface
import datastream.load as load
import plkg.greycode_quantization as quan
import plkg.ecc as ecc
import time
import plkg.sha256 as sha256

class evesdropper:
    def __init__(self):
        self.comPort = "COM5"

    def setupEve(self,comPort):
        self.comPort = comPort
        self.esp0 = csi_interface.com_esp(comPort,115200)

        self.reconciliation_result = ''
        #csi average
        self.csi_average = ''

        #plkg parameter
        self.quantization_result = ''
        self.key = b''

        #data exchange system
        self.chatmanager = False

    def set_chatmanager(self,chatmanager):
        self.chatmanager = chatmanager
        
    def save_probing_result(self,filename):
        self.save = True
        self.filename = filename

    def time_synchronize(self):
        if not self.chatmanager:
            print("Error: need to assign chatmanager")
            return False
        else:
            ack = 'FAIL'
            while ack != '-check':
                ack = self.chatmanager.pop_line()
            self.chatmanager.queue_clear()
            while self.chatmanager.pop_line() != '-bang':
                pass
            self.chatmanager.queue_clear()
            return True