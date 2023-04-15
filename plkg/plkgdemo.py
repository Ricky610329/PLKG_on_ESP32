import datastream.csi_interface as csi_interface
import datastream.load as load
import plkg.greycode_quantization as quan
import plkg.ecc as ecc
import time
import plkg.sha256 as sha256
class end_device:
    def __init__(self,device_tag):
        self.device_tag = device_tag
        self.esp0 = csi_interface.com_esp('/dev/ttyUSB0',115200)#setting up device
        if device_tag == 'U':
            self.magic = True
        elif device_tag == 'I':
            self.magic = False
        
        self.reconciliation_result = ''
        #csi average
        self.csi_average = ''

        #plkg parameter
        self.quantization_result = ''
        self.key = b''

        #data exchange system
        self.chatmanager = False

        #save parameter
        self.save = False
        self.filename = 'filename'

    def set_chatmanager(self,chatmanager):
        self.chatmanager = chatmanager
        
    def save_probing_result(self,filename):
        self.save = True
        self.filename = filename

    def time_synchronize(self):
        if not self.chatmanager:
            print("Error: need to assign chatmanager")
            return False
        if self.magic:
            ack = 'FAIL'
            while ack != '-check':
                self.chatmanager.send_line('-check')
                time.sleep(0.5)
                ack = self.chatmanager.pop_line()
            time.sleep(0.5)
            self.chatmanager.send_line('-bang')
            self.chatmanager.queue_clear()
            return True
        elif not self.magic:
            ack = 'FAIL'
            while ack != '-check':
                ack = self.chatmanager.pop_line()
                if ack == '-check':
                    self.chatmanager.send_line('-check')
            self.chatmanager.queue_clear()
            while self.chatmanager.pop_line() != '-bang':
                pass
            self.chatmanager.queue_clear()
            return True


    def channel_probing(self):
        self.esp0.run_collection(self.magic,1,10)#manage the order pf probing
        if self.save:
            csi_interface.savetocsv(self.filename,self.esp0.aquire_csi())
        self.save = False
        
    def quantization(self):
        csi_data = self.esp0.aquire_csi()
        self.csi_average = quan.average(load.transform(csi_data))
        self.quantization_result = quan.quantization_1(self.csi_average,2,13)
    
    def information_reconciliation(self):
        if self.magic:
            time.sleep(0.5)
            ecc_code = ecc.reconciliation_encode(self.quantization_result)
            self.chatmanager.send_line(ecc_code)
            self.reconciliation_result = self.quantization_result
        elif not self.magic:
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
