from multiprocessing.sharedctypes import Value
import sys

from xlsxwriter import Workbook
import csv
from PyQt5.uic import loadUi ,loadUiType
from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QDialog, QApplication, QWidget
# from PyQt5.QtGui import QPixmap
import os
from os import path
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sqlite3
from datetime import date
from datetime import datetime
import numpy as np
import pandas as pd
from PIL import Image
from classifier import training
import cv2
from mtcnn.mtcnn import MTCNN
import time
import re
'''
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import * 

any import link this will be replaced with 

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

there is two way to load GUI 
1) from-->  loadUi("./GUI/filename.ui",self) # load the GUI file
 
2) loading the python file of the gen design and import the class name 
    ex: step 1) from GUI.ui_welcome import Ui_WelcomeWindow  --> GUI is the folder . python file import the class

 

'''


from GUIPy.ui_companyinfo import Ui_Form
# IMPORT FUNCTIONS

# from ui_functions import *
from GUIPy.ui_welcome import Ui_WelcomeWindow 
from GUIPy.ui_employee import Ui_employeeWindow
from GUIPy.ui_login import Ui_loginWindow
from GUIPy.ui_MainMenue import Ui_MainWindow
from GUIPy.ui_newemployee import Ui_newemp1
from GUIPy.ui_newemployee2 import Ui_newemp2
from GUIPy.ui_newuser import Ui_newuser
from GUIPy.ui_CompanyMenue import Ui_CompanyMenuForm
from GUIPy.ui_TrainModelScreen import Ui_ModelTraining
from GUIPy.ui_AccessViewReport import Ui_AccessView
from GUIPy.ui_AttendanceViewReport import Ui_AttendanceView
from GUIPy.ui_ViewReport import Ui_ViewRep



def convert(filename):
    with open(filename, 'rb') as file:
        photo = file.read()
    return photo


class WelcomeScreen(QDialog):

    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_WelcomeWindow()
        self.ui.setupUi(self)
        self.ui.login_btn.clicked.connect(self.gotologin)
        self.setFixedWidth(550)
        self.setFixedHeight(661)
        self.setGeometry(50,50,371,661)
    
    def gotologin(self):

        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(548)
        widget.setFixedHeight(660)
        widget.setGeometry(50,50,1538,926)
        widget.setWindowTitle("Login Screen")
        
######################################################## StartUpWondow #############################################

######################################################## LoginScreen #############################################
class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("./GUI/login.ui",self)
        self.setFixedWidth(548)
        self.setFixedHeight(755)
        self.setGeometry(50,50,548,755)

        self.pass_line.setEchoMode(QtWidgets.QLineEdit.Password)

        self.login_btn.clicked.connect(self.loginfunction)
        #self.CancelButton.clicked.connect(self.goBack)

        self.setWindowTitle("Login")
        #self.mainwin=MainWin()


    def loginfunction(self):

        self.user = self.user_line.text()

        self.password = self.pass_line.text()


        if len(self.user)==0 or len(self.password)==0:
            QMessageBox.about(self,"Error","Please input all fields.")

        else:
            
            conn = sqlite3.connect("./DataBaseTable.db")
            cur = conn.cursor()
            #-----username= admin password 1234
            query = 'SELECT User_Password,User_type FROM Users WHERE User_Name =\''+self.user+"\'"
            cur.execute(query)
            query_result  = cur.fetchall()
            for row in query_result:
                self.password=row[0]
                self.user_Type=row[1]

                if self.password is not None:
                    if self.password == self.password:
                        QMessageBox.about(self, "alert", "Successfully logged in \n"+self.user)
                        print("Successfully logged in.")
                        self.gotomaintest(self.user_Type)
                    else:
                        QMessageBox.about(self,"Error","Invalid username or password")
                        # self.error.setText("Invalid username or password")
                else:        
                    QMessageBox.about(self,"Error","Invalid username or password")
                


    def gotomaintest(self,user_type):
        mainwint=MainWin()
        mainwint.userType.emit(user_type)
        widget.addWidget(mainwint)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(861)
        widget.setFixedHeight(605)
        widget.setGeometry(50,50,861,605)
        widget.setWindowTitle("Main Screen")

######################################################## EndCompanyInformationWindow #############################################   
         
######################################################## MainWindow #############################################

class MainWin(QDialog):
    userType=pyqtSignal(int)
    def __init__(self):    
        QWidget.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.type=0
        self.userType.connect(self.getuserType)

        # self.getuserType()
        self.ui.employee_btn.clicked.connect(self.gotoemp)
        self.ui.comp_btn.clicked.connect(self.gotoCompanyInfo)
        self.ui.nuser_btn.clicked.connect(self.gotoAddUser)
        self.ui.train_btn.clicked.connect(self.gotoTrain)

        #self.TakeAtt.clicked.connect(Attendace)
        #self.logoutButton.clicked.connect(self.gotoWelcome)
        #self.Exit.clicked.connect(self.Exitsys)

        # self.setFixedWidth(1200)
        # self.setFixedHeight(1200)
    
    def getuserType(self,userType):
        if userType==2:
            self.ui.train_btn.setEnabled(False)
            self.type=userType
        else:
            pass
    def gotoAddUser(self):  
        createProfile=AddNewUser()
        widget.addWidget(createProfile)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setWindowTitle("Add User")

    def gotoemp(self):
        EmpScreen = EmployeeMenu()
        EmpScreen.userType.emit(self.type)
        widget.addWidget(EmpScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)
       
  
    def gotoCompanyInfo(self):
        CompInfo = CompanyMeua()
        widget.addWidget(CompInfo)
        widget.setCurrentIndex(widget.currentIndex() + 1) 
        widget.setWindowTitle("Company Information ")
    
    def gotoTrain(self):
        TrainS = TrainScreen()
        widget.addWidget(TrainS)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setWindowTitle("Model Training")

############################################################################################################

