from datastream import chat
import time

Alice = chat.chat("192.168.0.143")
Alice.chat_init()
while True:
    time.sleep(1)
    Alice.send("Hi")
    print(Alice.read_queue())