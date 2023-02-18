"""
Error correction code

BCH
"""
import bchlib
import random



#generate random sequence for bch code
def rand_sequence(coefficient):
    output = ''
    for i in range(coefficient):
        sixteen_bit = random.randint(0, 62235)
        output = output + int(sixteen_bit,2).to_bytes(2,"big")
    return output


def gen_BCH_code(coefficient):
    pass

#'{0:016b}'.format(sixteen_bit)
#int.from_bytes(byte,"big")
#int(txt,2).to_bytes(2,"big")

def key_xor_ecc(key):
    
    output = ''

    key_len = len(key)
    co = key_len//16 + 1
    
    for _ in range(co*16-key_len):
        key = key + '0'
    

    ecc_code = rand_sequence(co)

    for i in range(co):
        
        ecc_code[16*i:16*i + 16]
        


a="11111111111111111001"
b="11111111111111111111"
y=int(a,2) ^ int(b,2)
print('{0:016b}'.format(y))