class EmployeeMenu(QDialog):
    userType=pyqtSignal(int)
    def __init__(self):    
        QWidget.__init__(self)
        self.ui=Ui_employeeWindow()
        self.ui.setupUi(self)
        self.type=0
        self.ui.report_btn.clicked.connect(self.viewreportmenu)
        self.ui.add_btn.clicked.connect(self.gotonewemployee)
        self.ui.edit_btn.clicked.connect(self.gotoeditemployee)
        self.ui.check_btn.clicked.connect(self.gotoCheck)
        
        # self.ui.report_btn.clicked.connect(self.gotoReport)
        
        self.ui.back_btn.clicked.connect(self.gotomainmenu)
        
        self.userType.connect(self.getuserType)

    def viewreportmenu(self):
        Newviewreport = viewreportmenu()
        widget.addWidget(Newviewreport)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setWindowTitle("Report Menu")


    # def getuserType(self,userType):
    #     if userType==2:
    #         self.ui.edit_btn.setEnabled(False)
    #         self.type=userType
    #     else:
    #         pass
    def gotonewemployee(self):
        NewEmpScreen = NewEmployee()
        widget.addWidget(NewEmpScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setWindowTitle("New Employee")
    
    def gotomainmenu(self):
        mainwint=MainWin()
        mainwint.userType.emit(self.type)
        widget.addWidget(mainwint)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(861)
        widget.setFixedHeight(605)
        widget.setGeometry(50,50,861,605)
        widget.setWindowTitle("Main Screen")
   
    def gotoeditemployee(self):
       EditEmployeescreen = EditEmployee()
       widget.addWidget(EditEmployeescreen)
       widget.setCurrentIndex(widget.currentIndex() + 1)
       widget.setWindowTitle("Edit Employee")

    def gotoCheck(self):
        print("will be added soon ")
    
    def gotoReport(self):
        print("will be added soon ")


###########################################################################################
class CompanyMeua(QDialog):
    def __init__(self):
        QWidget.__init__(self)
        self.companyUI=Ui_CompanyMenuForm()
        self.companyUI.setupUi(self)

        self.companyUI.addCompany_btn.clicked.connect(self.AddCompanyInfo)
        self.companyUI.edit_btn.clicked.connect(self.EditCompanyInfo)
        self.companyUI.back_btn.clicked.connect(self.goBack)

    def AddCompanyInfo(self):
        compInfo = CompanyInfo()
        widget.addWidget(compInfo)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setWindowTitle("CompanyInfo")
    def EditCompanyInfo(self):
        editCompanyInfo = editcompany()
        widget.addWidget(editCompanyInfo)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setWindowTitle("EditComapny")
    
    def goBack(self):
        mainWin =MainWin()
        mainWin.userType.emit()
        widget.addWidget(mainWin)
        widget.setCurrentIndex(widget.currentIndex() + 1)
   
####################################################################################################

##################################################################################################

class NewEmployee(QDialog):
    ImageUpdate = pyqtSignal(QImage)
    def __init__(self):
        QWidget.__init__(self)
        
        self.FirstUi=Ui_newemp1()
        self.FirstUi.setupUi(self)
        self.FirstUi.stackedWidget.setCurrentWidget(self.FirstUi.BasicInfoPage)
        self.getCompayinfo()  
        self.cleanImage()
        self.removeButtons()
        self.handelButtons()
        # self.handel_Lines()
        self.ImageUpdate.connect(self.ImageUpdateSlot)

        self.capture_Emp_ID=''
        self.emailregx=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
        widget.setFixedWidth(960)
        widget.setFixedHeight(830)

        self.phone=self.FirstUi.phone_line_3.setValidator(QIntValidator())
        self.phone=self.FirstUi.phone_line_3.text()
        
        self.search=self.FirstUi.searchbar.text()
        self.DOB=self.FirstUi.date_3.date().toPyDate()

        self.photo=self.FirstUi.photoview_3.isVisible()

    def handelButtons(self):
        self.FirstUi.cancel_btn_3.clicked.connect(self.gotoempmenu)
        self.FirstUi.Start_btn.clicked.connect(self.CaputerEmployeeDataset)
        self.FirstUi.Next2Cap.clicked.connect(self.nextToCapture)
        self.FirstUi.New_btn.clicked.connect(self.addNewEmployee)
        self.FirstUi.Back.clicked.connect(self.next2Empinfo)
        self.FirstUi.Next_btn.clicked.connect(self.next2Empinfo)
        self.FirstUi.save_btn.clicked.connect(self.SaveOnDataBase)
        self.FirstUi.Back2basic.clicked.connect(self.Back2Basic)
        self.FirstUi.back_btn_3.clicked.connect(self.gotoempmenu)
        self.FirstUi.AddPhoto.clicked.connect(self.BrowseImage)

    def removeButtons(self):
        self.FirstUi.searchbar.setVisible(False)
        self.FirstUi.search_btn.setVisible(False)
        self.FirstUi.delete_btn_3.setVisible(False)
        self.FirstUi.update_btn.setVisible(False)
        self.FirstUi.New_btn.setVisible(False)
        self.FirstUi.save_btn.setVisible(False)

    def cleanImage(self):
        self.imgpath=""
        self.FirstUi.photoview_3.setPixmap(QPixmap("Avatar.png"))   
   
    def nextToCapture(self):
        self.dep=self.FirstUi.dep_drop_3.currentText()
        self.jobTitle=self.FirstUi.job_drop_3.currentText()
        self.attendSch=self.FirstUi.att_drop_3.currentText()
        self.accessCat=self.FirstUi.acc_drop_3.currentText()
        if (self.dep or self.jobTitle or self.attendSch or self.accessCat)=='':
            QMessageBox.about(self,"Missing Information","Select ")
        else:
            self.FirstUi.stackedWidget.setCurrentWidget(self.FirstUi.CapturePage)
     
    def ImageUpdateSlot(self, Image):
            self.FirstUi.label_25.setPixmap(QPixmap.fromImage(Image))
            self.FirstUi.label_25.setScaledContents(True)

    def BrowseImage(self):

        filename = QFileDialog.getOpenFileName(self,'Open File','D\\','Image files (*.jpg *.png *.jpeg)')
        self.imgpath=filename[0]
        pixmap=QPixmap(self.imgpath)
        self.FirstUi.photoview_3.setPixmap(pixmap)
        self.FirstUi.photoview_3.setScaledContents(True)
        
    def Back2Basic(self):
        self.FirstUi.stackedWidget.setCurrentWidget(self.FirstUi.BasicInfoPage)
  
    def next2Empinfo(self):
        self.firstname1=self.FirstUi.first_line_3.text()
        self.middlename1=self.FirstUi.middle_line_3.text()
        self.lastname1=self.FirstUi.last_line_3.text()
        self.email=self.FirstUi.email_line_3.text()
        self.Malegender=self.FirstUi.MaleRadio_3.isChecked()
        self.Femalegender=self.FirstUi.FemaleRadio_3.isChecked()
        self.address=self.FirstUi.address_line_3.text()
        if len(self.middlename1)==0 or len(self.firstname1)==0 or len(self.lastname1)==0 or len(self.address)==0 or len(self.email)==0:
            QMessageBox.about(self,"Error","Please Enter Employee data")
        elif self.Malegender==False and self.Femalegender==False:
            QMessageBox.about(self,"Missing Data","Please Enter Employee Gender")
        elif not (re.fullmatch(self.emailregx,self.email)):
            QMessageBox.warning(self,"Email Verfication","Email Format is incorrect.",QMessageBox.Ok)
        else:
            self.FirstUi.stackedWidget.setCurrentWidget(self.FirstUi.EmployeeDataPage)
    
    def addNewEmployee(self):
        self.cleanImage()
        self.FirstUi.stackedWidget.setCurrentWidget(self.FirstUi.BasicInfoPage)

    def gotoempmenu(self):
        EmpScreen = EmployeeMenu()
        widget.addWidget(EmpScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setWindowTitle(" Employee Menu")

    def handel_Lines(self):
        self.FirstUi.first_line_3.clear()
        self.FirstUi.middle_line_3.clear()
        self.FirstUi.last_line_3.clear()
        self.FirstUi.address_line_3.clear()
        self.FirstUi.phone_line_3.clear()
        self.FirstUi.email_line_3.clear()
        self.FirstUi.MaleRadio_3.setCheckable(False)
        self.FirstUi.FemaleRadio_3.setCheckable(False)
        self.FirstUi.dep_drop_3.clear()
        self.FirstUi.job_drop_3.clear()
        self.FirstUi.acc_drop_3.clear()
        self.FirstUi.att_drop_3.clear()
        
    def genID(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "DataBaseTable.db")
        with sqlite3.connect(db_path) as db:
            cursor=db.cursor()
           
            for row in cursor.execute('SELECT Emp_ID FROM Employees ORDER BY Emp_ID DESC LIMIT 1;'):
                #print(row)
                printIDint=int(row[0])
                printIDint+=1
                printIDstr=str(printIDint)
                self.capture_Emp_ID=printIDstr   


    def getCompayinfo(self):

        conn = sqlite3.connect("./DataBaseTable.db")
        conn.text_factory=str
        cursor = conn.cursor()
            
        cursor.execute('SELECT Dept_Name FROM DepartmentsTable;')
        dept_names=cursor.fetchall()
        dept_names1=[r[0] for r in dept_names]

        cursor.execute('SELECT JobDesc FROM JobTittle;')
        JobTitles=cursor.fetchall()
        JobTitles1=[r[0] for r in JobTitles]

        cursor.execute('SELECT AttendanceDesc FROM Attendance_Schemes_Table;')
        attendanceSchem=cursor.fetchall()
        attendanceSchem1=[r[0] for r in attendanceSchem]

        cursor.execute('SELECT Category FROM AccessScheme;')
        accesSchem=cursor.fetchall()
        accesSchem1=[r[0] for r in accesSchem]


        deptlen=len(dept_names1)
        joblen=len(JobTitles1)
        attendanceSchLen=len(attendanceSchem1)
        accesSchemLen=len(accesSchem1)

        if dept_names1 == []:
            print("you cant add New Employee you must First ADD Company Dept's")
           
        else:
            count=0
            self.FirstUi.dep_drop_3.addItem("")
            for i in range (deptlen):
                
                self.FirstUi.dep_drop_3.addItem(dept_names1[count])
                count+=1


        if  JobTitles == []:
            print("you cant add New Employee you must First ADD Company Job Titles's")
           
            self.FirstUi.save_btn_3.setEnabled(False)     
        else:
            count=0
            self.FirstUi.job_drop_3.addItem("")
            for i in range (joblen):
                self.FirstUi.job_drop_3.addItem(JobTitles1[count])
                count+=1      

        if attendanceSchem1 ==[]:
            print("you cant add New Employee you must First ADD Company attendance Schem")
                 
        else:
            count=0 
            self.FirstUi.att_drop_3.addItem("")
            for i in range (attendanceSchLen):
                self.FirstUi.att_drop_3.addItem(attendanceSchem1[count])
                count+=1    

        if accesSchem1 ==[]:
            print("you cant add New Employee you must First ADD Company Access Schem")  
                  
        else:
            count=0 
            self.FirstUi.acc_drop_3.addItem("")
            for i in range (accesSchemLen):
                self.FirstUi.acc_drop_3.addItem(accesSchem1[count])
                count+=1  

    def CheckInputs(self):
       
        if len(self.middlename1)==0 or len(self.firstname1)==0 or len(self.lastname1)==0 or len(self.address)==0 or len(self.email)==0:
            QMessageBox.about(self,"Error","Please Enter Employee data")

        elif self.Malegender==False and self.Femalegender==False:
            QMessageBox.about(self,"Missing Data","Please Enter Employee Gender")

   
    def EmailTyping(self):
        self.FirstUi.email_line_3.textChanged.connect(self.EmailTyping)
        if not (self.FirstUi.email_line_3.hasAcceptableInput()):
            self.FirstUi.email_line_3.setStyleSheet("QLineEdit { color: red;}")
        else:
            self.FirstUi.email_line_3.setStyleSheet("QLineEdit { color: black;}")
        
  
    def SaveOnDataBase(self):
        conn = sqlite3.connect("./DataBaseTable.db")
        conn.text_factory=str
        cursor = conn.cursor()

   
        self.firstname1=self.FirstUi.first_line_3.text()
        self.middlename1=self.FirstUi.middle_line_3.text()
        self.lastname1=self.FirstUi.last_line_3.text()
        self.Malegender=self.FirstUi.MaleRadio_3.isChecked()
        self.Femalegender=self.FirstUi.FemaleRadio_3.isChecked()
        
        self.address=self.FirstUi.address_line_3.text()
        self.phone=self.FirstUi.phone_line_3.text()
        self.email=self.FirstUi.email_line_3.text()
        self.DOB=self.FirstUi.date_3.date().toPyDate()

        

       
        if self.Malegender==True:
            self.Putgender="M"
        else:
            self.Putgender="F"
        
      

        self.dep=self.FirstUi.dep_drop_3.currentText()
        self.jobTitle=self.FirstUi.job_drop_3.currentText()
        self.attendSch=self.FirstUi.att_drop_3.currentText()
        self.accessCat=self.FirstUi.acc_drop_3.currentText()
        

        dep_query = 'SELECT Dept_ID FROM DepartmentsTable WHERE Dept_Name =\''+self.dep+"\'"
        cursor.execute(dep_query)
        dep_query_result  = cursor.fetchone()
        # dep_query_result_str=[r[0] for r in dep_query_result]

        Job_query = 'SELECT Emp_Job_ID FROM JobTittle WHERE JobDesc =\''+self.jobTitle+"\'"
        cursor.execute(Job_query)
        Job_query_result  = cursor.fetchone()
        #Job_query_result_str=[r[0] for r in Job_query_result]

        attendSch_query = 'SELECT AttendanceSchemes_ID FROM Attendance_Schemes_Table WHERE AttendanceDesc =\''+self.attendSch+"\'"
        cursor.execute(attendSch_query)
        attendSch_query_result  = cursor.fetchone()
        #attendSch_query_result_str=[r[0] for r in attendSch_query_result]

        AccessCat_query = 'SELECT AccessSchemID FROM AccessScheme WHERE Category =\''+self.accessCat+"\'"
        cursor.execute(AccessCat_query)
        AccessCat_query_result  = cursor.fetchone()
        #AccessCat_query_result_str=[r[0] for r in AccessCat_query_result]

        GateID_query = 'SELECT GateID FROM AccessScheme WHERE Category =\''+self.accessCat+"\'"
        cursor.execute(GateID_query)
        GateID_query_result  = cursor.fetchone()


        if self.imgpath=="":
            QMessageBox.about(self, "alert", "please put Employee Photo ")
        else:
            print(self.imgpath)
            self.PhotoB=convert(self.imgpath)
      

            if dep_query_result is None :
                QMessageBox.about(self, "alert", "Please Fill All The Missing Parts ")
                
            if len(self.middlename1)==0 or len(self.firstname1)==0 or len(self.lastname1)==0 or len(self.address)==0 or len(self.email)==0:
                QMessageBox.about(self,"Error","Please Enter Employee Data")

            elif dep_query_result  is not None:
                Emp_info=[self.firstname1,self.middlename1,self.lastname1,self.Putgender,self.address,self.email,dep_query_result[0],Job_query_result[0],self.PhotoB,attendSch_query_result[0],AccessCat_query_result[0],str(self.phone),self.DOB]

                cursor.execute("INSERT INTO Employees(Emp_First_Name,Emp_Middle_Name,Emp_Last_Name,Emp_Gender,Emp_Address,Emp_email,Emp_Dpet_ID,Emp_Job_ID,Emp_Photo,Emp_Attendace_SchemeID,Emp_Access_ID,Emp_PhoneNumber,Emp_DOB) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);",Emp_info)

                for row in cursor.execute('SELECT Emp_ID FROM Employees ORDER BY Emp_ID DESC LIMIT 1;'):
                    #print(row)
                    printIDint=int(row[0])
                    #printIDint+=1
                    printIDstr=str(printIDint)
                    self.capture_Emp_ID=printIDstr  
                    Arr=[self.capture_Emp_ID,GateID_query_result[0],AccessCat_query_result[0],self.accessCat]
                    cursor.execute("INSERT INTO EmployeeAccess(Emp_ID,Gate_ID,AcessSchemeID,Cat) VALUES (?,?,?,?);",Arr)
                    QMessageBox.about(self, "alert", "Employee Added its ID"+self.capture_Emp_ID)
                    # NewEmployee.genID(self)
                    self.handel_Lines()
                self.FirstUi.stackedWidget.setCurrentWidget(self.FirstUi.CapturePage)
 
                conn.commit()
                conn.close()

            else:
                QMessageBox.about(self, "alert", "please Fill All the Missing Parts ")

                conn.commit()
                conn.close()
    
    def CaputerEmployeeDataset(self):
        Detector=MTCNN()
        self.genID()
        count=0
        Camera=cv2.VideoCapture(0)
        if (Camera.isOpened()==False):
            QMessageBox.warning(self,"Camera Not Found","Please Check Camera Inputs",QMessageBox.Ok)
        else:
            while True:
                ret,frame=Camera.read()
                if ret == True:
                    location=Detector.detect_faces(frame)
                    cropfame=frame
                    DatasetFolder="./DataSet/"+str(self.firstname1)+'.'+str(self.capture_Emp_ID)
                    if not os.path.exists(DatasetFolder):
                        os.makedirs(DatasetFolder)
                    imgpath=DatasetFolder+"/img"+str(count)+".jpg"
                if len(location) == 1 :
                    self.FirstUi.Error.setText("Please Rotate Your Head in all Directions")
                    for face in location:
                        count+=1
                        # filenamepath=name_ID+'/img'+str(count)+".jpg"
                        x, y, width, height = face['box']
                        x2, y2 = x + width, y + height
                        xmin,xmax=x,x2
                        ymin,ymax=y,y2
                        cropfame=frame[ymin:ymax,xmin:xmax]
                        cropface=cv2.resize(cropfame,(182,182))
                        cv2.imwrite(imgpath,cropface)                        

                        cv2.rectangle(cropface, (x, y), (x2, y2), (0, 0, 255), 4)
                        cv2.putText(cropface,str(count),(50,50),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(255,255,0),3)
                        ConvertToQtFormat = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                        self.ImageUpdate.emit(ConvertToQtFormat)
                        # cv2.imshow("Getting Employee face",face)
                elif len(location)> 1:
                    # QMessageBox.about(self,"Alerat","Can't Detecte Face or there are more than 2 faces ")
                    self.FirstUi.Error.setText("There Are More Than One Face")
                if cv2.waitKey(1)==13 or count==30:
                    QMessageBox.about(self,"INFO","Employee with ID : "+str(self.capture_Emp_ID)+"Dataset has Been Taken")
                    self.FirstUi.Error.setText("Procces Done")
                    # self.FirstUi.stackedWidget.setCurrentWidget(self.FirstUi.BasicInfoPage)
                    self.FirstUi.save_btn.setVisible(True)
                    self.FirstUi.Start_btn.setVisible(False)
                    self.FirstUi.New_btn.setVisible(True)
                    break
            Camera.release()

########################################################################################   
########################################################################################
class EditEmployee(QDialog): # ----need to add function delete
    def __init__(self):
        QWidget.__init__(self)
        self.ui=Ui_newemp1()
        self.ui.setupUi(self)

        self.ui.search_btn.clicked.connect(self.SearchEmpWithID)

        self.ui.Back2basic.clicked.connect(self.backToBasic)

        self.ui.back_btn_3.clicked.connect(self.gotoempmenu)


        self.ui.Next_btn.clicked.connect(self.next2Empinfo)
        self.emailregx=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        self.ui.stackedWidget.setCurrentWidget(self.ui.BasicInfoPage)

       
        self.getCompayinfo()
        widget.setFixedWidth(960)
        widget.setFixedHeight(830)

    
    def next2Empinfo(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.EmployeeDataPage)
        self.ui.Next2Cap.setVisible(False)
        self.ui.update_btn.setVisible(True)

    def backToBasic(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.BasicInfoPage)

    def getCompayinfo(self):

        conn = sqlite3.connect("./DataBaseTable.db")
        conn.text_factory=str
        cursor = conn.cursor()
            
        cursor.execute('SELECT Dept_Name FROM DepartmentsTable;')
        dept_names=cursor.fetchall()
        dept_names1=[r[0] for r in dept_names]

        cursor.execute('SELECT JobDesc FROM JobTittle;')
        JobTitles=cursor.fetchall()
        JobTitles1=[r[0] for r in JobTitles]

        cursor.execute('SELECT AttendanceDesc FROM Attendance_Schemes_Table;')
        attendanceSchem=cursor.fetchall()
        attendanceSchem1=[r[0] for r in attendanceSchem]

        cursor.execute('SELECT Category FROM AccessScheme;')
        accesSchem=cursor.fetchall()
        accesSchem1=[r[0] for r in accesSchem]


        deptlen=len(dept_names1)
        joblen=len(JobTitles1)
        attendanceSchLen=len(attendanceSchem1)
        accesSchemLen=len(accesSchem1)

        if dept_names1 == []:
            print("you cant add New Employee you must First ADD Company Dept's")
           
        else:
            count=0
            self.ui.dep_drop_3.addItem("")
            for i in range (deptlen):
                self.ui.dep_drop_3.addItem(dept_names1[count])
                count+=1


        if  JobTitles == []:
            print("you cant add New Employee you must First ADD Company Job Titles's")     
        else:
            count=0
            self.ui.job_drop_3.addItem("")
            for i in range (joblen):
                self.ui.job_drop_3.addItem(JobTitles1[count])
                count+=1      

        if attendanceSchem1 ==[]:
            print("you cant add New Employee you must First ADD Company attendance Schem")
                 
        else:
            count=0 
            self.ui.att_drop_3.addItem("")
            for i in range (attendanceSchLen):
                self.ui.att_drop_3.addItem(attendanceSchem1[count])
                count+=1    

        if accesSchem1 ==[]:
            print("you cant add New Employee you must First ADD Company Access Schem")  
                  
        else:
            count=0 
            self.ui.acc_drop_3.addItem("")
            for i in range (accesSchemLen):
                self.ui.acc_drop_3.addItem(accesSchem1[count])
                count+=1  
   
    def handel_Lines(self):
        self.ui.first_line_3.clear()
        self.ui.middle_line_3.clear()
        self.ui.last_line_3.clear()
        self.ui.address_line_3.clear()
        self.ui.phone_line_3.clear()
        self.ui.email_line_3.clear()

    def getEmpPhoto(self,ID):
        conn = sqlite3.connect("./DataBaseTable.db")
        conn.text_factory=str
        cursor = conn.cursor()
        cursor.execute('SELECT Emp_Photo FROM Employees WHERE Emp_ID = ?;',[ID])
        blob=cursor.fetchone()
        pix=QPixmap()
        if pix.loadFromData(blob[0]):
            self.ui.photoview_3.setPixmap(pix)
            self.ui.photoview_3.setScaledContents(True)


    def SearchEmpWithID(self):
        
        self.empid=self.ui.searchbar.text()
       
        if (len(self.empid)==0):
            QMessageBox.about(self,"Error","Please Enter Employee id")
            
        else:
            conn = sqlite3.connect("./DataBaseTable.db")
            conn.text_factory=str
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Employees WHERE Emp_ID = ?;',[self.empid])
            result=cursor.fetchall()
            if result !=[]:
                for row in result:
                    firstname=row[1]
                    middelname=row[2]
                    lastname=row[3]
                    gender=row[4]
                    dateOFbrith=row[5]
                    address=row[6]
                    email=row[7]
                    empDeptID=row[8]
                    empJobID=row[9]
                    empAttendaceID=row[13]
                    empAccessID=row[14]
                    empPhone=row[15]
                    self.getEmpPhoto(self.empid) 


                dep_query = 'SELECT Dept_Name FROM DepartmentsTable WHERE Dept_ID =\''+str(empDeptID)+"\'"
                cursor.execute(dep_query)
                dep_query_result  = cursor.fetchone()
                for r in dep_query_result:
                    dep_query_result_str=r

                Job_query = 'SELECT JobDesc FROM JobTittle WHERE Emp_Job_ID=\''+str(empJobID)+"\'"
                cursor.execute(Job_query)
                Job_query_result  = cursor.fetchone()
                for r in Job_query_result:
                    Job_query_result_str=r

                attendSch_query = 'SELECT AttendanceDesc FROM Attendance_Schemes_Table WHERE AttendanceSchemes_ID =\''+str(empAttendaceID)+"\'"
                cursor.execute(attendSch_query)
                attendSch_query_result  = cursor.fetchone()
                
                for r in attendSch_query_result:
                    attendSch_query_result_str=r

                AccessCat_query = 'SELECT Category FROM AccessScheme WHERE AccessSchemID  =\''+str(empAccessID)+"\'"
                cursor.execute(AccessCat_query)
                AccessCat_query_result  = cursor.fetchone()
                
                for r in AccessCat_query_result:
                    AccessCat_query_result_str=r



                self.ui.first_line_3.setText(firstname)
                self.ui.middle_line_3.setText(middelname)
                self.ui.last_line_3.setText(lastname)
                self.ui.address_line_3.setText(address)
                self.ui.email_line_3.setText(email)
                self.ui.phone_line_3.setText(str(empPhone))
                
                self.ui.dep_drop_3.setCurrentText(dep_query_result_str)
                self.ui.job_drop_3.setCurrentText(Job_query_result_str)
                self.ui.att_drop_3.setCurrentText(attendSch_query_result_str)
                self.ui.acc_drop_3.setCurrentText(AccessCat_query_result_str)

                if gender=='M':
                    self.ui.MaleRadio_3.setChecked(True)
                else:
                    self.ui.FemaleRadio_3.setChecked(True)
                
                # dateOFbrith=date.fromisocalendar(dateOFbrith)
                dob=datetime.strptime(dateOFbrith,"%Y-%m-%d").date()
                self.ui.date_3.setDate(dob)
            
                self.ui.update_btn.clicked.connect(self.updateEmployeeData)

                conn.commit()
                conn.close()
            else:
                QMessageBox.about(self,"ERROR","There is No Employee With This ID")

            
    
    def gotoempmenu(self):
        EmpScreen = EmployeeMenu()
        widget.addWidget(EmpScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setWindowTitle(" Employee Menu")  


    def deleteEmployee(self): #-------------Task do Delete 
        pass

    def updateEmployeeData(self):

        self.first=self.ui.first_line_3.text()
        self.middleLine=self.ui.middle_line_3.text()
        self.last=self.ui.last_line_3.text()
        self.Malegender=self.ui.MaleRadio_3.isChecked()
        self.Femalegender=self.ui.FemaleRadio_3.isChecked()
        self.address=self.ui.address_line_3.text()
        self.email=self.ui.email_line_3.text()
        self.search= self.ui.searchbar.text()
        self.search=int(self.search)

        self.dep=self.ui.dep_drop_3.currentText()
        self.jobTitle=self.ui.job_drop_3.currentText()
        self.attendSch=self.ui.att_drop_3.currentText()
        self.accessCat=self.ui.acc_drop_3.currentText()



        if self.Malegender==True:
            self.Putgender="M"
        else:
            self.Putgender="F"
      
        if (self.search)==0:
            QMessageBox.about(self,"Error","Please Enter Employee id")
            print("error")
        elif len(self.middleLine)==0 or len(self.first)==0 or len(self.last)==0 or len(self.address)==0 or len(self.email)==0:
            QMessageBox.about(self,"Error","Please Enter Employee data")
        elif not (re.fullmatch(self.emailregx,self.email)):
            QMessageBox.warning(self,"Email Verfication","Email Format is incorrect.",QMessageBox.Ok)
        elif self.Malegender==False and self.Femalegender==False:
            QMessageBox.about(self,"Missing Data","Please Enter Employee Gender")      
        else:
            conn = sqlite3.connect("./DataBaseTable.db")
            conn.text_factory=str
            cursor = conn.cursor()
            dep_query = 'SELECT Dept_ID FROM DepartmentsTable WHERE Dept_Name =\''+self.dep+"\'"
            cursor.execute(dep_query)
            dep_query_result  = cursor.fetchone()
            

            Job_query = 'SELECT Emp_Job_ID FROM JobTittle WHERE JobDesc =\''+self.jobTitle+"\'"
            cursor.execute(Job_query)
            Job_query_result  = cursor.fetchone()
            

            attendSch_query = 'SELECT AttendanceSchemes_ID FROM Attendance_Schemes_Table WHERE AttendanceDesc =\''+self.attendSch+"\'"
            cursor.execute(attendSch_query)
            attendSch_query_result  = cursor.fetchone()
        

            AccessCat_query = 'SELECT AccessSchemID FROM AccessScheme WHERE Category =\''+self.accessCat+"\'"
            cursor.execute(AccessCat_query)
            AccessCat_query_result  = cursor.fetchone()

            GateID_query = 'SELECT GateID FROM AccessScheme WHERE Category =\''+self.accessCat+"\'"
            cursor.execute(GateID_query)
            GateID_query_result  = cursor.fetchone()
        
            if (dep_query_result or Job_query_result or attendSch_query_result or AccessCat_query_result) ==[] :
                QMessageBox.about(self, "alert", "please Fill All the Missing Parts ")
            
            

            elif dep_query_result or Job_query_result or attendSch_query_result or AccessCat_query_result is not None:
                cursor.execute('UPDATE Employees SET Emp_First_Name=?,Emp_Middle_Name=?,Emp_Last_Name=? ,Emp_Address=?,Emp_email=?,Emp_Dpet_ID=?,Emp_Job_ID=?,Emp_Attendace_SchemeID=?,Emp_Access_ID=?,Emp_Gender=? WHERE Emp_ID = ?',(self.first,self.middleLine,self.last,self.address,self.email,dep_query_result[0],Job_query_result[0],attendSch_query_result[0],AccessCat_query_result[0],self.Putgender,self.search))
                Arr=[GateID_query_result[0],AccessCat_query_result[0],self.accessCat,self.search]
                cursor.execute("UPDATE EmployeeAccess SET Gate_ID=?,AcessSchemeID=?,Cat=?  WHERE Emp_ID=?;",Arr)
                QMessageBox.about(self,"Employee Saved","Employee of ID "+ str(self.search) + " Is Updated")
                self.handel_Lines()
        
        
            conn.commit()
            conn.close()

#################################################################################################

class AddNewUser(QDialog):
    def __init__(self):
        super(AddNewUser, self).__init__()
        loadUi("./GUI/newuser.ui",self)
        self.pass_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.CancelButton.clicked.connect(self.goBack)
        self.save_btn.clicked.connect(self.save)
        
        
    def save(self):
        EmpId=self.id.text()
        user = self.user_line.text()
        password = self.pass_line.text()
        confirmpassword = self.confirmpass_line.text()

         
        if len(user)==0 or len(password)==0 or len(confirmpassword)==0:
            # self.error.setText("Please fill in all inputs.")
            print("error")

        elif password!=confirmpassword:
            print("Passwords do not match.")

        else:
            conn = sqlite3.connect("./DataBaseTable.db")
            cur = conn.cursor()

            for EmpId in (EmpId):
                cur.execute("SELECT rowid FROM Employees WHERE Emp_ID = ?", (EmpId, ))
            data = cur.fetchall()
            if len(EmpId) ==0:
                print('There is No Employee With This ID %s' % EmpId)
                QMessageBox.about(self, "alert", 'There is No Employee With This ID %s' % EmpId)
            else :
               # print('Employee Found Adding his admin account  %s' % (EmpId, ','.join(map(str, next(zip( * data))))))

                user_info = [user,password,EmpId]
                cur.execute('INSERT INTO Users (User_Name, User_Password,Emp_ID) VALUES (?,?,?)', user_info)

                conn.commit()
                conn.close()
                QMessageBox.about(self, "alert", 'Employee With This ID  %s ->> Admin account Added' % EmpId)

    def goBack(self):
        back2wle = MainWin()
        widget.addWidget(back2wle)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setWindowTitle("Main Screen")

#############################################################################################################
class CompanyInfo(QWidget):
    def __init__(self):

        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.onlyInt = QIntValidator()
        self.ui.depid_line.setValidator(QIntValidator())
        self.ui.jobid_line.setValidator(QIntValidator())
        self.ui.attid_line.setValidator(QIntValidator())
        self.ui.arrive_line.setValidator(QIntValidator())
        self.ui.leave_line.setValidator(QIntValidator())
        self.ui.gateid_line.setValidator(QIntValidator())
        self.ui.accessschemeid_line.setValidator(QIntValidator())
        self.ui.gateid_line_3.setValidator(QIntValidator())

        self.ui.insert_dep.clicked.connect(self.DepDB)
        self.ui.insert_job.clicked.connect(self.JobDes)
        self.ui.insert_att.clicked.connect(self.attschme)
        self.ui.insert_gate.clicked.connect(self.gatess)
        self.ui.insert_access.clicked.connect(self.acesss)

        widget.setFixedHeight(554)
        widget.setFixedWidth(904)
        self.RemoveSave()

        self.RemoveSearch()

        self.ui.back_btn.clicked.connect(self.goBack)
    # 
        # self.ui.toggle_btn.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        ## PAGES
        ########################################################################
        self.ui.pages.setCurrentWidget(self.ui.page0)
        # PAGE 1
        self.ui.dep_btn.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.page0))


        # PAGE 2
        self.ui.jd_btn.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.page1))

        # PAGE 3
        self.ui.att_btn.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.page2))
        # page 4
        self.ui.gate_btn.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.page3)) 

        #page 5
        self.ui.access_btn_2.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.page4)) 
       
        ## SHOW ==> MAIN WINDOW
        ########################################################################
    
    def RemoveSearch(self):
        self.ui.lineEdit_2.setVisible(False)
        self.ui.lineEdit_3.setVisible(False)
        self.ui.lineEdit_4.setVisible(False)
        self.ui.lineEdit_5.setVisible(False)
        self.ui.searchid_1.setVisible(False)
        self.ui.search_dep.setVisible(False)
        self.ui.search_job.setVisible(False)
        self.ui.search_att.setVisible(False)
        self.ui.search_gates.setVisible(False)
        self.ui.search_access.setVisible(False)
        
    def RemoveSave(self):
        self.ui.save_dep.setVisible(False)
        self.ui.save_access.setVisible(False)
        self.ui.save_job.setVisible(False)
        self.ui.save_gate.setVisible(False)
        self.ui.save_att.setVisible(False)

    def goBack(self):
        back2wle = CompanyMeua()
        widget.addWidget(back2wle)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setWindowTitle("Main Screen")

    def DepDB(self):
        depline=self.ui.dep_line.text()
        depid=self.ui.depid_line.text()
        
        if len(depline)==0 or len(depid)==0:
            QMessageBox.about(self,'Error', 'Please fill the blanked fields ')
        elif len(depline)!=0 or len(depid)!=0:
            conn = sqlite3.connect("./DataBaseTable.db")
            cur = conn.cursor()
            cur.execute('INSERT OR IGNORE INTO DepartmentsTable (Dept_ID, Dept_Name) VALUES (?,?)', (depid,depline))
            QMessageBox.about(self,'Added', 'Dep Added '+depid)
            conn.commit()
            conn.close()
    def JobDes(self):
        jobidline=self.ui.jobid_line.text()
        jobdesc=self.ui.job_line.text()
      
            
        if len(jobidline)==0 or len(jobdesc)==0:
            QMessageBox.about(self,'Error', 'Please fill the blanked fields ')
        elif len(jobidline)!=0 and len(jobdesc)!=0:
            conn = sqlite3.connect("./DataBaseTable.db")
            cur = conn.cursor()
            cur.execute('INSERT OR IGNORE INTO JobTittle (Emp_Job_ID, JobDesc) VALUES (?,?)', (jobidline,jobdesc))
            QMessageBox.about(self,'Added', 'Job Added '+jobidline)
            conn.commit()
            conn.close()
    def attschme(self):
        attschmeline=self.ui.attid_line.text()
        attchme=self.ui.att_line.text()
        arrtime=self.ui.arrive_line.text()
        leavetime=self.ui.leave_line.text()
       

        if len(attschmeline)==0 or len(attchme)==0 or len(arrtime)==0 or len(leavetime)==0:
            QMessageBox.about(self,'Error', 'Please fill the blanked fields ')
        elif len(attschmeline)!=0 and len(attchme)!=0 and len(arrtime)!=0 and len(leavetime)!=0:

            conn = sqlite3.connect("./DataBaseTable.db")
            cur = conn.cursor()
            cur.execute('INSERT OR IGNORE INTO Attendance_Schemes_Table (AttendanceSchemes_ID, Entry_Time,Leave_Time,AttendanceDesc) VALUES (?,?,?,?)', (attschmeline,arrtime,leavetime,attchme))
            QMessageBox.about(self,'Added', 'Attendace Added '+attschmeline)
            conn.commit()
            conn.close()
    def gatess(self):
        gateid=self.ui.gateid_line.text()
        gatename=self.ui.gate_line.text()
        gatecamip=self.ui.camip_line.text()
        gatelockip=self.ui.gatelock_line.text()

        
            

        if len(gateid)==0 or len(gatename)==0 or len(gatecamip)==0 or len(gatelockip)==0:
            QMessageBox.about(self,'Error', 'Please fill the blanked fields ')
        elif len(gateid)!=0 and len(gatename)!=0 and len(gatecamip)!=0 and len(gatelockip)!=0:

            conn = sqlite3.connect("./DataBaseTable.db")
            cur = conn.cursor()
            cur.execute('INSERT OR IGNORE INTO GatesTable (Gate_ID,Gate_Name,Gate_Camera_IP,Gate_Door_Lock_IP) VALUES (?,?,?,?)', (gateid,gatename,gatecamip,gatelockip))
            QMessageBox.about(self,'Added', 'gate Added '+gateid)
            conn.commit()
            conn.close()

    def acesss(self):
        accessschemeid=self.ui.accessschemeid_line.text()
        gateid=self.ui.gateid_line_3.text()
        jobsallowed=self.ui.jobsallowed_line.text()
        category=self.ui.category_line.text()
        

        if len(accessschemeid)==0 or len(gateid)==0 or len(jobsallowed)==0 or len(category)==0:
            QMessageBox.about(self,'Error', 'Please fill the blanked fields ')
        elif len(accessschemeid)!=0 and len(gateid)!=0 and len(jobsallowed)!=0 and len(category)!=0:

            conn = sqlite3.connect("./DataBaseTable.db")
            cur = conn.cursor()
            cur.execute('INSERT OR IGNORE INTO AccessScheme (AccessSchemID,GateID,JobsAllowed,Category) VALUES (?,?,?,?)', (accessschemeid,gateid,jobsallowed,category))
            QMessageBox.about(self,'Added', 'Access Added '+accessschemeid)
            conn.commit()
            conn.close()

