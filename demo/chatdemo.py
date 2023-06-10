from datastream import chat
import time
import threading

def show(chat):
    while True:
        time.sleep(0.3)
        message = chat.read_queue()
        if len(message)>0:
            print(message)
Alice = chat.chat("192.168.0.143")#填彼此的IP
Alice.chat_init()
show_thread = threading.Thread(target=show,args=(Alice,))
show_thread.start()
while True:
    Alice.send(input('>>'))