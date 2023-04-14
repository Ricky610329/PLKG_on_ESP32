import re
import matplotlib.pyplot as plt
example = r'''conneting to 192.168.0.143[0, 360.74434912095194], [1, 361.1929446915944], [2, 375.70547694436345], [3, 383.16376781049945], [4, 372.27720573334705], [5, 355.11933943470774], [6, 348.6082319565661], [7, 338.94428939949876], [8, 332.6668995527084], [9, 336.8678115458153], [10, 356.08753552310094], [11, 363.8543675688721], [12, 356.13895703845753], [13, 343.8084892409546], [14, 344.53601656551814], [15, 353.1099817796287], [16, 335.52327781287545], [17, 320.66695170184], [18, 331.78262403181776], [19, 337.27216280926143], [20, 336.8364088006594], [21, 332.5808899928323], [22, 324.54490008304157], [23, 344.9897759306786], [24, 369.1200505466134], [25, 373.6163564552177], [26, 367.43551332563294], [27, 378.93336946255107], [28, 384.71986375313594], [29, 383.1364334755244], [30, 385.630658541374], [31, 395.10121448408], [32, 395.1108580286653], [33, 390.9165607841185], [34, 391.60538838184635], [35, 395.8039427801824], [36, 404.35913015344624], [37, 398.5504923001477], [38, 399.0003216761373], [39, 403.35482840081056], [40, 408.76877721385796], [41, 420.88459643636605], [42, 425.82831194701095], [43, 419.0879624810398], [44, 408.26717937501917], [45, 404.0643051782592], [46, 404.4012593127464], [47, 407.2239321416427], [48, 415.47145982400514], [49, 420.35471268666856], [50, 412.22247036775366], [51, 404.60341035940945]
Quantization result: 01010111010101000000010101000001000000000000000001010111111111111111111110111111101010101010101010101010
Generate key: b"a:n\x84\x10'\xa7\xd4\x84\x1c\x8d\xb7\x98\x87\x96*\x9d\xdf#\x9f\xa7\xf8\xe2\xae\xb2\x93S)\x88\x8d\xe9\xc8"'''


def dataStringToNum(example_data):
    dataset = re.findall('\[.*?]',example_data)

    for index, item in enumerate(dataset):
        sub, amp = item[1:-1].split(', ')
        dataset[index] = [int(sub),float(amp)]
    
    for index, item in enumerate(dataset):
        dataset[index][0] = item[0] + 7
        if item[0] > 32:
            dataset[index][0] = item[0] + 1


    return list(zip(*dataset))


def setup():
    plt.figure(figsize=(16,4))

    axy = plt.gca()
    x_major_locator = plt.MultipleLocator(1)
    axy.xaxis.set_major_locator(x_major_locator)

    y_major_locator = plt.MultipleLocator(20)
    axy.yaxis.set_major_locator(y_major_locator)

    plt.xlabel('Subcarrier Index', size = 8)
    plt.ylabel('Amplitude', size = 8)
    plt.grid()
    plt.xticks(size = 8)
    plt.yticks(size = 8)

def draw(example_data):
    subAmp = dataStringToNum(example_data)
    plt.plot(subAmp[0],subAmp[1], marker='o')


setup()
draw(example)
plt.show()