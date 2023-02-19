import bchlib
from plkg import ecc



BCH_POLYNOMIAL = 451
BCH_BITS = 8
bch = bchlib.BCH(BCH_POLYNOMIAL,BCH_BITS)

data = ecc.rand_sequence(2)
print("original:",data)
bytedata = ecc.binary_byte_convertor(data)
trans_data = bytedata + bch.encode(bytedata)
presentation = ecc.byte_binary_convertor(trans_data) 
print("    send:",presentation)
error_data = ecc.bit_flip(presentation)
print("  modify:",error_data)
fix_data = bch.decode(ecc.binary_byte_convertor(error_data)[:4],ecc.binary_byte_convertor(error_data)[4:])
print("     fix:",ecc.byte_binary_convertor(fix_data[1])+ecc.byte_binary_convertor(fix_data[2]))