from plkg import plkgdemo
from datastream import chat
import time
class uav_system:
    def __init__(self,target_ip,device_tag,eveip):
        self.uav_chat = chat.chat_manager(target_ip,4500)
        self.uav_chat.chat_init()
        time.sleep(0.1)
        if device_tag == 'U':
            self.eve_chat = chat.chat_manager(eveip,4501)
            self.eve_chat.send_init()
        elif device_tag == 'I':
            self.eve_chat = chat.chat_manager(eveip,4502)
            self.eve_chat.send_init()
        self.device_tag = device_tag
        self.plkg_manager = False
    def plkg_init(self):
        self.plkg_manager = plkgdemo.end_device(self.device_tag)
        self.plkg_manager.set_chatmanager(self.uav_chat,self.eve_chat)
    def run_plkg(self):
        self.plkg_manager.plkg()
    def get_plkg_data(self,type):
        if type == 'average_result':
            return self.plkg_manager.csi_average
        elif type == 'quan_result':
            return "Quantization result: " + self.plkg_manager.quantization_result
        elif type == 'key_result':
            return "Generate key: "+str(self.plkg_manager.key)