class editcompany(QWidget):
     def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.handelButton()


        self.onlyInt = QIntValidator()
        self.ui.depid_line.setValidator(QIntValidator())
        self.ui.jobid_line.setValidator(QIntValidator())
        self.ui.attid_line.setValidator(QIntValidator())
        self.ui.arrive_line.setValidator(QIntValidator())
        self.ui.leave_line.setValidator(QIntValidator())
        self.ui.gateid_line.setValidator(QIntValidator())
        self.ui.accessschemeid_line.setValidator(QIntValidator())
        self.ui.gateid_line_3.setValidator(QIntValidator())
        self.ReadOnly()
        self.RemoveInsert()
        
    
        

        self.ui.back_btn.clicked.connect(self.goback)

        # self.ui.toggle_btn.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))
        widget.setFixedHeight(554)
        widget.setFixedWidth(904)
        ## PAGES
        ########################################################################
        self.ui.pages.setCurrentWidget(self.ui.page0)
        # PAGE 1
        self.ui.dep_btn.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.page0))


        # PAGE 2
        self.ui.jd_btn.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.page1))

        # PAGE 3
        self.ui.att_btn.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.page2))
        # page 4
        self.ui.gate_btn.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.page3)) 

        #page 5
        self.ui.access_btn_2.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.page4))        
     def handelButton(self):
        self.ui.search_dep.clicked.connect(self.searchdepid)
        self.ui.save_dep.clicked.connect(self.editdepid)
        self.ui.search_job.clicked.connect(self.searchJob)
        self.ui.save_job.clicked.connect(self.editjob)
        self.ui.search_att.clicked.connect(self.searchattendancescheme)
        self.ui.save_att.clicked.connect(self.editattendancescheme)
        self.ui.search_gates.clicked.connect(self.searchGates)
        self.ui.save_gate.clicked.connect(self.editgates)
        self.ui.search_access.clicked.connect(self.searchAccess)
        self.ui.save_access.clicked.connect(self.editaccess)
     def goback(self):
        compInfo = CompanyMeua()
        widget.addWidget(compInfo)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setWindowTitle("CompanyInfo")

     def ReadOnly(self):
        self.ui.depid_line.setReadOnly(True)
        self.ui.jobid_line.setReadOnly(True)
        self.ui.attid_line.setReadOnly(True)
        self.ui.gateid_line.setReadOnly(True)
        self.ui.accessschemeid_line.setReadOnly(True)

     def RemoveInsert(self):
        self.ui.insert_access.setVisible(False)
        self.ui.insert_att.setVisible(False)
        self.ui.insert_dep.setVisible(False)
        self.ui.insert_gate.setVisible(False)
        self.ui.insert_job.setVisible(False)
         
    
     def searchdepid(self):
        self.searchid=self.ui.lineEdit_2.text()

        if len(self.searchid)==0:
            QMessageBox.about(self,'Error','Please fill the search')
        
        conn = sqlite3.connect("./DataBaseTable.db")
        conn.text_factory=str
        cursor = conn.cursor()
        # cursor.execute('SELECT rowid FROM DepartmentsTable WHERE Dept_ID = ?)', (searchid, ))
        cursor.execute('SELECT * FROM DepartmentsTable WHERE Dept_ID = ?;',[self.searchid])
        record=cursor.fetchall()
        
        recordItem1=[r[0] for r in record]
        
        listTostring1= ' '.join([str(r[0]) for r in record])
        listTostring2= ' '.join([str(r[1]) for r in record])
        # print(recordItem1)
        

        self.ui.depid_line.setText((listTostring1))
        self.ui.dep_line.setText((listTostring2))
        


        conn.commit()
        conn.close()
        if len(recordItem1)==0:
            QMessageBox.about(self,'Error','Result not found')

     def editdepid(self):
        depline=self.ui.dep_line.text()
        conn = sqlite3.connect("./DataBaseTable.db")
        conn.text_factory=str
        cursor = conn.cursor()
        cursor.execute('UPDATE OR IGNORE DepartmentsTable set Dept_Name = ? WHERE Dept_ID = ?',(depline,self.searchid))
        QMessageBox.about(self,'updated', 'Dep updated '+self.searchid)
        conn.commit()
        conn.close()

     def searchJob(self):
         self.searchjob=self.ui.lineEdit_3.text()
         if len(self.searchjob)==0:
             QMessageBox.about(self,'Error','Please fill the search')

         conn = sqlite3.connect("./DataBaseTable.db")
         conn.text_factory=str
         cursor = conn.cursor()
        # cursor.execute('SELECT rowid FROM DepartmentsTable WHERE Dept_ID = ?)', (searchid, ))
         cursor.execute('SELECT * FROM JobTittle WHERE Emp_Job_ID = ?',self.searchjob)
         record=cursor.fetchall()
         recordItem1=[r[0] for r in record]
         

         listTostring1= ' '.join([str(r[0]) for r in record])
         listTostring2= ' '.join([str(r[1]) for r in record])
         
         self.ui.jobid_line.setText(listTostring1)
         self.ui.job_line.setText(listTostring2)
         conn.commit()
         conn.close()
         if len(recordItem1)==0:
            QMessageBox.about(self,'Error','Result not found')
         
     def editjob(self):
        jobline=self.ui.job_line.text()
        conn = sqlite3.connect("./DataBaseTable.db")
        conn.text_factory=str
        cursor = conn.cursor()
        cursor.execute('UPDATE OR IGNORE JobTittle set JobDesc = ? WHERE Emp_Job_ID = ?',(jobline,self.searchjob))
        QMessageBox.about(self,'updated', 'Job updated '+self.searchjob)
        conn.commit()
        conn.close()
        
     def searchattendancescheme(self):
         self.searchatt=self.ui.lineEdit_4.text()
         if len(self.searchatt)==0:
             QMessageBox.about(self,'Error','Please fill the search')
         conn = sqlite3.connect("./DataBaseTable.db")
         conn.text_factory=str
         cursor = conn.cursor()
         cursor.execute('SELECT * FROM Attendance_Schemes_Table WHERE AttendanceSchemes_ID = ?',self.searchatt)
         record=cursor.fetchall()
         recordItem1=[r[0] for r in record]
        

         listTostring1= ' '.join([str(r[0]) for r in record])
         listTostring2= ' '.join([str(r[1]) for r in record])
         listTostring3= ' '.join([str(r[2]) for r in record])
         listTostring4= ' '.join([str(r[3]) for r in record])
         
         self.ui.attid_line.setText(listTostring1)
         self.ui.arrive_line.setText(listTostring2)
         self.ui.leave_line.setText(listTostring3)
         self.ui.att_line.setText(listTostring4)
         
         conn.commit()
         conn.close()
         if len(recordItem1)==0:
            QMessageBox.about(self,'Error','Result not found')

         
     def editattendancescheme(self):
         attendancescheme=self.ui.att_line.text()
         arrivingtime=self.ui.arrive_line.text()
         leavingtime=self.ui.leave_line.text()
         conn = sqlite3.connect("./DataBaseTable.db")
         conn.text_factory=str
         cursor = conn.cursor()
         cursor.execute('UPDATE OR IGNORE Attendance_Schemes_Table set Entry_Time = ? , Leave_Time = ? , AttendanceDesc = ? WHERE AttendanceSchemes_ID = ?',(arrivingtime,leavingtime,attendancescheme,self.searchatt))
         QMessageBox.about(self,'updated', 'Attendance updated '+self.searchatt)
         conn.commit()
         conn.close()
         
     def searchGates(self):
         self.searchgates=self.ui.lineEdit_5.text()
         if len(self.searchgates)==0:
             QMessageBox.about(self,'Error','Please fill the search')
         conn = sqlite3.connect("./DataBaseTable.db")
         conn.text_factory=str
         cursor = conn.cursor()
         cursor.execute('SELECT * FROM GatesTable WHERE Gate_ID = ?',self.searchgates)
         record=cursor.fetchall()
         recordItem1=[r[0] for r in record]
         

         listTostring1= ' '.join([str(r[0]) for r in record])
         listTostring2= ' '.join([str(r[1]) for r in record])
         listTostring3= ' '.join([str(r[2]) for r in record])
         listTostring4= ' '.join([str(r[3]) for r in record])
         
         self.ui.gateid_line.setText(listTostring1)
         self.ui.gate_line.setText(listTostring2)
         self.ui.camip_line.setText(listTostring3)
         self.ui.gatelock_line.setText(listTostring4)
         
         conn.commit()
         conn.close()
         if len(recordItem1)==0:
            QMessageBox.about(self,'Error','Result not found')
     
     def editgates(self):
         gatename=self.ui.gate_line.text()
         camip=self.ui.camip_line.text()
         gatelock=self.ui.gatelock_line.text()
         conn = sqlite3.connect("./DataBaseTable.db")
         conn.text_factory=str
         cursor = conn.cursor()
         cursor.execute('UPDATE OR IGNORE GatesTable set Gate_Name = ? , Gate_Camera_IP = ? , Gate_Door_Lock_IP = ? WHERE Gate_ID = ?',(gatename,camip,gatelock,self.searchgates))
         QMessageBox.about(self,'updated', 'gate updated '+self.searchgates)
         conn.commit()
         conn.close()
         
     def searchAccess(self):
         self.searchaccess=self.ui.searchid_1.text()
         if len(self.searchaccess)==0:
             QMessageBox.about(self,'Error','Please fill the search')
         conn = sqlite3.connect("./DataBaseTable.db")
         conn.text_factory=str
         cursor = conn.cursor()
         cursor.execute('SELECT * FROM AccessScheme WHERE AccessSchemID = ?',self.searchaccess)
         record=cursor.fetchall()
         recordItem1=[r[0] for r in record]
         

         listTostring1= ' '.join([str(r[0]) for r in record])
         listTostring2= ' '.join([str(r[1]) for r in record])
         listTostring3= ' '.join([str(r[2]) for r in record])
         listTostring4= ' '.join([str(r[3]) for r in record])
         
         self.ui.accessschemeid_line.setText(listTostring1)
         self.ui.gateid_line_3.setText(listTostring2)
         self.ui.jobsallowed_line.setText(listTostring3)
         self.ui.category_line.setText(listTostring4)
         
         conn.commit()
         conn.close()
         if len(recordItem1)==0:
            QMessageBox.about(self,'Error','Result not found')
     
     def editaccess(self):
         gateid=self.ui.gateid_line_3.text()
         jobsallowed=self.ui.jobsallowed_line.text()
         categoryy=self.ui.category_line.text()
         conn = sqlite3.connect("./DataBaseTable.db")
         conn.text_factory=str
         cursor = conn.cursor()
         cursor.execute('UPDATE OR IGNORE AccessScheme set GateID = ? , JobsAllowed = ? , Category = ? WHERE AccessSchemID = ?',(gateid,jobsallowed,categoryy,self.searchaccess))
         QMessageBox.about(self,'updated', 'Access updated '+self.searchaccess)
         conn.commit()
         conn.close()

