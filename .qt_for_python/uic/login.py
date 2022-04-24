# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_loginWindow(object):
    def setupUi(self, loginWindow):
        if not loginWindow.objectName():
            loginWindow.setObjectName(u"loginWindow")
        loginWindow.resize(503, 535)
        loginWindow.setStyleSheet(u"font: 25 18pt \"Bahnschrift Light\";\n"
"background:rgb(250, 249, 246)\n"
"")
        self.groupBox = QGroupBox(loginWindow)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(100, 70, 271, 401))
        font = QFont()
        font.setFamily(u"Bahnschrift Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"font: 25 20pt \"Bahnschrift Light\";\n"
"background:rgb(250, 249, 246)\n"
"")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.user_line = QLineEdit(self.groupBox)
        self.user_line.setObjectName(u"user_line")
        self.user_line.setFont(font)
        self.user_line.setStyleSheet(u"\n"
"border-width: 1px; border-radius: 4px;\n"
"background-color: rgb(255, 255, 255);\n"
"	border-style: solid;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));")
        self.user_line.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.user_line, 0, 0, 1, 1)

        self.login_btn = QPushButton(self.groupBox)
        self.login_btn.setObjectName(u"login_btn")
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(9)
        self.login_btn.setFont(font1)
        self.login_btn.setStyleSheet(u"QPushButton{\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, st"
                        "op:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 21"
                        "5), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(142,142,142);\n"
"}\n"
"QPushButton:disabled{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: #808086;\n"
"	padding: 2px;\n"
"	background-color: rgb(142,142,142);\n"
"}")

        self.gridLayout.addWidget(self.login_btn, 2, 0, 1, 1)

        self.pass_line = QLineEdit(self.groupBox)
        self.pass_line.setObjectName(u"pass_line")
        self.pass_line.setFont(font)
        self.pass_line.setStyleSheet(u"\n"
"border-width: 1px; border-radius: 4px;\n"
"background-color: rgb(255, 255, 255);\n"
"	border-style: solid;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));")
        self.pass_line.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.pass_line, 1, 0, 1, 1)

        QWidget.setTabOrder(self.user_line, self.pass_line)
        QWidget.setTabOrder(self.pass_line, self.login_btn)

        self.retranslateUi(loginWindow)

        QMetaObject.connectSlotsByName(loginWindow)
    # setupUi

    def retranslateUi(self, loginWindow):
        loginWindow.setWindowTitle(QCoreApplication.translate("loginWindow", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("loginWindow", u"Login", None))
        self.user_line.setPlaceholderText(QCoreApplication.translate("loginWindow", u"User Name..", None))
        self.login_btn.setText(QCoreApplication.translate("loginWindow", u"Login", None))
#if QT_CONFIG(shortcut)
        self.login_btn.setShortcut(QCoreApplication.translate("loginWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.pass_line.setPlaceholderText(QCoreApplication.translate("loginWindow", u"Password..", None))
    # retranslateUi

