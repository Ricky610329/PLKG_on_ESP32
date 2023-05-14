from datastream import chat
import threading
import time
def show(x):
    while True:
        print(x.read_queue())
        time.sleep(0.3)
agent = chat.chat_manager('192.168.0.162')

agent.chat_init()
threading.Thread(target=show,args=(agent,))
while True:
    agent.send(input(">>>"))