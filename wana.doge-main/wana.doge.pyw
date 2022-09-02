import sys
import ctypes
import os
import subprocess
import time
from PyQt5 import QtCore, QtGui, QtWidgets

import webbrowser
#WEBBROWSER OPEN ABOUT BTC
def AB_BTC():
        ab_BTC_URL="https://en.wikipedia.org/wiki/Bitcoin"
        webbrowser.open_new(ab_BTC_URL)

#WEBBROWSER OPEN WHERE TO BUY BTC
def HTB_BTC():
        HTB_BTC_URL="https://bitcoin.org/en/buy"
        webbrowser.open_new(HTB_BTC_URL)

class Ui_Main_window(object):
    def setupUi(self, Main_window):
        #change background
        dirname = os.path.dirname(__file__)
        Background_path = os.path.join(dirname, 'res/rthtzjtzjtzjtzj.jpg')
        ctypes.windll.user32.SystemParametersInfoW(20, 0, Background_path , 0)
        #open window
        Main_window.setObjectName("Main_window")
        Main_window.resize(820, 515)
        Main_window.setMinimumSize(QtCore.QSize(820, 515))
        Main_window.setMaximumSize(QtCore.QSize(820, 515))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/ico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Main_window.setWindowIcon(icon)
        self.background = QtWidgets.QLabel(Main_window)
        self.background.setGeometry(QtCore.QRect(0, 0, 821, 521))
        self.background.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.background.setFrameShape(QtWidgets.QFrame.Box)
        self.background.setText("")
        self.background.setObjectName("background")
        self.logo = QtWidgets.QLabel(Main_window)
        self.logo.setGeometry(QtCore.QRect(30, 20, 181, 181))
        self.logo.setStyleSheet("background-image: url(:/logo/ico.png);")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.comboBox = QtWidgets.QComboBox(Main_window)
        self.comboBox.setGeometry(QtCore.QRect(720, 20, 101, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(Main_window)
        self.label.setGeometry(QtCore.QRect(190, 0, 531, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Main_window)
        self.pushButton.setGeometry(QtCore.QRect(560, 470, 261, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Main_window)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 470, 261, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame = QtWidgets.QFrame(Main_window)
        self.frame.setGeometry(QtCore.QRect(260, 380, 551, 81))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(50)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 105, 31))
        self.label_2.setStyleSheet("background-image: url(:/BTC_a_here/btc_a_here.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 234, 2);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(120, 40, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_4.setFont(font)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setObjectName("label_4")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_3.setGeometry(QtCore.QRect(120, 40, 401, 31))
        self.textBrowser_3.setAcceptDrops(False)
        self.textBrowser_3.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.textBrowser_3.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_3.setLineWidth(1)
        self.textBrowser_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_5 = QtWidgets.QLabel(Main_window)
        self.label_5.setGeometry(QtCore.QRect(260, 50, 551, 321))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.textBrowser = QtWidgets.QTextBrowser(Main_window)
        self.textBrowser.setGeometry(QtCore.QRect(20, 431, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        self.textBrowser.setFont(font)
        self.textBrowser.setAcceptDrops(False)
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setStyleSheet("background-color: rgb(168, 0, 0);")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser.setReadOnly(False)
        self.textBrowser.setOpenExternalLinks(False)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Main_window)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 460, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setAcceptDrops(False)
        self.textBrowser_2.setAutoFillBackground(False)
        self.textBrowser_2.setStyleSheet("background-color: rgb(168, 0, 0);")
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_2.setReadOnly(False)
        self.textBrowser_2.setOpenExternalLinks(False)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_6 = QtWidgets.QLabel(Main_window)
        self.label_6.setGeometry(QtCore.QRect(260, 30, 551, 121))
        font = QtGui.QFont()
        font.setPointSize(69)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Main_window)
        self.label_7.setGeometry(QtCore.QRect(260, 250, 551, 121))
        font = QtGui.QFont()
        font.setPointSize(69)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Main_window)
        self.label_8.setGeometry(QtCore.QRect(260, 140, 551, 121))
        font = QtGui.QFont()
        font.setPointSize(69)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.frame_2 = QtWidgets.QFrame(Main_window)
        self.frame_2.setGeometry(QtCore.QRect(10, 210, 221, 181))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(1)
        self.frame_2.setObjectName("frame_2")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 234, 2);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(0, 29, 221, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(0, 70, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(0, 80, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.ABOUT_BTC_B = QtWidgets.QPushButton(Main_window)
        self.ABOUT_BTC_B.setGeometry(QtCore.QRect(10, 430, 111, 31))
        self.ABOUT_BTC_B.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:1 rgba(0, 0, 0, 0));")
        self.ABOUT_BTC_B.setText("")
        self.ABOUT_BTC_B.setFlat(True)
        self.ABOUT_BTC_B.setObjectName("ABOUT_BTC_B")
        self.HOW_B_BTC_B = QtWidgets.QPushButton(Main_window)
        self.HOW_B_BTC_B.setGeometry(QtCore.QRect(10, 460, 131, 31))
        self.HOW_B_BTC_B.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:1 rgba(0, 0, 0, 0));")
        self.HOW_B_BTC_B.setText("")
        self.HOW_B_BTC_B.setFlat(True)
        self.HOW_B_BTC_B.setObjectName("HOW_B_BTC_B")

        self.retranslateUi(Main_window)
        QtCore.QMetaObject.connectSlotsByName(Main_window)

    def retranslateUi(self, Main_window):
        _translate = QtCore.QCoreApplication.translate
        Main_window.setWindowTitle(_translate("Main_window", "wana.doge Decrypt0r 1.2"))
        self.comboBox.setItemText(0, _translate("Main_window", "English"))
        self.comboBox.setItemText(1, _translate("Main_window", "learn English"))
        self.label.setText(_translate("Main_window", " ⠀⠀Oops, your files were not encrypted!"))
        self.pushButton.setText(_translate("Main_window", "do nothing."))
        self.pushButton_2.setText(_translate("Main_window", "do nothing."))
        self.label_3.setText(_translate("Main_window", " ⠀⠀Send $2 worth of bitcoin to this address:"))
        self.label_4.setText(_translate("Main_window", "bc1qz5q86hrj4n983vxey3mxrrd7227ueacdfz56c9"))
        self.textBrowser_3.setHtml(_translate("Main_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"NO_CLICK\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">bc1q59kz2vyhqnq4ytqc0932avfdy0z6ys6780vert</span></a></p></body></html>"))
        self.textBrowser.setHtml(_translate("Main_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://en.wikipedia.org/wiki/Bitcoin\"><span style=\" text-decoration: underline; color:#0000ff;\">About bitcoin</span></a></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Main_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://bitcoin.org/en/buy\"><span style=\" text-decoration: underline; color:#0000ff;\">How to buy bitcoins?</span></a></p></body></html>"))
        self.label_6.setText(_translate("Main_window", "you"))
        self.label_7.setText(_translate("Main_window", "DUM!"))
        self.label_8.setText(_translate("Main_window", "dum"))
        self.label_9.setText(_translate("Main_window", "Your files will not be lost on"))
        self.label_10.setText(_translate("Main_window", "09/99/2999 99:99:99"))
        self.label_11.setText(_translate("Main_window", "Time Left"))
        self.label_12.setText(_translate("Main_window", "99:99:99:99"))

        #BUTTONS
        self.ABOUT_BTC_B.clicked.connect(lambda: AB_BTC())
        self.HOW_B_BTC_B.clicked.connect(lambda: HTB_BTC())

#import resources
import res.res_rc


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Main_window()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())