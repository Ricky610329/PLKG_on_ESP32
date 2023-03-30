import sys
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
        self.plkg_product = {
            'iot':False,
            'uav':False
        }
    def excute_send(self):
        input_text = COMMAND_SEND + self.send_text_console.toPlainText()
        d_index = self.data_direction_type.currentIndex()
        self.send_text_console.setText('')
        self.system_prompt_console.append(prompt_action + "data transimission direction <" + self.data_direction_type.currentText() + ">")
        try:
            if d_index == 0:
                self.data_exchange.send('uav',input_text)
            elif d_index == 1:
                self.data_exchange.send('iot',input_text)
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
            self.monitor_console_stop()
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
            self.monitor_console_run()
            self.data_exchange.send('uav',COMMAND_CONFIRM+'u'+self.data_exchange.link_table['iot_ip'])
            self.data_exchange.send('iot',COMMAND_CONFIRM+'i'+self.data_exchange.link_table['uav_ip'])
        else:
            self.system_prompt_console.append(prompt_fail + "system initialization failed\ncheck:\n - raspberry pi\n - IP/port\n - ESP32")
            return

    def monitor_console(self,target):
        if target == 'uav':
            console = self.drone_console
        elif target == 'iot':
            console = self.iot_console
        console.setText()
        while self.monitor_run:
            time.sleep(0.1)
            output = self.data_exchange.read(target)
            if output[:5] == COMMAND_PLKG:
                self.plkg_product[target] = output
            else:
                console.append(output)#can change to insertplaintext
            
    
    def monitor_eve(self):
        pass

    def monitor_console_run(self):
        self.monitor_task['uav'] = threading.Thread(target= self.monitor_console,args = ('uav',))
        self.monitor_task['iot'] = threading.Thread(target= self.monitor_console,args = ('iot',))
        self.monitor_task['eve'] = threading.Thread(target= self.monitor_eve)
        self.monitor_task['uav'].start()
        self.monitor_task['iot'].start()
        #self.monitor_task['eve'].start()
    

    def monitor_console_stop(self):
        self.monitor_task['uav'].join()
        self.monitor_task['iot'].join()
        #self.monitor_task['eve'].join()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = plkg_main_window()
    myWin.show()
    sys.exit(app.exec_())