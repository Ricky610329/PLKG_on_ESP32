import datastream.interface as interface
import datastream.load as load
import plkg.greycode_quantization as quan

esp0 = interface.com_esp('/dev/ttyUSB0',115200)

esp0.run_collection(True,1,10)
data = esp0.aquire_csi()

interface.savetocsv("test0_b",data)

data = quan.average(load.transform(data))
data = quan.quantization_1(data,4,4)
for i in range(len(data)):
    print(data[i][2],end="")

