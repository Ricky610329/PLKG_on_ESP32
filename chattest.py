from datastream import chat
import threading
import time
def show(x):
    while True:
        y = x.read_queue()
        if len(y) != 0:
            print(y.decode('utf-8'))
        time.sleep(0.3)
agent = chat.chat_manager('192.168.0.162')

agent.chat_init()
th = threading.Thread(target=show,args=(agent,))
th.start()
while True:
    agent.send(input())