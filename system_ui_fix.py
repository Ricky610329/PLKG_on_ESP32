import sys
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication
from IoD_UI.uiv2 import *
from m_chat import multi_chat
import time
import threading

COMMAND_PLKG = "$PLKG"
COMMAND_SEND = "$SEND"
COMMAND_CHECK = "$CHEC"
COMMAND_CONFIRM = "$CONF"

prompt_action = '[ACTION]'
prompt_status = '[STATUS]'
prompt_fail = '[FAIL]'
prompt_success = '[SUCCESS]'

class monitorConsole(QThread):

    trigger = pyqtSignal(str)

    def __init__(self,data_exchange,target,text):
        super().__init__()
        self.data_exchange = data_exchange
        self.target = target
        self.text = text
    def run(self):
        while True:
            time.sleep(0.5)
            output = self.data_exchange.read(self.target)
            self.text[self.target] = self.text[self.target] + output
            self.trigger.emit(output)



class plkg_main_window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(plkg_main_window, self).__init__(parent)
        #super(multi_chat, self).__init__(parent)
        self.setupUi(self)
        self.send_data_buttom.clicked.connect(self.excute_send)
        self.run_plkg.clicked.connect(self.excute_plkg)
        self.check_system.clicked.connect(self.excute_check)
        self.settings_confirm.clicked.connect(self.excute_confirm)
        self.data_exchange = multi_chat()
        self.monitor_run = False
        self.monitor_task = {
            'uav':False,
            'iot':False,
            'eve':False
        }
        self.text = {
            'iot':'',
            'uav':''
        }
    def excute_send(self):
        input_text = COMMAND_SEND + self.send_text_console.toPlainText()
        d_index = self.data_direction_type.currentIndex()
        self.send_text_console.setText('')
        self.system_prompt_console.append(prompt_action + "data transimission direction <" + self.data_direction_type.currentText() + ">")
        try:
            if d_index == 0:
                self.data_exchange.send('uav',COMMAND_SEND + input_text)
            elif d_index == 1:
                self.data_exchange.send('iot',COMMAND_SEND + input_text)
            self.system_prompt_console.append(prompt_success + "send command success...")
        except:
            self.system_prompt_console.append(prompt_fail + "send command fail...\ncheck:\n - settings\n - rasspberry connection")
    def excute_plkg(self):
        try:
            self.data_exchange.send('uav',COMMAND_PLKG)
            self.data_exchange.send('iot',COMMAND_PLKG)
            self.system_prompt_console.append(prompt_success + "run plkg command success...")
        except:
            self.system_prompt_console.append(prompt_fail + "run plkg command fail...\ncheck:\n - settings\n - rasspberry connection")
    def excute_check(self):
        try:
            self.data_exchange.send('uav',COMMAND_CHECK)
            self.data_exchange.send('iot',COMMAND_CHECK)
            self.system_prompt_console.append(prompt_success + "check command success...")
        except:
            self.system_prompt_console.append(prompt_fail + "check command fail...\ncheck:\n - settings\n - rasspberry connection")
    def excute_confirm(self):
        if self.monitor_run:
            self.monitor_run = False
            #self.monitor_console_stop()
        self.data_exchange.chat_close()
        self.system_prompt_console.append(prompt_status + "socket close")
        self.system_prompt_console.append(prompt_action + "seting up IP/port of devices")
        
        
        try:
            self.data_exchange.set_parameter('uav_ip',self.drone_ip.text())
            self.data_exchange.set_parameter('iot_ip',self.iot_ip.text())
            self.data_exchange.set_parameter('eve_ip',self.eve_ip.text())
            self.data_exchange.set_parameter('eve_ip',self.gcs_ip.text())
            self.data_exchange.set_parameter('uav_port',int(self.drone_port.text()))
            self.data_exchange.set_parameter('iot_port',int(self.iot_port.text()))
            self.data_exchange.set_parameter('eve_port',int(self.eve_port.text()))
        except:
            self.system_prompt_console.append(prompt_fail +"input error")
            return
        


        if self.data_exchange.link_init():
            self.system_prompt_console.append(prompt_success +"system initialization success")
            self.monitor_run = True
            self.uavConsole = monitorConsole(self.data_exchange,'uav',self.text)
            self.iotConsole = monitorConsole(self.data_exchange,'iot',self.text)
            self.uavConsole.start()
            self.iotConsole.start()
            self.uavConsole.trigger.connect(self.appendUavConsole)
            self.iotConsole.trigger.connect(self.appendIotConsole)
            #self.monitor_console_run()
            self.data_exchange.send('uav',COMMAND_CONFIRM+'U'+self.data_exchange.link_table['iot_ip'])
            self.data_exchange.send('iot',COMMAND_CONFIRM+'I'+self.data_exchange.link_table['uav_ip'])
        else:
            self.system_prompt_console.append(prompt_fail + "system initialization failed\ncheck:\n - raspberry pi\n - IP/port\n - ESP32")
            return
    
    def appendUavConsole(self,text):
        if len(text) != 0:
            self.drone_console.append(text)
    def appendIotConsole(self,text):
        if len(text) != 0:
            self.iot_console.append(text)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = plkg_main_window()
    myWin.show()
    sys.exit(app.exec_())