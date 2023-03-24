# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unfinish.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 520)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.system_tab = QtWidgets.QTabWidget(self.centralwidget)
        self.system_tab.setObjectName("system_tab")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.control_pannel_frame = QtWidgets.QFrame(self.tab)
        self.control_pannel_frame.setAutoFillBackground(False)
        self.control_pannel_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.control_pannel_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.control_pannel_frame.setObjectName("control_pannel_frame")
        self.send_data_buttom = QtWidgets.QPushButton(self.control_pannel_frame)
        self.send_data_buttom.setGeometry(QtCore.QRect(490, 240, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.send_data_buttom.setFont(font)
        self.send_data_buttom.setObjectName("send_data_buttom")
        self.data_direction_type = QtWidgets.QComboBox(self.control_pannel_frame)
        self.data_direction_type.setGeometry(QtCore.QRect(180, 240, 141, 24))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.data_direction_type.setFont(font)
        self.data_direction_type.setObjectName("data_direction_type")
        self.data_direction_type.addItem("")
        self.data_direction_type.addItem("")
        self.send_text_console = QtWidgets.QTextEdit(self.control_pannel_frame)
        self.send_text_console.setGeometry(QtCore.QRect(10, 270, 1051, 71))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setBold(False)
        font.setWeight(50)
        self.send_text_console.setFont(font)
        self.send_text_console.setObjectName("send_text_console")
        self.line = QtWidgets.QFrame(self.control_pannel_frame)
        self.line.setGeometry(QtCore.QRect(10, 340, 1051, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.encryption_type = QtWidgets.QComboBox(self.control_pannel_frame)
        self.encryption_type.setGeometry(QtCore.QRect(410, 240, 71, 24))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.encryption_type.setFont(font)
        self.encryption_type.setObjectName("encryption_type")
        self.encryption_type.addItem("")
        self.encryption_type.addItem("")
        self.data_direction_label = QtWidgets.QLabel(self.control_pannel_frame)
        self.data_direction_label.setGeometry(QtCore.QRect(10, 240, 161, 25))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.data_direction_label.setFont(font)
        self.data_direction_label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.data_direction_label.setToolTipDuration(1)
        self.data_direction_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.data_direction_label.setAutoFillBackground(False)
        self.data_direction_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.data_direction_label.setObjectName("data_direction_label")
        self.encryption_label = QtWidgets.QLabel(self.control_pannel_frame)
        self.encryption_label.setGeometry(QtCore.QRect(340, 240, 61, 25))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.encryption_label.setFont(font)
        self.encryption_label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.encryption_label.setToolTipDuration(1)
        self.encryption_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.encryption_label.setAutoFillBackground(False)
        self.encryption_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.encryption_label.setObjectName("encryption_label")
        self.system_prompt_console = QtWidgets.QTextBrowser(self.control_pannel_frame)
        self.system_prompt_console.setGeometry(QtCore.QRect(280, 380, 781, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setBold(False)
        font.setWeight(50)
        self.system_prompt_console.setFont(font)
        self.system_prompt_console.setObjectName("system_prompt_console")
        self.system_prompt = QtWidgets.QLabel(self.control_pannel_frame)
        self.system_prompt.setGeometry(QtCore.QRect(280, 350, 161, 25))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.system_prompt.setFont(font)
        self.system_prompt.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.system_prompt.setToolTipDuration(1)
        self.system_prompt.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.system_prompt.setAutoFillBackground(False)
        self.system_prompt.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.system_prompt.setObjectName("system_prompt")
        self.layoutWidget = QtWidgets.QWidget(self.control_pannel_frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 1051, 194))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.drone_console = QtWidgets.QTextBrowser(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.drone_console.setFont(font)
        self.drone_console.setObjectName("drone_console")
        self.gridLayout_2.addWidget(self.drone_console, 0, 0, 1, 1)
        self.iot_console = QtWidgets.QTextBrowser(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.iot_console.setFont(font)
        self.iot_console.setObjectName("iot_console")
        self.gridLayout_2.addWidget(self.iot_console, 0, 1, 1, 1)
        self.eve_console = QtWidgets.QTextBrowser(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.eve_console.setFont(font)
        self.eve_console.setObjectName("eve_console")
        self.gridLayout_2.addWidget(self.eve_console, 0, 2, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.control_pannel_frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 1051, 27))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.drone_console_label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.drone_console_label.setFont(font)
        self.drone_console_label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.drone_console_label.setToolTipDuration(1)
        self.drone_console_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.drone_console_label.setAutoFillBackground(False)
        self.drone_console_label.setAlignment(QtCore.Qt.AlignCenter)
        self.drone_console_label.setObjectName("drone_console_label")
        self.gridLayout_3.addWidget(self.drone_console_label, 0, 0, 1, 1)
        self.iot_console_label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.iot_console_label.setFont(font)
        self.iot_console_label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.iot_console_label.setToolTipDuration(1)
        self.iot_console_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.iot_console_label.setAutoFillBackground(False)
        self.iot_console_label.setAlignment(QtCore.Qt.AlignCenter)
        self.iot_console_label.setObjectName("iot_console_label")
        self.gridLayout_3.addWidget(self.iot_console_label, 0, 1, 1, 1)
        self.eve_console_label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.eve_console_label.setFont(font)
        self.eve_console_label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.eve_console_label.setToolTipDuration(1)
        self.eve_console_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.eve_console_label.setAutoFillBackground(False)
        self.eve_console_label.setAlignment(QtCore.Qt.AlignCenter)
        self.eve_console_label.setObjectName("eve_console_label")
        self.gridLayout_3.addWidget(self.eve_console_label, 0, 2, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(self.control_pannel_frame)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 360, 251, 81))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.check_system = QtWidgets.QPushButton(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_system.sizePolicy().hasHeightForWidth())
        self.check_system.setSizePolicy(sizePolicy)
        self.check_system.setObjectName("check_system")
        self.gridLayout_4.addWidget(self.check_system, 0, 0, 1, 1)
        self.run_plkg = QtWidgets.QPushButton(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.run_plkg.sizePolicy().hasHeightForWidth())
        self.run_plkg.setSizePolicy(sizePolicy)
        self.run_plkg.setObjectName("run_plkg")
        self.gridLayout_4.addWidget(self.run_plkg, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.control_pannel_frame)
        self.system_tab.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.system_tab.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gcs_settings = QtWidgets.QGroupBox(self.tab_3)
        self.gcs_settings.setGeometry(QtCore.QRect(10, 339, 961, 111))
        self.gcs_settings.setObjectName("gcs_settings")
        self.gcs_ip = QtWidgets.QLineEdit(self.gcs_settings)
        self.gcs_ip.setGeometry(QtCore.QRect(100, 40, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setBold(False)
        font.setWeight(50)
        self.gcs_ip.setFont(font)
        self.gcs_ip.setText("")
        self.gcs_ip.setObjectName("gcs_ip")
        self.gcs_ip_label = QtWidgets.QLabel(self.gcs_settings)
        self.gcs_ip_label.setGeometry(QtCore.QRect(20, 40, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.gcs_ip_label.setFont(font)
        self.gcs_ip_label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.gcs_ip_label.setToolTipDuration(1)
        self.gcs_ip_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gcs_ip_label.setAutoFillBackground(False)
        self.gcs_ip_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.gcs_ip_label.setObjectName("gcs_ip_label")
        self.layoutWidget_5 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget_5.setGeometry(QtCore.QRect(10, 10, 1061, 321))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.layoutWidget_5)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.drone_settings = QtWidgets.QGroupBox(self.layoutWidget_5)
        self.drone_settings.setObjectName("drone_settings")
        self.drone_ip_label = QtWidgets.QLabel(self.drone_settings)
        self.drone_ip_label.setGeometry(QtCore.QRect(30, 80, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.drone_ip_label.setFont(font)
        self.drone_ip_label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.drone_ip_label.setToolTipDuration(1)
        self.drone_ip_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.drone_ip_label.setAutoFillBackground(False)
        self.drone_ip_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.drone_ip_label.setObjectName("drone_ip_label")
        self.drone_ip = QtWidgets.QLineEdit(self.drone_settings)
        self.drone_ip.setGeometry(QtCore.QRect(110, 80, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setBold(False)
        font.setWeight(50)
        self.drone_ip.setFont(font)
        self.drone_ip.setText("")
        self.drone_ip.setObjectName("drone_ip")
        self.gridLayout_8.addWidget(self.drone_settings, 0, 0, 1, 1)
        self.eve_settings = QtWidgets.QGroupBox(self.layoutWidget_5)
        self.eve_settings.setObjectName("eve_settings")
        self.eve_ip = QtWidgets.QLineEdit(self.eve_settings)
        self.eve_ip.setGeometry(QtCore.QRect(110, 80, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setBold(False)
        font.setWeight(50)
        self.eve_ip.setFont(font)
        self.eve_ip.setText("")
        self.eve_ip.setObjectName("eve_ip")
        self.eve_ip_label = QtWidgets.QLabel(self.eve_settings)
        self.eve_ip_label.setGeometry(QtCore.QRect(30, 80, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.eve_ip_label.setFont(font)
        self.eve_ip_label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.eve_ip_label.setToolTipDuration(1)
        self.eve_ip_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.eve_ip_label.setAutoFillBackground(False)
        self.eve_ip_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.eve_ip_label.setObjectName("eve_ip_label")
        self.gridLayout_8.addWidget(self.eve_settings, 0, 2, 1, 1)
        self.iot_settings = QtWidgets.QGroupBox(self.layoutWidget_5)
        self.iot_settings.setObjectName("iot_settings")
        self.iot_ip = QtWidgets.QLineEdit(self.iot_settings)
        self.iot_ip.setGeometry(QtCore.QRect(100, 80, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setBold(False)
        font.setWeight(50)
        self.iot_ip.setFont(font)
        self.iot_ip.setText("")
        self.iot_ip.setObjectName("iot_ip")
        self.iot_ip_label = QtWidgets.QLabel(self.iot_settings)
        self.iot_ip_label.setGeometry(QtCore.QRect(20, 80, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.iot_ip_label.setFont(font)
        self.iot_ip_label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.iot_ip_label.setToolTipDuration(1)
        self.iot_ip_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.iot_ip_label.setAutoFillBackground(False)
        self.iot_ip_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.iot_ip_label.setObjectName("iot_ip_label")
        self.gridLayout_8.addWidget(self.iot_settings, 0, 1, 1, 1)
        self.settings_confirm = QtWidgets.QPushButton(self.tab_3)
        self.settings_confirm.setGeometry(QtCore.QRect(980, 340, 91, 111))
        self.settings_confirm.setObjectName("settings_confirm")
        self.system_tab.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.system_tab, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.system_tab.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.send_data_buttom.setText(_translate("MainWindow", "Send"))
        self.data_direction_type.setItemText(0, _translate("MainWindow", "Drone to IoT Device"))
        self.data_direction_type.setItemText(1, _translate("MainWindow", "IoT Device to Drone"))
        self.encryption_type.setItemText(0, _translate("MainWindow", "<None>"))
        self.encryption_type.setItemText(1, _translate("MainWindow", "AES"))
        self.data_direction_label.setText(_translate("MainWindow", "Data Transmission Direction:"))
        self.encryption_label.setText(_translate("MainWindow", "Encryption"))
        self.system_prompt_console.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.system_prompt.setText(_translate("MainWindow", "System Prompt:"))
        self.drone_console.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'PMingLiU\'; font-weight:400;\"><br /></p></body></html>"))
        self.iot_console.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'PMingLiU\'; font-weight:400;\"><br /></p></body></html>"))
        self.eve_console.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'PMingLiU\'; font-weight:400;\"><br /></p></body></html>"))
        self.drone_console_label.setText(_translate("MainWindow", "Drone"))
        self.iot_console_label.setText(_translate("MainWindow", "IoT Devie"))
        self.eve_console_label.setText(_translate("MainWindow", "Eavesdropper"))
        self.check_system.setText(_translate("MainWindow", "Check"))
        self.run_plkg.setText(_translate("MainWindow", "Run PLKG"))
        self.system_tab.setTabText(self.system_tab.indexOf(self.tab), _translate("MainWindow", "Control Pannel"))
        self.system_tab.setTabText(self.system_tab.indexOf(self.tab_2), _translate("MainWindow", "Analysis"))
        self.gcs_settings.setTitle(_translate("MainWindow", "Ground Control Station"))
        self.gcs_ip_label.setText(_translate("MainWindow", "IP Address:"))
        self.drone_settings.setTitle(_translate("MainWindow", "Drone"))
        self.drone_ip_label.setText(_translate("MainWindow", "IP Address:"))
        self.eve_settings.setTitle(_translate("MainWindow", "Eavesdropper"))
        self.eve_ip_label.setText(_translate("MainWindow", "IP Address:"))
        self.iot_settings.setTitle(_translate("MainWindow", "IoT Device"))
        self.iot_ip_label.setText(_translate("MainWindow", "IP Address:"))
        self.settings_confirm.setText(_translate("MainWindow", "Confirm"))
        self.system_tab.setTabText(self.system_tab.indexOf(self.tab_3), _translate("MainWindow", "Settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
