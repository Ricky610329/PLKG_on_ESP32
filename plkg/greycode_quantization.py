import copy


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


#output a string that is hte quantization result
def quantization_1(datas,Nbits,inbits):
    count = 0
    data = copy.deepcopy(datas)
    datalen = len(data)
    gray = gray_code_gen(Nbits)
    data.sort(key = lambda s: s[1])
    for i in range(2**Nbits):
        for j in range(inbits):
            data[count].append(gray[i])
            count += 1
            if not count < datalen :
                data.sort(key = lambda t: t[0])
                output = ''
                for x in range(len(data)):
                    output = output+data[x][2]
                return output