import csv
import re
import numpy as np
import math
import time

SUBCARRIER = 64
NO_USE_SUB = [0 ,1 ,2 ,3 ,4 ,5 ,32 ,59 ,60 ,61 ,62 ,63 ,64 ,65 ,123 ,124 ,125 ,126 ,127 ,128 ,129 ,130 ,131 ,132 ,133 ,191]

def amplitude(x,y):
    return math.sqrt(x*x+y*y)

def transform(rows):
    output = []
    for row in rows:
        raw = re.search("\[.*?\]",row).group()
        raw = raw[1:-1].split(",")
        flst = [float(item) for item in raw]
        flst_clean = []
        for i in range(SUBCARRIER):
            if not i in NO_USE_SUB:
                flst_clean.append(amplitude(flst[2*i],flst[2*i+1]))
        output.append(np.array(flst_clean))
    return output

#retrun clean list 
def load(filename):
    with open(filename,newline='') as csvfile:
        rows = csv.reader(csvfile)
        return transform(rows)


def average(sample):
    phase1 = sample[0]
    for csi in range(1,len(sample)):
        phase1 = phase1 + sample[csi]
    order_a = []
    for i in range(len(phase1)):
        order_a.append([i,phase1[i]])
    return order_a


def swap(bit,x):
    if bit == '0' and x%2 == 0:
        return '1'
    if bit == '0' and x%2 == 1:
        return '0'
    if bit == '1' and x%2 == 0:
        return '0'
    if bit =='1' and x%2 == 1:
        return '1'

def gray_code_gen(Nbits):
    gray_sequence = []
    for i in range(2**Nbits):
        gray_sequence.append("")
    for code in range(Nbits):
        newbit = '0'
        count = 0
        x = 0
        for bit in range(2**Nbits):
            gray_sequence[bit] = newbit + gray_sequence[bit]
            count+=1
            if count == 2**(code):
                count = 0
                newbit = swap(newbit,x)
                x+=1
                
            
    return gray_sequence

            

def quantization_1(data,Nbits,inbits):
    count = 0
    datalen = len(data)
    gray = gray_code_gen(Nbits)
    data.sort(key = lambda s: s[1])
    for i in range(2**Nbits):
        for j in range(inbits):
            data[count].append(gray[i])
            count += 1
            if not count < datalen :
                data.sort(key = lambda t: t[0])
                return data
