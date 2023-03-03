from datastream import chatv2
import time

Alice = chatv2.chat_manager()
Alice.chat_init()
Alice.receive_start()
while True:
    time.sleep(1)
    Alice.sendto("hi klla;skjf;asjfld;")
    print(Alice.pop(),end='')
Alice.receive_stop()