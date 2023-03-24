from datastream import chat
from datastream import rssi_interface as ri
import time

pi_1 = chat.chat_manager('192.168.0.143')
pi_2 = chat.chat_manager('192.168.0.192')
esp = ri.rssi_massive_collection('COM5',115200)

pi_1.chat_init()
pi_2.chat_init()
a = 'q'
while a != 's':
    a = input('input start >>> ')

pi_1.send('s')
pi_2.send('s')


esp.csv_setup("eve3_2m")
esp.start_monitor()
start = time.time()
while time.time() - start < 30:
    esp.csv_save()
    time.sleep(5)
esp.start_monitor()
esp.csv_close()