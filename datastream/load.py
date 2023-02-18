import csv
import re
import numpy as np
import math

SUBCARRIER = 64
NO_USE_SUB = [0 ,1 ,2 ,3 ,4 ,5 ,32 ,59 ,60 ,61 ,62 ,63 ,64 ,65 ,123 ,124 ,125 ,126 ,127 ,128 ,129 ,130 ,131 ,132 ,133 ,191]

def amplitude(x,y):
    return math.sqrt(x*x+y*y)

#take raw data from interface to editable form
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

#--------------------------------------------------------
