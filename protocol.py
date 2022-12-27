import interface
import time
import loadcsv


esp0 = interface.com_esp('/dev/ttyUSB0',115200)

esp0.run_collection(True,1,10)
data = esp0.aquire_csi()
interface.savetocsv("test0_b",data)
data = loadcsv.average(loadcsv.transform(data))
data = loadcsv.quantization_1(data,4,4)
for i in range(len(data)):
    print(data[i][2],end="")

"""talk = chat.chat("192.168.0.105")
talk.init()

while True:
    txt = input("send>>>")
    talk.send(txt)"""

#print(certificate.gen_certificate())