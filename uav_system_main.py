import system_ui
from datastream import chat
from uav_system import uav_system

COMMAND_PLKG = "$PLKG"
COMMAND_SEND = "$SEND"
COMMAND_CHECK = "$CHEC"
COMMAND_CONFIRM = "$CONF"


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
    uav_interface = uav_connection(gcs_chat)
    uav_interface.plkg_init()
    while True:
        #寫工作任務，主程式部分需要完成eve的系統，但可以先進行實測。
        pass
