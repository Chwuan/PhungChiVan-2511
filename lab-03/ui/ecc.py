# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/ecc.ui'
#
# Created by: PyQt5 UI code generator 5.15.11

from PyQt5 import QtCore, QtGui, QtWidgets
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "../platforms"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 315)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(100, 10, 180, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setObjectName("lblTitle")
        
        self.btn_gen_keys = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gen_keys.setGeometry(QtCore.QRect(290, 15, 110, 23))
        self.btn_gen_keys.setObjectName("btn_gen_keys")
        
        self.txtInformation = QtWidgets.QLabel(self.centralwidget)
        self.txtInformation.setGeometry(QtCore.QRect(10, 70, 80, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtInformation.setFont(font)
        self.txtInformation.setObjectName("txtInformation")
        
        self.txt_info = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_info.setGeometry(QtCore.QRect(100, 70, 300, 71))
        self.txt_info.setObjectName("txt_info")
        
        self.txtSignature = QtWidgets.QLabel(self.centralwidget)
        self.txtSignature.setGeometry(QtCore.QRect(10, 160, 80, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtSignature.setFont(font)
        self.txtSignature.setObjectName("txtSignature")
        
        self.txt_sign = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_sign.setGeometry(QtCore.QRect(100, 160, 300, 71))
        self.txt_sign.setObjectName("txt_sign")
        
        self.btn_sign = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sign.setGeometry(QtCore.QRect(120, 250, 90, 25))
        self.btn_sign.setObjectName("btn_sign")
        
        self.btn_verify = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verify.setGeometry(QtCore.QRect(260, 250, 90, 25))
        self.btn_verify.setObjectName("btn_verify")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 420, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ECC Cipher App"))
        self.lblTitle.setText(_translate("MainWindow", "ECC CIPHER"))
        self.txtInformation.setText(_translate("MainWindow", "Information:"))
        self.txtSignature.setText(_translate("MainWindow", "Signature:"))
        self.btn_sign.setText(_translate("MainWindow", "Sign"))
        self.btn_verify.setText(_translate("MainWindow", "Verify"))
        self.btn_gen_keys.setText(_translate("MainWindow", "Generate Keys"))
