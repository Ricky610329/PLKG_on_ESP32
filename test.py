import numpy as np
import plkg.greycode_quantization as quan
import csv
import plkg.ecc as ecc

def compare(data1,data2,bit,inbit):
    for sample1,sample2 in zip(data1,data2):
        gen1 = quan.quantization_1(sample1,bit,inbit)
        gen2 = quan.quantization_1(sample2,bit,inbit)
        re_data = ecc.reconciliation_encode(gen1)
        fix_data = ecc.reconciliation_decode(gen2,re_data)
        ecc.check_same(gen1,fix_data)


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

compare(pi1,pi2,2,13)