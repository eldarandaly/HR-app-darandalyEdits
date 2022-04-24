from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
 
#from ui_companyinfo import Ui_Form
import sys
from PyQt5 import QtWidgets
from PyQt5 import *
# IMPORT FUNCTIONS
#from ui_functions import *
from GUI.ui_welcome import Ui_WelcomeWindow 
#from GUI.ui_employee import Ui_employeeWindow
from GUI.ui_login import Ui_loginWindow
#from GUI.ui_MainMenue import Ui_MainWindow
#from GUI.ui_newemployee import Ui_newemp1
#from GUI.ui_newemployee2 import Ui_newemp2
#from GUI.ui_newuser import Ui_newuser

class WelcomeScreen(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_WelcomeWindow()
        self.ui.setupUi(self)
        self.ui.login_btn.clicked.connect(self.gotologin)
        self.show()
    def gotologin(self):
        gologin=login()
        widget.addWidget(gologin)
        widget.setCurrentWidget(gologin)
        

class login(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui=Ui_loginWindow()
        self.ui.setupUi(self)
        self.show()

if __name__== "__main__":
    app= QApplication(sys.argv)
    win=WelcomeScreen()
    widget=QtWidgets.QStackedWidget()
    widget.addWidget(win)
    widget.show() 
    sys.exit(app.exec_())