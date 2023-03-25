from datastream import chat

pi1 = chat.chat_manager("192.168.0.143",4000)
pi2 = chat.chat_manager("192.168.0.192")

pi1.chat_init()
pi2.chat_init()

while True:
    out = input("send>>")
    if out[0] == '1':
        pi1.send(out)
    elif out[0] == '2':
        pi2.send(out)
    
    x = pi1.read_queue()
    if x != b'':
        print(x)
    x = pi2.read_queue()
    if x != b'':
        print(x)