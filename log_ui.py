# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Log_UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Log(object):
    def setupUi(self, Log):
        Log.setObjectName("Log")
        Log.resize(480, 600)
        self.textBrowser = QtWidgets.QTextBrowser(Log)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 481, 601))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Log)
        QtCore.QMetaObject.connectSlotsByName(Log)

    def retranslateUi(self, Log):
        _translate = QtCore.QCoreApplication.translate
        Log.setWindowTitle(_translate("Log", "Form"))

