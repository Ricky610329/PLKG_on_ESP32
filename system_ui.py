import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from IoD_UI.uiv2 import *
import time
  
class plkg_main_window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(plkg_main_window, self).__init__(parent)
        self.setupUi(self)
        self.send_data_buttom.clicked.connect(self.excute_send)
        self.run_plkg.clicked.connect(self.excute_plkg)
        self.check_system.clicked.connect(self.excute_check)
        self.settings_confirm.clicked.connect(self.excute_confirm)
    def excute_send(self):
        pass
    def excute_plkg(self):
        pass
    def excute_check(self):
        pass
    def excute_confirm(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = plkg_main_window()
    myWin.show()
    sys.exit(app.exec_())