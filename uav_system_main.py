import system_ui
from datastream import chat
from uav_system import uav_system
import time

COMMAND_PLKG = "$PLKG"
COMMAND_SEND = "$SEND"
COMMAND_CHECK = "$CHEC"
COMMAND_CONFIRM = "$CONF"
COMMAND_LISTEN = "$LISN"


def ui_connection():
    gcs_ip = input("Input IP >>>")
    gcs_port = int(input("Input Port >>>"))
    return chat.chat_manager(gcs_ip,gcs_port)

def uav_connection(gcs_chat):
    gcs_chat.send("waiting for gcs")
    command = ''
    while True:
        command = gcs_chat.read_queue().decode('utf-8')
        if command[:5] == COMMAND_CONFIRM:
            break
    gcs_chat.send("conneting to "+ command[6:])
    return uav_system(command[6:],command[5])




if __name__ == "__main__":
    gcs_chat = ui_connection()
    gcs_chat.chat_init()
    uav_interface = uav_connection(gcs_chat)
    uav_interface.plkg_init()
    while True:
        command = gcs_chat.read_queue().decode('utf-8')
        gcs_chat.send(uav_interface.uav_chat.read_queue().decode('utf-8'))
        if command[:5] == COMMAND_CHECK:
            gcs_chat.send("Check received")
        elif command[:5] == COMMAND_SEND:
            uav_interface.uav_chat.send(command[5:])
            gcs_chat.send("sending:"+command[5:])
        elif command[:5] == COMMAND_LISTEN:
            time.sleep(0.5)
            gcs_chat.send(uav_interface.uav_chat.read_queue().decode('utf-8'))
        elif command[:5] == COMMAND_PLKG:
            uav_interface.run_plkg()
            #time.sleep(30)
            gcs_chat.send(', '.join((str(i) for i in uav_interface.get_plkg_data('average_result')))+'\n')
            gcs_chat.send((uav_interface.get_plkg_data('quan_result'))+'\n')
            gcs_chat.send((uav_interface.get_plkg_data('key_result'))+'\n')