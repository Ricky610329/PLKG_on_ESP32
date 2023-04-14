from datastream import chat
from uav_system import uav_system
import time
from plkg import aes

COMMAND_PLKG = "$PLKG"
COMMAND_SEND = "$SEND"
COMMAND_CHECK = "$CHEC"
COMMAND_CONFIRM = "$CONF"
COMMAND_LISTEN = "$LISN"

AES_ON = "$ON"
AES_OFF = "$OF"

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

            if command[5:8] == AES_ON:
                outputtext = ''
                outputtext = aes.encrypt(command[8:].encode('utf-8'),uav_interface.plkg_manager.key)
                uav_interface.uav_chat.send(outputtext)
                gcs_chat.send("sending:\n"+str(outputtext))
            
            elif command[5:8] == AES_OFF:
                gcs_chat.send("sending:\n"+command[8:])
                uav_interface.uav_chat.send(command[8:])

        elif command[:5] == COMMAND_LISTEN:
            time.sleep(0.5)
            if command[5:8] == AES_ON:
                gcs_chat.send_original(aes.decrypt(uav_interface.uav_chat.read_queue().decode('utf-8'),uav_interface.plkg_manager.key))
            if command[5:8] == AES_OFF:
                gcs_chat.send_original(uav_interface.uav_chat.read_queue())
        elif command[:5] == COMMAND_PLKG:
            uav_interface.run_plkg()
            #time.sleep(30)
            gcs_chat.send(', '.join((str(i) for i in uav_interface.get_plkg_data('average_result')))+'\n')
            gcs_chat.send((uav_interface.get_plkg_data('quan_result'))+'\n')
            gcs_chat.send((uav_interface.get_plkg_data('key_result'))+'\n')