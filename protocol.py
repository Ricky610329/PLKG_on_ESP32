import datastream.interface as interface
import datastream.load as load
import plkg.greycode_quantization as quan
import plkg.ecc as ecc

magic = True

#setting up device
esp0 = interface.com_esp('/dev/ttyUSB0',115200)

#channel probing
esp0.run_collection(magic,1,10)#manage the order pf probing
csi_data = esp0.aquire_csi()

#save csi data
interface.savetocsv("alice",csi_data)

#quantization
csi_average = quan.average(load.transform(csi_data))
quantization_result = quan.quantization_1(csi_average,2,13)

#information reconciliation
if magic:
    ecc.reconciliation_encode(quantization_result)
else:
    ecc.reconciliation_decode(quantization_result,reconcilation_result)

