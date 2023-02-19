import matplotlib.pyplot as plt
import numpy as np
import plkg.greycode_quantization as quan
import csv

def compare(data1,data2,bit,inbit):
    result = []
    for sample1,sample2 in zip(data1,data2):
        gen1 = quan.quantization_1(sample1,bit,inbit)
        gen2 = quan.quantization_1(sample2,bit,inbit)
        #print(len(gen1))
        #print(len(gen2))
        count=0
        for i in range(len(gen1)):
            if gen1[i]==gen2[i]:
                count+=1
        result.append(count/len(gen1))
    output = []
    for i in range(3):
        value = 0
        for j in range(3):
            value+=result[3*i+j]
        output.append(round(1-value/3,2))
    return output


pi1 = []
pi2 = []
for i in range(3):
    for j in range(3):
        file1 = "./dataset/pi1/"+ str(i+1)+"_"+str(j+1)+"_meter.csv"
        file2 = "./dataset/pi2/"+ str(i+1)+"_"+str(j+1)+"_meter.csv"
        pi1_hold = []
        with open(file1,'r',newline="") as csvfile1:
            file1_reader = csv.reader(csvfile1, delimiter=',')
            for rows in file1_reader:
                pi1_hold.append([int(rows[0]),float(rows[1])])
        pi1.append(pi1_hold)
        pi2_hold = []
        with open(file2,'r',newline="") as csvfile2:
            file2_reader = csv.reader(csvfile2, delimiter=',')
            for rows in file2_reader:
                pi2_hold.append([int(rows[0]),float(rows[1])])
        pi2.append(pi2_hold)

label = ['1 m','3 m','5 m']
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 12})
x = np.arange(len(label))
width = 0.2
m1 = compare(pi1,pi2,2,13)
m2 = compare(pi1,pi2,3,7)
m3 = compare(pi1,pi2,4,4)

plt.bar(x, m1, width, color='steelblue', label='2-bit',edgecolor = 'black',zorder=100)
plt.bar(x+width, m2, width, tick_label=label,color='skyblue', label='3-bit',edgecolor = 'black',zorder=100)
plt.bar(x+2*width, m3, width, color='azure', label='4-bit',edgecolor = 'black',zorder=100)
plt.ylabel('KDR')
plt.xlabel('Distance between UAV and IoT device (m)')
plt.legend(title = "Gray code",bbox_to_anchor=(1,1), loc='upper right')
plt.grid(linestyle = '--',zorder=0)
plt.show()