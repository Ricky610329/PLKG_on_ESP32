# 基於實體層保密技術實現高安全無人機資料交換系統程式碼

作者：鄒穎麒    日期：2023/6/9

此文件整理了有關專本專題所使用的程式碼，為了方便使用者接下來自行更動，作者刪減掉程式碼中實際使用的部分，並重新挑整了部分的命名。請一定要熟悉class的使用。

**程式碼模組清單：**
* **datastream**：包含所有資料在不同介面之間交換的函式。ESP32的CSI資料透過serial的傳輸介面、樹梅派透過socket進行資料交換的傳輸介面。
* **IoD_UI**：專題呈現實作成果時所設計的使用者介面模組。透過Qtdesigner製作。
* **plkg**：實現plkg有關代碼及資料加密代碼。

**非模組部分：**
* 在demo資料夾中存放檔案皆為模組的基本功能展示，只需要將其拉到主資料夾中(也就是模組所在的資料夾中)就可以呈現其效果。
* 其餘沒有打包的外部程式為專題實作成果的展試檔。寫的時候比較隨興，建議未來使用者要建立成果於本研究之上時，使用所提供的三個模組重新構建自己的測試環境，以優化效能。

**環境：**
* python3.8
* 按裝包管理conda

## datastream
-------
### chat.py
用於在裝置之見建立socket進行資料交換，必須連到同一個網路下，將裝置在該網路的IP/PORT輸入後方可進行資料交換。(細節請看網路概論課本)

**需要模組：**
* socket
* threading
* re

程式碼說明：
|函式名稱|說明|
|----|----|
|```chat_manager(<string ip>,<int port>)```|兩台裝置皆輸入欲交換資料裝置的IP/PORT即可進行資料交換，預設PORT為5000。若想與同一台裝置建立兩條連線，請使用不同的PORT(網概)。|
|```chat_manager.receive_task()```|持續進行接收資料的工作|
|```chat_manager.recv_init()```|初始化資料接收功能|
|```chat_manager.send_init()```|初始化資料傳輸功能|
|```chat_manager.chat_init()```|同時初始化接收與傳輸功能|
|```chat_manager.close_socket()```|同時關閉接收、發送socket|
|```chat_manager.pop()```|FIFO的方式return第一個字符，回傳格式為utf-8碼|
|```chat_manager.pop_line()```|FIFO的方式return透過```chat_manager.send_line()```傳輸的連續資料，請避免使用"-end"，此為判斷結束符號。回傳格式為string|
|```chat_manager.read_queue()```|一次性讀取記憶體內所有的資料|
|```chat_manager.queue_clear()```|清除記憶體內所有累積資料|
|```chat_manager.send(<string message>)```|傳輸資料給接收方，會自動進行utf-8編碼|
|```chat_manager.send_line(<string message>)```|傳輸資料給接收方，接收方可以使用```chat_manager.pop_line()```去取得整段資料|
|```chat_manager.send_original(<utf-8 message>)```|接收utf-8編碼後直接傳輸|

基本功能展示:
```python
from datastream import chat
import time
import threading

def show(chat):
    while True:
        time.sleep(0.3)
        message = chat.read_queue()
        if len(message)>0:
            print(message.decode("utf-8"))


Alice = chat.chat("192.168.0.143")#填彼此的IP
Alice.chat_init()
show_thread = threading.Thread(target=show,args=(Alice,))
show_thread.start()

while True:
    Alice.send(input('>>'))
```
上面程式碼實現了同時進行資料收發，可以以此做為參考更動為你的設計。

### csi_interface.py
收集CSI資料時與ESP32進行資料交換的介面。同時在此處也實踐了Channel probing的介面，未來欲更動資料收集策略者請看此處。

**需要模組：**
* serial
* threading
* platform
* threading
* re
* csv