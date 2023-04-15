# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unfinishv3.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from IoD_UI.mplwidget import MplWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1800, 1000)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
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
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.control_pannel_frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.eve_console_label = QtWidgets.QLabel(self.control_pannel_frame)
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
        self.verticalLayout_4.addWidget(self.eve_console_label)
        self.eve_console = QtWidgets.QTextBrowser(self.control_pannel_frame)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.eve_console.setFont(font)
        self.eve_console.setObjectName("eve_console")
        self.verticalLayout_4.addWidget(self.eve_console)
        self.gridLayout_6.addLayout(self.verticalLayout_4, 0, 2, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.drone_console_label = QtWidgets.QLabel(self.control_pannel_frame)
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
        self.verticalLayout_2.addWidget(self.drone_console_label)
        self.drone_console = QtWidgets.QTextBrowser(self.control_pannel_frame)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.drone_console.setFont(font)
        self.drone_console.setObjectName("drone_console")
        self.verticalLayout_2.addWidget(self.drone_console)
        self.gridLayout_6.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.iot_console_label = QtWidgets.QLabel(self.control_pannel_frame)
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
        self.verticalLayout_3.addWidget(self.iot_console_label)
        self.iot_console = QtWidgets.QTextBrowser(self.control_pannel_frame)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.iot_console.setFont(font)
        self.iot_console.setObjectName("iot_console")
        self.verticalLayout_3.addWidget(self.iot_console)
        self.gridLayout_6.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_6)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.widget = QtWidgets.QWidget(self.control_pannel_frame)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.data_direction_label = QtWidgets.QLabel(self.widget)
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
        self.horizontalLayout.addWidget(self.data_direction_label)
        self.data_direction_type = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.data_direction_type.setFont(font)
        self.data_direction_type.setObjectName("data_direction_type")
        self.data_direction_type.addItem("")
        self.data_direction_type.addItem("")
        self.horizontalLayout.addWidget(self.data_direction_type)
        self.gridLayout_7.addWidget(self.widget, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.encryption_label = QtWidgets.QLabel(self.control_pannel_frame)
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
        self.horizontalLayout_2.addWidget(self.encryption_label)
        self.encryption_type = QtWidgets.QComboBox(self.control_pannel_frame)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.encryption_type.setFont(font)
        self.encryption_type.setObjectName("encryption_type")
        self.encryption_type.addItem("")
        self.encryption_type.addItem("")
        self.horizontalLayout_2.addWidget(self.encryption_type)
        self.gridLayout_7.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.control_pannel_frame)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_7.addWidget(self.widget_2, 0, 2, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.control_pannel_frame)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_7.addWidget(self.widget_3, 0, 4, 1, 1)
        self.send_data_buttom = QtWidgets.QPushButton(self.control_pannel_frame)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.send_data_buttom.setFont(font)
        self.send_data_buttom.setObjectName("send_data_buttom")
        self.gridLayout_7.addWidget(self.send_data_buttom, 0, 3, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_7)
        self.send_text_console = QtWidgets.QTextEdit(self.control_pannel_frame)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setBold(False)
        font.setWeight(50)
        self.send_text_console.setFont(font)
        self.send_text_console.setObjectName("send_text_console")
        self.verticalLayout_5.addWidget(self.send_text_console)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.system_prompt = QtWidgets.QGroupBox(self.control_pannel_frame)
        self.system_prompt.setObjectName("system_prompt")
        self.gridLayout = QtWidgets.QGridLayout(self.system_prompt)
        self.gridLayout.setObjectName("gridLayout")
        self.system_prompt_console = QtWidgets.QTextBrowser(self.system_prompt)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setBold(False)
        font.setWeight(50)
        self.system_prompt_console.setFont(font)
        self.system_prompt_console.setObjectName("system_prompt_console")
        self.gridLayout.addWidget(self.system_prompt_console, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.system_prompt, 0, 1, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_5 = QtWidgets.QWidget(self.control_pannel_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_6.addWidget(self.widget_5)
        self.run_plkg = QtWidgets.QPushButton(self.control_pannel_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.run_plkg.sizePolicy().hasHeightForWidth())
        self.run_plkg.setSizePolicy(sizePolicy)
        self.run_plkg.setObjectName("run_plkg")
        self.verticalLayout_6.addWidget(self.run_plkg)
        self.check_system = QtWidgets.QPushButton(self.control_pannel_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_system.sizePolicy().hasHeightForWidth())
        self.check_system.setSizePolicy(sizePolicy)
        self.check_system.setObjectName("check_system")
        self.verticalLayout_6.addWidget(self.check_system)
        self.widget_4 = QtWidgets.QWidget(self.control_pannel_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_6.addWidget(self.widget_4)
        self.gridLayout_2.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_2)
        self.verticalLayout.addWidget(self.control_pannel_frame)
        self.system_tab.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.analysis_button = QtWidgets.QPushButton(self.tab_2)
        self.analysis_button.setObjectName("analysis_button")
        self.gridLayout_4.addWidget(self.analysis_button, 1, 0, 1, 1)
        self.graphtogo = MplWidget(self.tab_2)
        self.graphtogo.setObjectName("graphtogo")
        self.gridLayout_4.addWidget(self.graphtogo, 0, 0, 1, 1)
        self.system_tab.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.eve_settings = QtWidgets.QGroupBox(self.tab_3)
        self.eve_settings.setObjectName("eve_settings")
        self.formLayout_3 = QtWidgets.QFormLayout(self.eve_settings)
        self.formLayout_3.setObjectName("formLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.eve_ip_label = QtWidgets.QLabel(self.eve_settings)
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
        self.horizontalLayout_5.addWidget(self.eve_ip_label)
        self.eve_ip = QtWidgets.QLineEdit(self.eve_settings)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setBold(False)
        font.setWeight(50)
        self.eve_ip.setFont(font)
        self.eve_ip.setText("")
        self.eve_ip.setObjectName("eve_ip")
        self.horizontalLayout_5.addWidget(self.eve_ip)
        self.formLayout_3.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_5)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.eve_port_label = QtWidgets.QLabel(self.eve_settings)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.eve_port_label.setFont(font)
        self.eve_port_label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.eve_port_label.setToolTipDuration(1)
        self.eve_port_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.eve_port_label.setAutoFillBackground(False)
        self.eve_port_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.eve_port_label.setObjectName("eve_port_label")
        self.horizontalLayout_10.addWidget(self.eve_port_label)
        self.eve_port = QtWidgets.QLineEdit(self.eve_settings)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setBold(False)
        font.setWeight(50)
        self.eve_port.setFont(font)
        self.eve_port.setText("")
        self.eve_port.setObjectName("eve_port")
        self.horizontalLayout_10.addWidget(self.eve_port)
        self.formLayout_3.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_10)
        self.gridLayout_8.addWidget(self.eve_settings, 0, 2, 1, 1)
        self.iot_settings = QtWidgets.QGroupBox(self.tab_3)
        self.iot_settings.setObjectName("iot_settings")
        self.formLayout_2 = QtWidgets.QFormLayout(self.iot_settings)
        self.formLayout_2.setObjectName("formLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.iot_ip_label = QtWidgets.QLabel(self.iot_settings)
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
        self.horizontalLayout_4.addWidget(self.iot_ip_label)
        self.iot_ip = QtWidgets.QLineEdit(self.iot_settings)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setBold(False)
        font.setWeight(50)
        self.iot_ip.setFont(font)
        self.iot_ip.setText("")
        self.iot_ip.setObjectName("iot_ip")
        self.horizontalLayout_4.addWidget(self.iot_ip)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_4)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.iot_port_label = QtWidgets.QLabel(self.iot_settings)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.iot_port_label.setFont(font)
        self.iot_port_label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.iot_port_label.setToolTipDuration(1)
        self.iot_port_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.iot_port_label.setAutoFillBackground(False)
        self.iot_port_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.iot_port_label.setObjectName("iot_port_label")
        self.horizontalLayout_9.addWidget(self.iot_port_label)
        self.iot_port = QtWidgets.QLineEdit(self.iot_settings)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setBold(False)
        font.setWeight(50)
        self.iot_port.setFont(font)
        self.iot_port.setText("")
        self.iot_port.setObjectName("iot_port")
        self.horizontalLayout_9.addWidget(self.iot_port)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_9)
        self.gridLayout_8.addWidget(self.iot_settings, 0, 1, 1, 1)
        self.drone_settings = QtWidgets.QGroupBox(self.tab_3)
        self.drone_settings.setObjectName("drone_settings")
        self.formLayout = QtWidgets.QFormLayout(self.drone_settings)
        self.formLayout.setObjectName("formLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.drone_ip_label = QtWidgets.QLabel(self.drone_settings)
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
        self.horizontalLayout_3.addWidget(self.drone_ip_label)
        self.drone_ip = QtWidgets.QLineEdit(self.drone_settings)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setBold(False)
        font.setWeight(50)
        self.drone_ip.setFont(font)
        self.drone_ip.setText("")
        self.drone_ip.setObjectName("drone_ip")
        self.horizontalLayout_3.addWidget(self.drone_ip)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.drone_port_label = QtWidgets.QLabel(self.drone_settings)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.drone_port_label.setFont(font)
        self.drone_port_label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.drone_port_label.setToolTipDuration(1)
        self.drone_port_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.drone_port_label.setAutoFillBackground(False)
        self.drone_port_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.drone_port_label.setObjectName("drone_port_label")
        self.horizontalLayout_8.addWidget(self.drone_port_label)
        self.drone_port = QtWidgets.QLineEdit(self.drone_settings)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setBold(False)
        font.setWeight(50)
        self.drone_port.setFont(font)
        self.drone_port.setText("")
        self.drone_port.setObjectName("drone_port")
        self.horizontalLayout_8.addWidget(self.drone_port)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_8)
        self.widget_6 = QtWidgets.QWidget(self.drone_settings)
        self.widget_6.setObjectName("widget_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.widget_6)
        self.gridLayout_8.addWidget(self.drone_settings, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.gcs_settings = QtWidgets.QGroupBox(self.tab_3)
        self.gcs_settings.setObjectName("gcs_settings")
        self.formLayout_4 = QtWidgets.QFormLayout(self.gcs_settings)
        self.formLayout_4.setObjectName("formLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.gcs_ip_label = QtWidgets.QLabel(self.gcs_settings)
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
        self.horizontalLayout_6.addWidget(self.gcs_ip_label)
        self.gcs_ip = QtWidgets.QLineEdit(self.gcs_settings)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setBold(False)
        font.setWeight(50)
        self.gcs_ip.setFont(font)
        self.gcs_ip.setText("")
        self.gcs_ip.setObjectName("gcs_ip")
        self.horizontalLayout_6.addWidget(self.gcs_ip)
        self.formLayout_4.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_6)
        self.horizontalLayout_7.addWidget(self.gcs_settings)
        self.settings_confirm = QtWidgets.QPushButton(self.tab_3)
        self.settings_confirm.setObjectName("settings_confirm")
        self.horizontalLayout_7.addWidget(self.settings_confirm)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem)
        self.system_tab.addTab(self.tab_3, "")
        self.gridLayout_5.addWidget(self.system_tab, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.system_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.eve_console_label.setText(_translate("MainWindow", "Eavesdropper"))
        self.eve_console.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'PMingLiU\'; font-weight:400;\"><br /></p></body></html>"))
        self.drone_console_label.setText(_translate("MainWindow", "Drone"))
        self.drone_console.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'PMingLiU\'; font-weight:400;\"><br /></p></body></html>"))
        self.iot_console_label.setText(_translate("MainWindow", "IoT Devie"))
        self.iot_console.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'PMingLiU\'; font-weight:400;\"><br /></p></body></html>"))
        self.data_direction_label.setText(_translate("MainWindow", "Data Transmission Direction:"))
        self.data_direction_type.setItemText(0, _translate("MainWindow", "Drone to IoT Device"))
        self.data_direction_type.setItemText(1, _translate("MainWindow", "IoT Device to Drone"))
        self.encryption_label.setText(_translate("MainWindow", "Encryption:"))
        self.encryption_type.setItemText(0, _translate("MainWindow", "<None>"))
        self.encryption_type.setItemText(1, _translate("MainWindow", "AES"))
        self.send_data_buttom.setText(_translate("MainWindow", "Send"))
        self.send_text_console.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.system_prompt.setTitle(_translate("MainWindow", "System Prompt:"))
        self.system_prompt_console.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.run_plkg.setText(_translate("MainWindow", "Run PLKG"))
        self.check_system.setText(_translate("MainWindow", "Check"))
        self.system_tab.setTabText(self.system_tab.indexOf(self.tab), _translate("MainWindow", "Control Pannel"))
        self.analysis_button.setText(_translate("MainWindow", "Analysis"))
        self.system_tab.setTabText(self.system_tab.indexOf(self.tab_2), _translate("MainWindow", "Analysis"))
        self.eve_settings.setTitle(_translate("MainWindow", "Eavesdropper"))
        self.eve_ip_label.setText(_translate("MainWindow", "IP Address:"))
        self.eve_port_label.setText(_translate("MainWindow", "Port:"))
        self.iot_settings.setTitle(_translate("MainWindow", "IoT Device"))
        self.iot_ip_label.setText(_translate("MainWindow", "IP Address:"))
        self.iot_port_label.setText(_translate("MainWindow", "Port:"))
        self.drone_settings.setTitle(_translate("MainWindow", "Drone"))
        self.drone_ip_label.setText(_translate("MainWindow", "IP Address:"))
        self.drone_port_label.setText(_translate("MainWindow", "Port:"))
        self.gcs_settings.setTitle(_translate("MainWindow", "Ground Control Station"))
        self.gcs_ip_label.setText(_translate("MainWindow", "IP Address:"))
        self.settings_confirm.setText(_translate("MainWindow", "Confirm"))
        self.system_tab.setTabText(self.system_tab.indexOf(self.tab_3), _translate("MainWindow", "Settings"))
