from plkg import plkg
from datastream import chat

class uav_system:
    def __init__(self,target_ip,device_tag):
        self.uav_chat = chat.chat_manager(target_ip,4500)
        self.device_tag = device_tag
        self.plkg_manager = False
    def plkg_init(self):
        self.plkg_manager = plkg.end_device(self.device_tag)
        self.plkg_manager.set_chatmanager(self.uav_chat)
    def run_plkg(self):
        self.plkg_manager.plkg()
    def get_plkg_data(self,type):
        if type == 'average_result':
            return self.plkg_manager.csi_average
        elif type == 'quan_result':
            return self.plkg_manager.quantization_result
        elif type == 'key_result':
            return self.plkg_manager.key