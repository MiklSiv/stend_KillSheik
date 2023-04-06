
import sys
import time
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
import client_TCP

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(755, 599)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_START_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_START_1.setGeometry(QtCore.QRect(50, 90, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_START_1.setFont(font)
        self.pushButton_START_1.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.pushButton_START_1.setObjectName("pushButton_START_1")
        self.pushButton_STOP_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_STOP_1.setGeometry(QtCore.QRect(50, 140, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_STOP_1.setFont(font)
        self.pushButton_STOP_1.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.pushButton_STOP_1.setObjectName("pushButton_STOP_1")
        self.groupBox__ystavki1 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox__ystavki1.setGeometry(QtCore.QRect(30, 240, 111, 221))
        self.groupBox__ystavki1.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.groupBox__ystavki1.setObjectName("groupBox__ystavki1")
        self.nadpis_temper_2 = QtWidgets.QLabel(self.groupBox__ystavki1)
        self.nadpis_temper_2.setGeometry(QtCore.QRect(20, 100, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nadpis_temper_2.setFont(font)
        self.nadpis_temper_2.setMouseTracking(False)
        self.nadpis_temper_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.nadpis_temper_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nadpis_temper_2.setStyleSheet("background-color: rgb(243, 205, 255);")
        self.nadpis_temper_2.setAlignment(QtCore.Qt.AlignCenter)
        self.nadpis_temper_2.setObjectName("nadpis_temper_2")
        self.nadpis_oboroti_2 = QtWidgets.QLabel(self.groupBox__ystavki1)
        self.nadpis_oboroti_2.setGeometry(QtCore.QRect(20, 20, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nadpis_oboroti_2.setFont(font)
        self.nadpis_oboroti_2.setMouseTracking(False)
        self.nadpis_oboroti_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.nadpis_oboroti_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nadpis_oboroti_2.setStyleSheet("background-color: rgb(243, 205, 255);")
        self.nadpis_oboroti_2.setAlignment(QtCore.Qt.AlignCenter)
        self.nadpis_oboroti_2.setObjectName("nadpis_oboroti_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox__ystavki1)
        self.pushButton.setGeometry(QtCore.QRect(20, 180, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox__ystavki1)
        self.textBrowser.setGeometry(QtCore.QRect(20, 130, 71, 31))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 231, 206);")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox__ystavki1)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 50, 71, 31))
        self.textBrowser_2.setStyleSheet("background-color: rgb(255, 231, 206);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_STOP_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_STOP_2.setGeometry(QtCore.QRect(410, 140, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_STOP_2.setFont(font)
        self.pushButton_STOP_2.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.pushButton_STOP_2.setObjectName("pushButton_STOP_2")
        self.pushButton_START_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_START_2.setGeometry(QtCore.QRect(410, 90, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_START_2.setFont(font)
        self.pushButton_START_2.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.pushButton_START_2.setObjectName("pushButton_START_2")
        self.parametr_temp_vozdyha = QtWidgets.QLabel(self.centralwidget)
        self.parametr_temp_vozdyha.setGeometry(QtCore.QRect(380, 540, 131, 21))
        self.parametr_temp_vozdyha.setMouseTracking(False)
        self.parametr_temp_vozdyha.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.parametr_temp_vozdyha.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.parametr_temp_vozdyha.setStyleSheet("background-color: rgb(197, 255, 161);")
        self.parametr_temp_vozdyha.setText("")
        self.parametr_temp_vozdyha.setAlignment(QtCore.Qt.AlignCenter)
        self.parametr_temp_vozdyha.setObjectName("parametr_temp_vozdyha")
        self.nadpis_temp_vozdyha = QtWidgets.QLabel(self.centralwidget)
        self.nadpis_temp_vozdyha.setGeometry(QtCore.QRect(210, 540, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nadpis_temp_vozdyha.setFont(font)
        self.nadpis_temp_vozdyha.setMouseTracking(False)
        self.nadpis_temp_vozdyha.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.nadpis_temp_vozdyha.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nadpis_temp_vozdyha.setStyleSheet("background-color: rgb(251, 255, 167);")
        self.nadpis_temp_vozdyha.setAlignment(QtCore.Qt.AlignCenter)
        self.nadpis_temp_vozdyha.setObjectName("nadpis_temp_vozdyha")
        self.pushButton_STOP = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_STOP.setGeometry(QtCore.QRect(410, 10, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_STOP.setFont(font)
        self.pushButton_STOP.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.pushButton_STOP.setObjectName("pushButton_STOP")
        self.pushButton_START = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_START.setGeometry(QtCore.QRect(270, 10, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_START.setFont(font)
        self.pushButton_START.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.pushButton_START.setObjectName("pushButton_START")
        self.groupBox_stakan1 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_stakan1.setGeometry(QtCore.QRect(160, 90, 151, 411))
        self.groupBox_stakan1.setStyleSheet("background-color: rgb(252, 234, 255);")
        self.groupBox_stakan1.setObjectName("groupBox_stakan1")
        self.nadpis_DO2_N1 = QtWidgets.QLabel(self.groupBox_stakan1)
        self.nadpis_DO2_N1.setGeometry(QtCore.QRect(20, 180, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nadpis_DO2_N1.setFont(font)
        self.nadpis_DO2_N1.setMouseTracking(False)
        self.nadpis_DO2_N1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.nadpis_DO2_N1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nadpis_DO2_N1.setStyleSheet("background-color: rgb(251, 255, 167);")
        self.nadpis_DO2_N1.setAlignment(QtCore.Qt.AlignCenter)
        self.nadpis_DO2_N1.setObjectName("nadpis_DO2_N1")
        self.parametr_pH_V1 = QtWidgets.QLabel(self.groupBox_stakan1)
        self.parametr_pH_V1.setGeometry(QtCore.QRect(90, 100, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.parametr_pH_V1.setFont(font)
        self.parametr_pH_V1.setMouseTracking(False)
        self.parametr_pH_V1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.parametr_pH_V1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.parametr_pH_V1.setStyleSheet("background-color: rgb(197, 255, 161);")
        self.parametr_pH_V1.setText("")
        self.parametr_pH_V1.setAlignment(QtCore.Qt.AlignCenter)
        self.parametr_pH_V1.setObjectName("parametr_pH_V1")
        self.parametr_pH_N1 = QtWidgets.QLabel(self.groupBox_stakan1)
        self.parametr_pH_N1.setGeometry(QtCore.QRect(90, 260, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.parametr_pH_N1.setFont(font)
        self.parametr_pH_N1.setMouseTracking(False)
        self.parametr_pH_N1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.parametr_pH_N1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.parametr_pH_N1.setStyleSheet("background-color: rgb(197, 255, 161);")
        self.parametr_pH_N1.setText("")
        self.parametr_pH_N1.setAlignment(QtCore.Qt.AlignCenter)
        self.parametr_pH_N1.setObjectName("parametr_pH_N1")
        self.nadpis_CO2_N1 = QtWidgets.QLabel(self.groupBox_stakan1)
        self.nadpis_CO2_N1.setGeometry(QtCore.QRect(20, 220, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nadpis_CO2_N1.setFont(font)
        self.nadpis_CO2_N1.setMouseTracking(False)
        self.nadpis_CO2_N1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.nadpis_CO2_N1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nadpis_CO2_N1.setStyleSheet("background-color: rgb(251, 255, 167);")
        self.nadpis_CO2_N1.setAlignment(QtCore.Qt.AlignCenter)
        self.nadpis_CO2_N1.setObjectName("nadpis_CO2_N1")
        self.parametr_oboroti_1 = QtWidgets.QLabel(self.groupBox_stakan1)
        self.parametr_oboroti_1.setGeometry(QtCore.QRect(90, 300, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.parametr_oboroti_1.setFont(font)
        self.parametr_oboroti_1.setMouseTracking(False)
        self.parametr_oboroti_1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.parametr_oboroti_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.parametr_oboroti_1.setStyleSheet("background-color: rgb(197, 255, 161);")
        self.parametr_oboroti_1.setText("")
        self.parametr_oboroti_1.setAlignment(QtCore.Qt.AlignCenter)
        self.parametr_oboroti_1.setObjectName("parametr_oboroti_1")
        self.parametr_DO2_N1 = QtWidgets.QLabel(self.groupBox_stakan1)
        self.parametr_DO2_N1.setGeometry(QtCore.QRect(90, 180, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.parametr_DO2_N1.setFont(font)
        self.parametr_DO2_N1.setMouseTracking(False)
        self.parametr_DO2_N1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.parametr_DO2_N1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.parametr_DO2_N1.setStyleSheet("background-color: rgb(197, 255, 161);")
        self.parametr_DO2_N1.setText("")
        self.parametr_DO2_N1.setAlignment(QtCore.Qt.AlignCenter)
        self.parametr_DO2_N1.setObjectName("parametr_DO2_N1")
        self.nadpis_pH_V1 = QtWidgets.QLabel(self.groupBox_stakan1)
        self.nadpis_pH_V1.setGeometry(QtCore.QRect(20, 100, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nadpis_pH_V1.setFont(font)
        self.nadpis_pH_V1.setMouseTracking(False)
        self.nadpis_pH_V1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.nadpis_pH_V1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nadpis_pH_V1.setStyleSheet("background-color: rgb(251, 255, 167);")
        self.nadpis_pH_V1.setAlignment(QtCore.Qt.AlignCenter)
        self.nadpis_pH_V1.setObjectName("nadpis_pH_V1")
        self.parametr_CO2_N1 = QtWidgets.QLabel(self.groupBox_stakan1)
        self.parametr_CO2_N1.setGeometry(QtCore.QRect(90, 220, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.parametr_CO2_N1.setFont(font)
        self.parametr_CO2_N1.setMouseTracking(False)
        self.parametr_CO2_N1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.parametr_CO2_N1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.parametr_CO2_N1.setStyleSheet("background-color: rgb(197, 255, 161);")
        self.parametr_CO2_N1.setText("")
        self.parametr_CO2_N1.setAlignment(QtCore.Qt.AlignCenter)
        self.parametr_CO2_N1.setObjectName("parametr_CO2_N1")
        self.parametr_CO2_V1 = QtWidgets.QLabel(self.groupBox_stakan1)
        self.parametr_CO2_V1.setGeometry(QtCore.QRect(90, 60, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.parametr_CO2_V1.setFont(font)
        self.parametr_CO2_V1.setMouseTracking(False)
        self.parametr_CO2_V1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.parametr_CO2_V1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.parametr_CO2_V1.setStyleSheet("background-color: rgb(197, 255, 161);")
        self.parametr_CO2_V1.setText("")
        self.parametr_CO2_V1.setAlignment(QtCore.Qt.AlignCenter)
        self.parametr_CO2_V1.setObjectName("parametr_CO2_V1")
        self.nadpis_oboroti_1 = QtWidgets.QLabel(self.groupBox_stakan1)
        self.nadpis_oboroti_1.setGeometry(QtCore.QRect(20, 300, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nadpis_oboroti_1.setFont(font)
        self.nadpis_oboroti_1.setMouseTracking(False)
        self.nadpis_oboroti_1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.nadpis_oboroti_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nadpis_oboroti_1.setStyleSheet("background-color: rgb(251, 255, 167);")
        self.nadpis_oboroti_1.setAlignment(QtCore.Qt.AlignCenter)
        self.nadpis_oboroti_1.setObjectName("nadpis_oboroti_1")
        self.paramertr_temperVanni_1 = QtWidgets.QLabel(self.groupBox_stakan1)
        self.paramertr_temperVanni_1.setGeometry(QtCore.QRect(90, 380, 51, 21))
        self.paramertr_temperVanni_1.setMouseTracking(False)
        self.paramertr_temperVanni_1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.paramertr_temperVanni_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.paramertr_temperVanni_1.setStyleSheet("background-color: rgb(197, 255, 161);")
        self.paramertr_temperVanni_1.setText("")
        self.paramertr_temperVanni_1.setAlignment(QtCore.Qt.AlignCenter)
        self.paramertr_temperVanni_1.setObjectName("paramertr_temperVanni_1")
        self.nadpis_temperVanni_1 = QtWidgets.QLabel(self.groupBox_stakan1)
        self.nadpis_temperVanni_1.setGeometry(QtCore.QRect(20, 380, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nadpis_temperVanni_1.setFont(font)
        self.nadpis_temperVanni_1.setMouseTracking(False)
        self.nadpis_temperVanni_1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.nadpis_temperVanni_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nadpis_temperVanni_1.setStyleSheet("background-color: rgb(251, 255, 167);")
        self.nadpis_temperVanni_1.setAlignment(QtCore.Qt.AlignCenter)
        self.nadpis_temperVanni_1.setObjectName("nadpis_temperVanni_1")
        self.nadpis_pH_N1 = QtWidgets.QLabel(self.groupBox_stakan1)
        self.nadpis_pH_N1.setGeometry(QtCore.QRect(20, 260, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nadpis_pH_N1.setFont(font)
        self.nadpis_pH_N1.setMouseTracking(False)
        self.nadpis_pH_N1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.nadpis_pH_N1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nadpis_pH_N1.setStyleSheet("background-color: rgb(251, 255, 167);")
        self.nadpis_pH_N1.setAlignment(QtCore.Qt.AlignCenter)
        self.nadpis_pH_N1.setObjectName("nadpis_pH_N1")
        self.nadpis_CO2_V1 = QtWidgets.QLabel(self.groupBox_stakan1)
        self.nadpis_CO2_V1.setGeometry(QtCore.QRect(20, 60, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nadpis_CO2_V1.setFont(font)
        self.nadpis_CO2_V1.setMouseTracking(False)
        self.nadpis_CO2_V1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.nadpis_CO2_V1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nadpis_CO2_V1.setStyleSheet("background-color: rgb(251, 255, 167);")
        self.nadpis_CO2_V1.setAlignment(QtCore.Qt.AlignCenter)
        self.nadpis_CO2_V1.setObjectName("nadpis_CO2_V1")
        self.parametr_temperSredi_1 = QtWidgets.QLabel(self.groupBox_stakan1)
        self.parametr_temperSredi_1.setGeometry(QtCore.QRect(90, 340, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.parametr_temperSredi_1.setFont(font)
        self.parametr_temperSredi_1.setMouseTracking(False)
        self.parametr_temperSredi_1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.parametr_temperSredi_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.parametr_temperSredi_1.setStyleSheet("background-color: rgb(197, 255, 161);")
        self.parametr_temperSredi_1.setText("")
        self.parametr_temperSredi_1.setAlignment(QtCore.Qt.AlignCenter)
        self.parametr_temperSredi_1.setObjectName("parametr_temperSredi_1")
        self.nadpis_DO2_V1 = QtWidgets.QLabel(self.groupBox_stakan1)
        self.nadpis_DO2_V1.setGeometry(QtCore.QRect(20, 20, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nadpis_DO2_V1.setFont(font)
        self.nadpis_DO2_V1.setMouseTracking(False)
        self.nadpis_DO2_V1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.nadpis_DO2_V1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nadpis_DO2_V1.setStyleSheet("background-color: rgb(251, 255, 167);")
        self.nadpis_DO2_V1.setAlignment(QtCore.Qt.AlignCenter)
        self.nadpis_DO2_V1.setObjectName("nadpis_DO2_V1")
        self.parametr_DO2_V1 = QtWidgets.QLabel(self.groupBox_stakan1)
        self.parametr_DO2_V1.setGeometry(QtCore.QRect(90, 20, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.parametr_DO2_V1.setFont(font)
        self.parametr_DO2_V1.setMouseTracking(False)
        self.parametr_DO2_V1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.parametr_DO2_V1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.parametr_DO2_V1.setStyleSheet("background-color: rgb(197, 255, 161);")
        self.parametr_DO2_V1.setText("")
        self.parametr_DO2_V1.setAlignment(QtCore.Qt.AlignCenter)
        self.parametr_DO2_V1.setObjectName("parametr_DO2_V1")
        self.nadpis_temperSredi_1 = QtWidgets.QLabel(self.groupBox_stakan1)
        self.nadpis_temperSredi_1.setGeometry(QtCore.QRect(20, 340, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nadpis_temperSredi_1.setFont(font)
        self.nadpis_temperSredi_1.setMouseTracking(False)
        self.nadpis_temperSredi_1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.nadpis_temperSredi_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nadpis_temperSredi_1.setStyleSheet("background-color: rgb(251, 255, 167);")
        self.nadpis_temperSredi_1.setAlignment(QtCore.Qt.AlignCenter)
        self.nadpis_temperSredi_1.setObjectName("nadpis_temperSredi_1")
        self.groupBox__ystavki2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox__ystavki2.setGeometry(QtCore.QRect(390, 240, 111, 221))
        self.groupBox__ystavki2.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.groupBox__ystavki2.setObjectName("groupBox__ystavki2")
        self.nadpis_temper_3 = QtWidgets.QLabel(self.groupBox__ystavki2)
        self.nadpis_temper_3.setGeometry(QtCore.QRect(20, 100, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nadpis_temper_3.setFont(font)
        self.nadpis_temper_3.setMouseTracking(False)
        self.nadpis_temper_3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.nadpis_temper_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nadpis_temper_3.setStyleSheet("background-color: rgb(243, 205, 255);")
        self.nadpis_temper_3.setAlignment(QtCore.Qt.AlignCenter)
        self.nadpis_temper_3.setObjectName("nadpis_temper_3")
        self.nadpis_oboroti_3 = QtWidgets.QLabel(self.groupBox__ystavki2)
        self.nadpis_oboroti_3.setGeometry(QtCore.QRect(20, 20, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nadpis_oboroti_3.setFont(font)
        self.nadpis_oboroti_3.setMouseTracking(False)
        self.nadpis_oboroti_3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.nadpis_oboroti_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nadpis_oboroti_3.setStyleSheet("background-color: rgb(243, 205, 255);")
        self.nadpis_oboroti_3.setAlignment(QtCore.Qt.AlignCenter)
        self.nadpis_oboroti_3.setObjectName("nadpis_oboroti_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox__ystavki2)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 180, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.groupBox__ystavki2)
        self.textBrowser_3.setGeometry(QtCore.QRect(20, 50, 71, 31))
        self.textBrowser_3.setStyleSheet("background-color: rgb(255, 231, 206);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.groupBox__ystavki2)
        self.textBrowser_4.setGeometry(QtCore.QRect(20, 130, 71, 31))
        self.textBrowser_4.setStyleSheet("background-color: rgb(255, 231, 206);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.groupBox_stakan2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_stakan2.setGeometry(QtCore.QRect(520, 90, 151, 411))
        self.groupBox_stakan2.setStyleSheet("background-color: rgb(252, 234, 255);")
        self.groupBox_stakan2.setObjectName("groupBox_stakan2")
        self.nadpis_DO2_N2 = QtWidgets.QLabel(self.groupBox_stakan2)
        self.nadpis_DO2_N2.setGeometry(QtCore.QRect(20, 180, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nadpis_DO2_N2.setFont(font)
        self.nadpis_DO2_N2.setMouseTracking(False)
        self.nadpis_DO2_N2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.nadpis_DO2_N2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nadpis_DO2_N2.setStyleSheet("background-color: rgb(251, 255, 167);")
        self.nadpis_DO2_N2.setAlignment(QtCore.Qt.AlignCenter)
        self.nadpis_DO2_N2.setObjectName("nadpis_DO2_N2")
        self.parametr_pH_V2 = QtWidgets.QLabel(self.groupBox_stakan2)
        self.parametr_pH_V2.setGeometry(QtCore.QRect(90, 100, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.parametr_pH_V2.setFont(font)
        self.parametr_pH_V2.setMouseTracking(False)
        self.parametr_pH_V2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.parametr_pH_V2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.parametr_pH_V2.setStyleSheet("background-color: rgb(197, 255, 161);")
        self.parametr_pH_V2.setText("")
        self.parametr_pH_V2.setAlignment(QtCore.Qt.AlignCenter)
        self.parametr_pH_V2.setObjectName("parametr_pH_V2")
        self.parametr_pH_N2 = QtWidgets.QLabel(self.groupBox_stakan2)
        self.parametr_pH_N2.setGeometry(QtCore.QRect(90, 260, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.parametr_pH_N2.setFont(font)
        self.parametr_pH_N2.setMouseTracking(False)
        self.parametr_pH_N2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.parametr_pH_N2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.parametr_pH_N2.setStyleSheet("background-color: rgb(197, 255, 161);")
        self.parametr_pH_N2.setText("")
        self.parametr_pH_N2.setAlignment(QtCore.Qt.AlignCenter)
        self.parametr_pH_N2.setObjectName("parametr_pH_N2")
        self.nadpis_CO2_N2 = QtWidgets.QLabel(self.groupBox_stakan2)
        self.nadpis_CO2_N2.setGeometry(QtCore.QRect(20, 220, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nadpis_CO2_N2.setFont(font)
        self.nadpis_CO2_N2.setMouseTracking(False)
        self.nadpis_CO2_N2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.nadpis_CO2_N2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nadpis_CO2_N2.setStyleSheet("background-color: rgb(251, 255, 167);")
        self.nadpis_CO2_N2.setAlignment(QtCore.Qt.AlignCenter)
        self.nadpis_CO2_N2.setObjectName("nadpis_CO2_N2")
        self.parametr_oboroti_2 = QtWidgets.QLabel(self.groupBox_stakan2)
        self.parametr_oboroti_2.setGeometry(QtCore.QRect(90, 300, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.parametr_oboroti_2.setFont(font)
        self.parametr_oboroti_2.setMouseTracking(False)
        self.parametr_oboroti_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.parametr_oboroti_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.parametr_oboroti_2.setStyleSheet("background-color: rgb(197, 255, 161);")
        self.parametr_oboroti_2.setText("")
        self.parametr_oboroti_2.setAlignment(QtCore.Qt.AlignCenter)
        self.parametr_oboroti_2.setObjectName("parametr_oboroti_2")
        self.parametr_DO2_N2 = QtWidgets.QLabel(self.groupBox_stakan2)
        self.parametr_DO2_N2.setGeometry(QtCore.QRect(90, 180, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.parametr_DO2_N2.setFont(font)
        self.parametr_DO2_N2.setMouseTracking(False)
        self.parametr_DO2_N2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.parametr_DO2_N2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.parametr_DO2_N2.setStyleSheet("background-color: rgb(197, 255, 161);")
        self.parametr_DO2_N2.setText("")
        self.parametr_DO2_N2.setAlignment(QtCore.Qt.AlignCenter)
        self.parametr_DO2_N2.setObjectName("parametr_DO2_N2")
        self.nadpis_pH_V2 = QtWidgets.QLabel(self.groupBox_stakan2)
        self.nadpis_pH_V2.setGeometry(QtCore.QRect(20, 100, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nadpis_pH_V2.setFont(font)
        self.nadpis_pH_V2.setMouseTracking(False)
        self.nadpis_pH_V2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.nadpis_pH_V2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nadpis_pH_V2.setStyleSheet("background-color: rgb(251, 255, 167);")
        self.nadpis_pH_V2.setAlignment(QtCore.Qt.AlignCenter)
        self.nadpis_pH_V2.setObjectName("nadpis_pH_V2")
        self.parametr_CO2_N2 = QtWidgets.QLabel(self.groupBox_stakan2)
        self.parametr_CO2_N2.setGeometry(QtCore.QRect(90, 220, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.parametr_CO2_N2.setFont(font)
        self.parametr_CO2_N2.setMouseTracking(False)
        self.parametr_CO2_N2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.parametr_CO2_N2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.parametr_CO2_N2.setStyleSheet("background-color: rgb(197, 255, 161);")
        self.parametr_CO2_N2.setText("")
        self.parametr_CO2_N2.setAlignment(QtCore.Qt.AlignCenter)
        self.parametr_CO2_N2.setObjectName("parametr_CO2_N2")
        self.parametr_CO2_V2 = QtWidgets.QLabel(self.groupBox_stakan2)
        self.parametr_CO2_V2.setGeometry(QtCore.QRect(90, 60, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.parametr_CO2_V2.setFont(font)
        self.parametr_CO2_V2.setMouseTracking(False)
        self.parametr_CO2_V2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.parametr_CO2_V2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.parametr_CO2_V2.setStyleSheet("background-color: rgb(197, 255, 161);")
        self.parametr_CO2_V2.setText("")
        self.parametr_CO2_V2.setAlignment(QtCore.Qt.AlignCenter)
        self.parametr_CO2_V2.setObjectName("parametr_CO2_V2")
        self.nadpis_oboroti_4 = QtWidgets.QLabel(self.groupBox_stakan2)
        self.nadpis_oboroti_4.setGeometry(QtCore.QRect(20, 300, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nadpis_oboroti_4.setFont(font)
        self.nadpis_oboroti_4.setMouseTracking(False)
        self.nadpis_oboroti_4.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.nadpis_oboroti_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nadpis_oboroti_4.setStyleSheet("background-color: rgb(251, 255, 167);")
        self.nadpis_oboroti_4.setAlignment(QtCore.Qt.AlignCenter)
        self.nadpis_oboroti_4.setObjectName("nadpis_oboroti_4")
        self.parametr_temperVanni_2 = QtWidgets.QLabel(self.groupBox_stakan2)
        self.parametr_temperVanni_2.setGeometry(QtCore.QRect(90, 380, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.parametr_temperVanni_2.setFont(font)
        self.parametr_temperVanni_2.setMouseTracking(False)
        self.parametr_temperVanni_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.parametr_temperVanni_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.parametr_temperVanni_2.setStyleSheet("background-color: rgb(197, 255, 161);")
        self.parametr_temperVanni_2.setText("")
        self.parametr_temperVanni_2.setAlignment(QtCore.Qt.AlignCenter)
        self.parametr_temperVanni_2.setObjectName("parametr_temperVanni_2")
        self.nadpis_temperVanni_2 = QtWidgets.QLabel(self.groupBox_stakan2)
        self.nadpis_temperVanni_2.setGeometry(QtCore.QRect(20, 380, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nadpis_temperVanni_2.setFont(font)
        self.nadpis_temperVanni_2.setMouseTracking(False)
        self.nadpis_temperVanni_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.nadpis_temperVanni_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nadpis_temperVanni_2.setStyleSheet("background-color: rgb(251, 255, 167);")
        self.nadpis_temperVanni_2.setAlignment(QtCore.Qt.AlignCenter)
        self.nadpis_temperVanni_2.setObjectName("nadpis_temperVanni_2")
        self.nadpis_pH_N2 = QtWidgets.QLabel(self.groupBox_stakan2)
        self.nadpis_pH_N2.setGeometry(QtCore.QRect(20, 260, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nadpis_pH_N2.setFont(font)
        self.nadpis_pH_N2.setMouseTracking(False)
        self.nadpis_pH_N2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.nadpis_pH_N2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nadpis_pH_N2.setStyleSheet("background-color: rgb(251, 255, 167);")
        self.nadpis_pH_N2.setAlignment(QtCore.Qt.AlignCenter)
        self.nadpis_pH_N2.setObjectName("nadpis_pH_N2")
        self.nadpis_CO2_V2 = QtWidgets.QLabel(self.groupBox_stakan2)
        self.nadpis_CO2_V2.setGeometry(QtCore.QRect(20, 60, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nadpis_CO2_V2.setFont(font)
        self.nadpis_CO2_V2.setMouseTracking(False)
        self.nadpis_CO2_V2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.nadpis_CO2_V2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nadpis_CO2_V2.setStyleSheet("background-color: rgb(251, 255, 167);")
        self.nadpis_CO2_V2.setAlignment(QtCore.Qt.AlignCenter)
        self.nadpis_CO2_V2.setObjectName("nadpis_CO2_V2")
        self.parametr_temperSredi_2 = QtWidgets.QLabel(self.groupBox_stakan2)
        self.parametr_temperSredi_2.setGeometry(QtCore.QRect(90, 340, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.parametr_temperSredi_2.setFont(font)
        self.parametr_temperSredi_2.setMouseTracking(False)
        self.parametr_temperSredi_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.parametr_temperSredi_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.parametr_temperSredi_2.setStyleSheet("background-color: rgb(197, 255, 161);")
        self.parametr_temperSredi_2.setText("")
        self.parametr_temperSredi_2.setAlignment(QtCore.Qt.AlignCenter)
        self.parametr_temperSredi_2.setObjectName("parametr_temperSredi_2")
        self.nadpis_DO2_V2 = QtWidgets.QLabel(self.groupBox_stakan2)
        self.nadpis_DO2_V2.setGeometry(QtCore.QRect(20, 20, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nadpis_DO2_V2.setFont(font)
        self.nadpis_DO2_V2.setMouseTracking(False)
        self.nadpis_DO2_V2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.nadpis_DO2_V2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nadpis_DO2_V2.setStyleSheet("background-color: rgb(251, 255, 167);")
        self.nadpis_DO2_V2.setAlignment(QtCore.Qt.AlignCenter)
        self.nadpis_DO2_V2.setObjectName("nadpis_DO2_V2")
        self.parametr_DO2_V2 = QtWidgets.QLabel(self.groupBox_stakan2)
        self.parametr_DO2_V2.setGeometry(QtCore.QRect(90, 20, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.parametr_DO2_V2.setFont(font)
        self.parametr_DO2_V2.setMouseTracking(False)
        self.parametr_DO2_V2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.parametr_DO2_V2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.parametr_DO2_V2.setStyleSheet("background-color: rgb(197, 255, 161);")
        self.parametr_DO2_V2.setText("")
        self.parametr_DO2_V2.setAlignment(QtCore.Qt.AlignCenter)
        self.parametr_DO2_V2.setObjectName("parametr_DO2_V2")
        self.nadpis_temperSredi_2 = QtWidgets.QLabel(self.groupBox_stakan2)
        self.nadpis_temperSredi_2.setGeometry(QtCore.QRect(20, 340, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nadpis_temperSredi_2.setFont(font)
        self.nadpis_temperSredi_2.setMouseTracking(False)
        self.nadpis_temperSredi_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.nadpis_temperSredi_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nadpis_temperSredi_2.setStyleSheet("background-color: rgb(251, 255, 167);")
        self.nadpis_temperSredi_2.setAlignment(QtCore.Qt.AlignCenter)
        self.nadpis_temperSredi_2.setObjectName("nadpis_temperSredi_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Система управления Килл-Шейк"))
        self.pushButton_START_1.setText(_translate("MainWindow", "ПУСК"))
        self.pushButton_STOP_1.setText(_translate("MainWindow", "СТОП"))
        self.groupBox__ystavki1.setTitle(_translate("MainWindow", "УСТАВКИ"))
        self.nadpis_temper_2.setText(_translate("MainWindow", "T"))
        self.nadpis_oboroti_2.setText(_translate("MainWindow", "обороты"))
        self.pushButton.setText(_translate("MainWindow", "Примеить"))
        self.pushButton_STOP_2.setText(_translate("MainWindow", "СТОП"))
        self.pushButton_START_2.setText(_translate("MainWindow", "ПУСК"))
        self.nadpis_temp_vozdyha.setText(_translate("MainWindow", "температура воздуха"))
        self.pushButton_STOP.setText(_translate("MainWindow", "СТОП"))
        self.pushButton_START.setText(_translate("MainWindow", "ПУСК"))
        self.groupBox_stakan1.setTitle(_translate("MainWindow", "СТАКАН №1"))
        self.nadpis_DO2_N1.setText(_translate("MainWindow", "DO2"))
        self.nadpis_CO2_N1.setText(_translate("MainWindow", "CO2"))
        self.nadpis_pH_V1.setText(_translate("MainWindow", "pH"))
        self.nadpis_oboroti_1.setText(_translate("MainWindow", "обороты"))
        self.nadpis_temperVanni_1.setText(_translate("MainWindow", "T ванны"))
        self.nadpis_pH_N1.setText(_translate("MainWindow", "pH"))
        self.nadpis_CO2_V1.setText(_translate("MainWindow", "CO2"))
        self.nadpis_DO2_V1.setText(_translate("MainWindow", "DO2"))
        self.nadpis_temperSredi_1.setText(_translate("MainWindow", "T среды"))
        self.groupBox__ystavki2.setTitle(_translate("MainWindow", "УСТАВКИ"))
        self.nadpis_temper_3.setText(_translate("MainWindow", "T"))
        self.nadpis_oboroti_3.setText(_translate("MainWindow", "обороты"))
        self.pushButton_2.setText(_translate("MainWindow", "Примеить"))
        self.groupBox_stakan2.setTitle(_translate("MainWindow", "СТАКАН №2"))
        self.nadpis_DO2_N2.setText(_translate("MainWindow", "DO2"))
        self.nadpis_CO2_N2.setText(_translate("MainWindow", "CO2"))
        self.nadpis_pH_V2.setText(_translate("MainWindow", "pH"))
        self.nadpis_oboroti_4.setText(_translate("MainWindow", "обороты"))
        self.nadpis_temperVanni_2.setText(_translate("MainWindow", "T ванны"))
        self.nadpis_pH_N2.setText(_translate("MainWindow", "pH"))
        self.nadpis_CO2_V2.setText(_translate("MainWindow", "CO2"))
        self.nadpis_DO2_V2.setText(_translate("MainWindow", "DO2"))
        self.nadpis_temperSredi_2.setText(_translate("MainWindow", "T среды"))

        self.flag = True
        #self.start_opros()




    def potok_dannih_in(self):
        while self.flag:
            self.parametr_DO2_V2.setText(str(client_TCP.stakan_2['DO2V']))
            self.parametr_pH_N2.setText(str(client_TCP.stakan_2['pHN']))
            self.parametr_temperSredi_2.setText(str(client_TCP.stakan_2['tsr']))
            self.parametr_CO2_N2.setText(str(client_TCP.stakan_2['CO2N']))
            self.parametr_DO2_N2.setText(str(client_TCP.stakan_2['DO2N']))
            self.parametr_CO2_V2.setText(str(client_TCP.stakan_2['CO2V']))
            self.parametr_temperVanni_2.setText(str(client_TCP.stakan_2['tvanni']))
            self.parametr_pH_V2.setText(str(client_TCP.stakan_2['pHV']))
            self.parametr_oboroti_2.setText(str(client_TCP.stakan_2['oborot']))
            time.sleep(1)

    #def start_opros(self):
        #wer = threading.Thread(target=self.potok_dannih_in)
        #self.pushButton_START_2.clicked.connect(wer.start())



def app(): # графический интерфей
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
    ui.potok_dannih_in()
    sys.exit()

if __name__ == "__main__":
    app()
