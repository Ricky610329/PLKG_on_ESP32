"""
Error correction code

BCH
"""
import bchlib
import random
import math

BCH_POLYNOMIAL = 501
BCH_BITS = 8

def bit_flip(binary):
    output = ''
    for i in range(len(binary)):
        if random.randint(0,10) == 4:
            if binary[i] == "0":
                output = output + "1"
            if binary[i] == "1":
                output = output + "0"
        else:
            output = output + binary[i]
    return output

#generate random sequence for bch code
def rand_sequence(num):
    output = ''
    for i in range(num):
        sixteen_bit = random.randint(0, 62235)
        output = output + '{0:016b}'.format(sixteen_bit)
    return output

#changing 0/1 sequence to byte
def binary_byte_convertor(data):
    output = b''
    index = 0
    
    if len(data) % 16 != 0:
        print("data length must be multiples of 16")
        return b''
    
    for index in range(len(data)//16):
        bdata = data[16*index:16*(index+1)]
        output = output + int(bdata,2).to_bytes(2,"big")
    
    return output

#changing byte to 0/1 sequence
def byte_binary_convertor(data):
    output = ''
    index = 0
    if len(data) % 2 != 0:
        print("data length must be multiples of 2")
        return
    
    for index in range(len(data)//2):
        bdata = data[2*index:2*(index+1)]
        binary = int.from_bytes(bdata,"big")
        output = output + '{0:016b}'.format(binary)

    return output

#run xor
def run_xor(sequence1,sequence2):
    small = min(len(sequence1),len(sequence2))
    output = ''
    for i in range(small):
        if sequence1[i] == sequence2[i]:
            output = output + '0'
        else:
            output = output + '1'
    output = output + sequence1[small:] + sequence2[small:]
    return output

#check if the data is hte same
def check_same(sequence1,sequence2):
    flag = True
    count = 0
    for i in range(len(sequence1)):
        if sequence1[i] != sequence2[i]:
            flag = False
            count += 1
    print(count)
    if flag:
        print("same")
    else:
        print("not the same")
    return flag

def BCH_gen():
    bch = bchlib.BCH(BCH_POLYNOMIAL,BCH_BITS)
    data = rand_sequence(1)
    bytedata = binary_byte_convertor(data)
    trans_data = bytedata + bch.encode(bytedata)
    presentation = byte_binary_convertor(trans_data)
    return presentation

#bch system
def reconciliation_encode(q_result):
    miss = 16*math.ceil(len(q_result)/16)-len(q_result)
    for _ in range(miss):
        q_result = q_result +"0"
    length_ecc = math.ceil(len(q_result)/80)
    ecc_code = ''
    for _ in range(length_ecc):
        ecc_code = ecc_code + BCH_gen()
    xor_result = run_xor(ecc_code,q_result)
    return xor_result

def reconciliation_decode(q_result,re_result):
    bch = bchlib.BCH(BCH_POLYNOMIAL,BCH_BITS)
    length_ecc = math.ceil(len(q_result)/80)
    error_data = binary_byte_convertor(run_xor(q_result,re_result))
    output = ''
    for i in range(length_ecc):
        fix_data = bch.decode(error_data[10*i:10*i+10][:2],error_data[10*i:10*i+10][2:])
        output = output + byte_binary_convertor(fix_data[1])+byte_binary_convertor(fix_data[2])
    return run_xor(re_result,output)[:len(q_result)]
    

'''
for i in range(16):
    print(len(binary_byte_convertor(rand_sequence(1))))
'''