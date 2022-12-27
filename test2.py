import loadcsv

rows = loadcsv.gray_code_gen(4)
for i in rows:
    print(i)