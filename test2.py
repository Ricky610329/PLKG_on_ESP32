import bchlib
import random

bch = bchlib.BCH(529,46)
ecc = bch.encode(b'a')
print()
a = ['1' for _ in range(104)]
b = ['0' for _ in range(104)]
a.extend(b)
random.shuffle(a)
a=''.join(a)
