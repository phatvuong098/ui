# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui1.ui'
#
# Created: Thu Aug  2 16:49:39 2018
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import RPi.GPIO as GPIO
import threading
import serial

ser = serial.Serial('/dev/ttyUSB0',9600)
iphaotrong = 11
iphaongoai =13
ibomtrong = 15
ibomngoai = 16
isuckhi = 18
ihoaChat = 22
iozon = 29
iuv = 31

ouv = 32
ozon =33
obomtrong = 35
obomngoai = 36
osuckhi = 37
ohoachat = 38
ison = 0
sodem = 0
isdem = 0
sodem = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(iphaotrong,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(iphaongoai,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(ozon,GPIO.OUT)
GPIO.setup(obomtrong,GPIO.OUT)
GPIO.setup(obomngoai,GPIO.OUT)
GPIO.setup(ohoachat,GPIO.OUT)
GPIO.setup(osuckhi,GPIO.OUT)
GPIO.setup(ouv,GPIO.OUT)
def some_job():
	#c = ser.readline()
	#print (c)
	global sodem,isdem
	threading.Timer(1.0,some_job).start()
	if (isdem == 1):
		sodem=sodem+1
	if(GPIO.input(iphaongoai)==1 and GPIO.input(iphaotrong) ==1 and ison!=0):
		GPIO.output(obomtrong,1)
		isdem=1
	if(sodem>10 and ison!=0):
		GPIO.output(ohoachat,1)
		GPIO.output(osuckhi,1)
	if(sodem>15 and ison!=0):
		GPIO.output(ohoachat,0)
	if(GPIO.input(iphaotrong) == 0 and ison!= 0):
		GPIO.output(obomngoai,1)
	if(sodem>25 and ison!=0):
		GPIO.output(ouv,1)
		GPIO.output(ozon,1)
	if(sodem>35 and ison!=0 and GPIO.input(iphaotrong)==1):
		GPIO.output(obomtrong,1)
		GPIO.output(osuckhi,0)
		GPIO.output(ozon,0)
		GPIO.output(ouv,0)
	if(sodem>45 and ison!=0 and GPIO.input(iphaotrong)==0):
		GPIO.output(obomtrong,0)
		isdem=0
		sodem=0
def on():
	print ("on")
	GPIO.output(a,True)
def vuong(channel):
	print ("ngat")
 
class Ui_MainWindow(object):
    def off():
        print ("off")
        GPIO.output(a,False)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
 m       self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 150, 201, 181))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 160, 201, 181))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "on"))
        self.pushButton_2.setText(_translate("MainWindow", "off"))
        self.pushButton.clicked.connect(on)
        self.pushButton_2.clicked.connect(self.off)
        some_job()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
