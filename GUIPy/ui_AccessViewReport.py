# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AccessViewReportQYHIaj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sqlite3

class Ui_AccessView(object):
    def loadData(self):
        conn=sqlite3.connect('./DataBaseTable.db')
        query='SELECT * FROM EmployeeAccess'
        result=conn.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, colum_number, QTableWidgetItem(str(data)))

        conn.close()
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(824, 565)
        Form.setStyleSheet(u"background:rgb(250, 249, 246)")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 30, 241, 31))
        self.label.setStyleSheet(u"font: 25 20pt \"Bahnschrift Light\";\n"
"background:rgb(250, 249, 246)")
        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 70, 521, 431))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(420, 520, 75, 23))
        self.backaccrep_btn = QPushButton(Form)
        self.backaccrep_btn.setObjectName(u"backaccrep_btn")
        self.backaccrep_btn.setGeometry(QRect(90, 520, 75, 23))
        self.lineEdit_accrep = QLineEdit(Form)
        self.lineEdit_accrep.setObjectName(u"lineEdit_accrep")
        self.lineEdit_accrep.setGeometry(QRect(500, 10, 151, 21))
        self.searchaccrep = QPushButton(Form)
        self.searchaccrep.setObjectName(u"searchaccrep")
        self.searchaccrep.setGeometry(QRect(670, 10, 75, 23))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(510, 40, 141, 21))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Access Report View", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Emp_ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Gate_ID", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"AccessSchemeID", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"AllowedJobs", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Category", None));
        self.pushButton.setText(QCoreApplication.translate("Form", u"Save", None))
        self.backaccrep_btn.setText(QCoreApplication.translate("Form", u"Back", None))
        self.searchaccrep.setText(QCoreApplication.translate("Form", u"Search", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Search by Emp ID", None))
    # retranslateUi

