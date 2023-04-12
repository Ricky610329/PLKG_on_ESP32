from datastream import chat

class multi_chat:
    def __init__(self):
        self.link_table = {
            'uav_ip':False,
            'uav_port':False,
            'iot_ip':False,
            'iot_port':False,
            'eve_ip':False,
            'eve_port':False,
            'gcs_ip':False
        }
        self.chat = {
            'uav':False,
            'iot':False
        }
    def set_parameter(self,par_name,par_value):
        self.link_table[par_name] = par_value
    
    def link_init(self):
        self.chat['uav'] = chat.chat_manager(self.link_table['uav_ip'],self.link_table['uav_port'])
        self.chat['iot'] = chat.chat_manager(self.link_table['iot_ip'],self.link_table['iot_port'])
        try:
            self.chat['uav'].chat_init()
            self.chat['iot'].chat_init()
        except:
            return False
        return True
    
    def send(self,target,message):
        self.chat[target].send(message)

    def read(self,target):
        return self.chat[target].read_queue().decode('utf-8')
    
    def chat_close(self):
        try:
            self.chat['uav'].close_socket()
        except:
            pass
        try:
            self.chat['iot'].close_socket()
        except:
            pass