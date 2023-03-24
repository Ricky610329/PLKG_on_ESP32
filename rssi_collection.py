from datastream import rssi_interface as ri
import time
from datastream import chat

esp = ri.rssi_massive_collection('/dev/ttyUSB0',115200)
sy = chat.chat_manager('')

sy.chat_init()

while sy.read_queue().decode('utf-8') != 's':
    print("waiting...")
    time.sleep(0.1)

esp.csv_setup("3_2m")
esp.start_monitor()
start = time.time()
while time.time() - start < 30:
    esp.csv_save()
    time.sleep(5)
esp.start_monitor()
esp.csv_close()