class TrainScreen(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_ModelTraining()
        
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.StartTrain)
        self.ui.progressBar.setRange(0, 500)
        self.ui.progressBar.setValue(0)
        self.ui.back_btn.setVisible(False)
        self.ui.back_btn.clicked.connect(self.goback)

    def goback(self):
        compInfo = MainWin()
        widget.addWidget(compInfo)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        # widget.setWindowTitle("CompanyInfo")

    def LoadBar(self, flag):

        if(flag == True):
            for i in range(500):
                time.sleep(0.01)
                self.ui.progressBar.setValue(i+1)
        else:
            # self.ui.progressBar.setValue(500)
            self.ui.back_btn.setVisible(True)
            QMessageBox.about(self,"INFO","Training Done")
            # self.ui.progressBar.setVisible(False)
    def StartTrain(self):

        self.datadir = './DataSet'
        self.modeldir = './model/trained_facenet_model.pb'
        self.classifier_filename = './class/test.pkl'

        obj=training(self.datadir,self.modeldir,self.classifier_filename)
        self.LoadBar(True)
        get_file=obj.main_train()
        # print('Saved classifier model to file "%s"' % get_file)
        
        self.LoadBar(False)    


class viewreportmenu(QWidget):
        def __init__(self):
            QWidget.__init__(self)
            self.ui = Ui_ViewRep()
            self.ui.setupUi(self)
            # self.ui.attendanceviewreport_btn.clicked.connect(self.gotoattendance)
            # self.ui.accessviewreport_btn.clicked.connect(self.gotoaccess)
            self.ui.backreport_btn.clicked.connect(self.goback)
            # self.ui.customreport_btn.clicked.connect(self.gotochoice)
            self.ui.attendanceviewreport_btn.clicked.connect(self.searchatt) 
            self.ui.accessviewreport_btn.clicked.connect(self.searchacc)

        

        
        def gotoattendance(self):
            Newviewatt= viewattendance()
            widget.addWidget(Newviewatt)
            widget.setCurrentIndex(widget.currentIndex()+1)
            widget.setWindowTitle("View Attendance Report")

        # def gotochoice(self):
        #     # self.ui.customreport_btn.setVisible(False)
        #     self.ui.attendanceviewreport_btn.clicked.connect(self.searchatt) 
        #     self.ui.accessviewreport_btn.clicked.connect(self.searchacc)



        def gotoaccess(self):
            Newviewacc= viewaccess()
            widget.addWidget(Newviewacc)
            widget.setCurrentIndex(widget.currentIndex()+1)
            widget.setWindowTitle("View Access Report")

        def goback(self):
            Newmenu = EmployeeMenu()
            widget.addWidget(Newmenu)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            widget.setWindowTitle(" View Report Menu")  
        def searchatt(self):
            Newatt = searchattreport()
            widget.addWidget(Newatt)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        def searchacc(self):
            Newacc = searchaccreport()
            widget.addWidget(Newacc)
            widget.setCurrentIndex(widget.currentIndex() + 1)

