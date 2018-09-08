# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created: Mon Aug 27 19:09:03 2018
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#import RPi.GPIO as GPIO
import threading
isModeA = False
isModeB = False
isHCO = False
isUVO = False
isO3O = False
isO2O = False
isBTO = False
isBNO = False
isPW = False

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        MainWindow.setStyleSheet("background-image: url(bg.jpg);")
        #MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnModeA = QtWidgets.QPushButton(self.centralwidget)
        self.btnModeA.setGeometry(QtCore.QRect(70, 120, 136, 131))
        self.btnModeA.setStyleSheet("background-image: url(offmode.png);\n""background-color: transparent;")
        self.btnModeA.setText("")
        self.btnModeA.setObjectName("pushButton")
        self.btnModeA.setEnabled(True)
        self.btnUV = QtWidgets.QPushButton(self.centralwidget)
        self.btnUV.setGeometry(QtCore.QRect(40, 390, 140, 131))
        self.btnUV.setStyleSheet("background-image: url(uvoff.png);")
        self.btnUV.setText("")
        self.btnUV.setObjectName("pushButton_3")
        self.btnPW = QtWidgets.QPushButton(self.centralwidget)
        self.btnPW.setGeometry(QtCore.QRect(680, 80, 235, 235))
        self.btnPW.setStyleSheet("background-image: url(offpw.png);\n""background-color: transparent;")
        self.btnPW.setText("")
        self.btnPW.setObjectName("pushButton_9")
        self.btnModeB = QtWidgets.QPushButton(self.centralwidget)
        self.btnModeB.setGeometry(QtCore.QRect(280, 120, 136, 131))
        self.btnModeB.setStyleSheet("background-image: url(offmode.png);\n""background-color: transparent;")
        self.btnModeB.setText("")
        self.btnModeB.setObjectName("pushButton_2")
        self.btnBT = QtWidgets.QPushButton(self.centralwidget)
        self.btnBT.setGeometry(QtCore.QRect(200, 390, 140, 131))
        self.btnBT.setStyleSheet("background-image: url(bom2off.png);")
        self.btnBT.setText("")
        self.btnBT.setObjectName("pushButton_4")
        self.btnO3 = QtWidgets.QPushButton(self.centralwidget)
        self.btnO3.setGeometry(QtCore.QRect(360, 390, 140, 131))
        self.btnO3.setStyleSheet("background-image: url(o3off.png);")
        self.btnO3.setText("")
        self.btnO3.setObjectName("pushButton_5")
        self.btnHC = QtWidgets.QPushButton(self.centralwidget)
        self.btnHC.setGeometry(QtCore.QRect(520, 390, 140, 131))
        self.btnHC.setText("")
        self.btnHC.setObjectName("pushButton_6")
        self.btnHC.setStyleSheet("background-image: url(hoachatoff.png);")
        self.btnO2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnO2.setGeometry(QtCore.QRect(680, 390, 140, 131))
        self.btnO2.setStyleSheet("background-image: url(o2off.png);")
        self.btnO2.setText("")
        self.btnO2.setObjectName("pushButton_7")
        self.btnBN = QtWidgets.QPushButton(self.centralwidget)
        self.btnBN.setGeometry(QtCore.QRect(840, 390, 140, 131))
        self.btnBN.setStyleSheet("background-image: url(bomoff.png);")
        self.btnBN.setText("")
        self.btnBN.setObjectName("pushButton_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.btnModeA.clicked.connect(self.ModeA)
        self.btnModeB.clicked.connect(self.ModeB)
        self.btnPW.clicked.connect(self.PW)
        self.loop()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def hc(self):
        if isHCO:
            self.btnHC.setStyleSheet("background-image: url(hoachatoff.png);")
        else:
            self.btnHC.setStyleSheet("background-image: url(hoachaton.png);")
    def ModeA(self):
        global isModeA
        if isModeA:
            self.btnModeA.setStyleSheet("background-image: url(offmode.png);\n""background-color: transparent;")
            isModeA = False
        else:
            self.btnModeA.setStyleSheet("background-image: url(onmode.png);\n""background-color: transparent;")
            isModeA = True
    def ModeB(self):
        global isModeB
        if isModeB:
            self.btnModeB.setStyleSheet("background-image: url(offmode.png);\n""background-color: transparent;")
            isModeB = False
        else:
            self.btnModeB.setStyleSheet("background-image: url(onmode.png);\n""background-color: transparent;")
            isModeB = True
    def UV(self):
        if isUVO:
            self.btnUV.setStyleSheet("background-image: url(uvon.png);")
        else:
            self.btnUV.setStyleSheet("background-image: url(uvoff.png);")
    def O3(self):
        if isO3O:
            self.btnO3.setStyleSheet("background-image: url(o3on.png);")
        else:
            self.btnO3.setStyleSheet("background-image: url(o3off.png);")
    def BT(self):
        if isBTO:
            self.btnBT.setStyleSheet("background-image: url(bom2off.png);")
        else:
            self.btnBT.setStyleSheet("background-image: url(bom2on.png);")
    def BN(self):
        if isBNO:
            self.btnBN.setStyleSheet("background-image: url(bomoff.png);")
        else:
            self.btnBN.setStyleSheet("background-image: url(bomon.png);")
    def O2(self):
        if isO2O:
            self.btnO2.setStyleSheet("background-image: url(o2off.png);")
        else:
            self.btnO2.setStyleSheet("background-image: url(o2on.png);")
    def PW(self):
		global isPW
        if isPW:
            self.btnPW.setStyleSheet("background-image: url(offpw.png);\n""background-color: transparent;")
			isPW = False
        else:
            self.btnPW.setStyleSheet("background-image: url(onpw.png);\n""background-color: transparent;")
			isPW = True
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    def loop(self):
        self.PW()
        self.O2()
        self.O3()
		self.BN()
		self.BT()
		self.hc()
        threading.Timer(1.0,self.loop).start()
		
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
