from plkg import eveplkg
from datastream import chat

class uav_system:
    def __init__(self,uav_ip,iot_ip):
        self.uav_chat = chat.chat_manager(uav_ip,4501)
        self.uav_chat.recv_init()
        self.iot_chat = chat.chat_manager(iot_ip,4502)
        self.iot_chat.recv_init()
        self.plkg_manager = False
    def plkg_init(self,comPort):
        self.plkg_manager = eveplkg.end_device()
        self.plkg_manager.setupEve(comPort)
        self.plkg_manager.set_chatmanager(self.uav_chat)
    def run_plkg(self):
        self.plkg_manager.plkg()
    def get_plkg_data(self,type):
        if type == 'average_result':
            return self.plkg_manager.csi_average
        elif type == 'quan_result':
            return "Quantization result: " + self.plkg_manager.quantization_result
        elif type == 'key_result':
            return "Generate key: "+str(self.plkg_manager.key)