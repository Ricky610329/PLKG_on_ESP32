import datastream.csi_interface as csi_interface
import datastream.load as load
import plkg.greycode_quantization as quan
import plkg.ecc as ecc
import time
import plkg.sha256 as sha256

class end_device:
    def __init__(self):
        self.comPort = "COM5"

        self.reconciliation_result = ''
        #csi average
        self.csi_average = ''

        #plkg parameter
        self.quantization_result = ''
        self.key = b''

        #data exchange system
        self.chatmanager = False

        self.save = False

    def setupEve(self,comPort):
        self.comPort = comPort
        self.esp0 = csi_interface.com_esp(comPort,115200)

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
    
    def channel_probing(self):
        self.esp0.set_ping_f(1)#manage the order pf probing
        self.esp0.set_timeout(4)
        self.esp0.start_monitor()
        time.sleep(2)
        self.esp0.send_command("recv")
        time.sleep(4+3)
        time.sleep(2)
        self.esp0.stop_monitor()
        if self.save:
            csi_interface.savetocsv(self.filename,self.esp0.aquire_csi())
        self.save = False
        
    def quantization(self):
        csi_data = self.esp0.aquire_csi()
        self.csi_average = quan.average(load.transform(csi_data))
        self.quantization_result = quan.quantization_1(self.csi_average,2,13)
    
    def information_reconciliation(self):
        reconcilation_result = "FAIL"
        while reconcilation_result == "FAIL":
            reconcilation_result = self.chatmanager.pop_line()
        self.reconciliation_result = ecc.reconciliation_decode(self.quantization_result,reconcilation_result)
    
    def privacy_amplification(self):
        self.key = sha256.sha_byte(self.reconciliation_result)

    def plkg(self):
        if self.time_synchronize():
            self.channel_probing()
            self.quantization()
            self.information_reconciliation()
            self.privacy_amplification()
            self.chatmanager.queue_clear()
        else:
            return b"FAIL"
        return self.key