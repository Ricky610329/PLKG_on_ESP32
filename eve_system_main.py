from datastream import chat
from uav_system_eve import uav_system
import time
from plkg import aes

COMMAND_PLKG = "$PLKG"
COMMAND_SEND = "$SEND"
COMMAND_CHECK = "$CHEC"
COMMAND_CONFIRM = "$CONF"
COMMAND_LISTEN = "$LISN"

AES_ON = "$ON"
AES_OFF = "$OF"


class evesdropper:
    def __init__(self,uav_ip,iot_ip,comport):
        self.command = ''
        self.uav_ip = uav_ip
        self.iot_ip = iot_ip
        self.comport =comport
        self.senddata = ''
        self.eve_system =  uav_system(self.uav_ip,self.iot_ip)


    def main(self):
        self.eve_system.plkg_init(self.comport)
        while True:
            if self.command == COMMAND_CHECK:
                self.senddata = "Check received"
                self.command = ''


            elif self.command[:5] == COMMAND_LISTEN:
                time.sleep(0.5)
                if self.command[5:8] == AES_ON:
                    try:
                        self.senddata = aes.decrypt(self.eve_system.uav_chat.read_queue().decode('utf-8'),self.eve_system.plkg_manager.key)
                    except:
                        pass
                    try:
                        self.senddata = aes.decrypt(self.eve_system.iot_chat.read_queue().decode('utf-8'),self.eve_system.plkg_manager.key)
                    except:
                        pass
                elif self.command[5:8] == AES_OFF:
                    try:
                        self.senddata = self.eve_system.uav_chat.read_queue()
                    except:
                        pass
                    try:
                        self.senddata = self.eve_system.iot_chat.read_queue()
                    except:
                        pass
                self.command = ''
            elif self.command[:5] == COMMAND_PLKG:
                print("in")
                self.eve_system.run_plkg()
                #time.sleep(30)
                self.senddata = ', '.join((str(i) for i in self.eve_system.get_plkg_data('average_result')))+'\n' + self.eve_system.get_plkg_data('quan_result')+'\n'+self.eve_system.get_plkg_data('key_result')+'\n'
                self.command = ''