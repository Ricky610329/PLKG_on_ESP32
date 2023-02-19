"""
Error correction code

BCH
"""
import bchlib
import random

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
    if len(sequence1) != len(sequence2):
        print("Data must have same length")
        return ''
    output = ''
    for i in range(len(sequence1)):
        if sequence1[i] == sequence2[i]:
            output = output + '0'
        else:
            output = output + '1'




def gen_BCH_code(coefficient):
    pass



for i in range(16):
    print(len(binary_byte_convertor(rand_sequence(1))))