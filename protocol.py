import interface
import time


esp0 = interface.com_esp('COM5',115200)

esp0.start_monitor()
time.sleep(10)
esp0.send_command("recv")
time.sleep(15)
esp0.send_command("ping")
time.sleep(15)
interface.savetocsv(esp0.aquire_csi())

"""talk = chat.chat("192.168.0.105")
talk.init()

while True:
    txt = input("send>>>")
    talk.send(txt)"""

#print(certificate.gen_certificate())