class viewattendance(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_AttendanceView()
        self.ui.setupUi(self)
        self.ui.loadData()
        self.ui.backattrep_btn.clicked.connect(self.goback)
        self.ui.lineEdit_attrep.setVisible(False)
        self.ui.searchattrep.setVisible(False)
        self.ui.label_2.setVisible(False)
    def goback(self):
        Newviewreport = viewreportmenu()
        widget.addWidget(Newviewreport)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setWindowTitle(" View Report Menu")  
    def saveexcelatt(self):
        conn = sqlite3.connect('./DataBaseTable.db', isolation_level=None,
                       detect_types=sqlite3.PARSE_COLNAMES)
        db_df = pd.read_sql_query("SELECT * FROM AttendanceSheet", conn)
        db_df.to_csv('database.csv', index=False)

        QMessageBox.about(self,'Notification', 'File saved to excel successfully ')
        
class viewaccess(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_AccessView()
        self.ui.setupUi(self)
        self.ui.loadData()
        self.ui.backaccrep_btn.clicked.connect(self.goback)
        self.ui.pushButton.clicked.connect(self.saveexcelacc)
        self.ui.lineEdit_accrep.setVisible(False)
        self.ui.searchaccrep.setVisible(False)
        self.ui.label_2.setVisible(False)

    def goback(self):
        Newviewreport = viewreportmenu()
        widget.addWidget(Newviewreport)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setWindowTitle(" View Report Menu")  

    def saveexcelacc(self):
        conn = sqlite3.connect('./DataBaseTable.db', isolation_level=None,
                       detect_types=sqlite3.PARSE_COLNAMES)
        db_df = pd.read_sql_query("SELECT * FROM EmployeeAccess", conn)
        db_df.to_csv('database.csv', index=False)

        QMessageBox.about(self,'Notification', 'File saved to excel successfully ')
        conn.close()
    
class searchattreport(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_AttendanceView()
        self.ui.setupUi(self)
        self.ui.searchattrep.clicked.connect(self.search)
        self.ui.backattrep_btn.clicked.connect(self.goback)
        self.ui.pushButton.setVisible(False)
    def search(self):
        conn = sqlite3.connect("./DataBaseTable.db")
        conn.text_factory=str
        cursor = conn.cursor()
        self.search=self.ui.lineEdit_attrep.text()
        cursor.execute('SELECT * FROM AttendanceSheet WHERE Emp_ID=?', (self.search,))
        result=cursor.fetchall()
        self.ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, colum_number, QTableWidgetItem(str(data)))
    def goback(self):
        Newviewreport = viewreportmenu()
        widget.addWidget(Newviewreport)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        
class searchaccreport(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_AccessView()
        self.ui.setupUi(self)
        self.ui.searchaccrep.clicked.connect(self.search)
        self.ui.backaccrep_btn.clicked.connect(self.goback)
        # self.ui.pushButton.setVisible(False)
    def search(self):
        conn = sqlite3.connect("./DataBaseTable.db")
        conn.text_factory=str
        cursor = conn.cursor()
        self.search=self.ui.lineEdit_accrep.text()
        cursor.execute('SELECT * FROM EmployeeAccess WHERE Emp_ID=?', (self.search,))
        result=cursor.fetchall()
        self.ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, colum_number, QTableWidgetItem(str(data)))
    def goback(self):
        Newviewreport = viewreportmenu()
        widget.addWidget(Newviewreport)
        widget.setCurrentIndex(widget.currentIndex() + 1)


        

        
        
    
        


        





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WelcomeScreen()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(window)
    widget.show()
    sys.exit(app.exec_())
        





    