# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cover.ui'
#
# Created: Sat Mar 21 17:00:27 2015
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
from hotels_and_sight_seeing import *
from city_list_gui3 import *
from state_review2_gui import *
from flight_in_gui2 import *
from sslist_gui import *
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class cover_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
    
    def setupUi(self, Form):
        self.state=''
        self.city=''
        self.st_p_name=[]
        self.st_title=[]
        self.st_review=[]
        self.ssid=0
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(647, 550)
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 70, 311, 131))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.formLayout = QtGui.QFormLayout(self.frame)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.pushButton)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtGui.QFormLayout.FieldRole, spacerItem)
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 80, 131, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_6 = QtGui.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(350, 150, 131, 23))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(350, 180, 131, 23))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.frame_2 = QtGui.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(30, 310, 276, 121))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textBrowser = QtGui.QTextBrowser(self.frame_2)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout.addWidget(self.textBrowser)
        self.pushButton_9 = QtGui.QPushButton(self.frame_2)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.verticalLayout.addWidget(self.pushButton_9)
        self.pushButton_8 = QtGui.QPushButton(self.frame_2)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.verticalLayout.addWidget(self.pushButton_8)
        self.frame_3 = QtGui.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(19, 230, 311, 41))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_5 = QtGui.QPushButton(self.frame_3)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_3 = QtGui.QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(self.frame_3)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout.addWidget(self.pushButton_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "State", None))
        self.pushButton.setText(_translate("Form", "City", None))
        self.pushButton_2.setText(_translate("Form", "See State Reviews", None))
        self.pushButton_6.setText(_translate("Form", "See Hotels", None))
        self.pushButton_7.setText(_translate("Form", "See Places To Visit", None))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Our Recommendations</span></p></body></html>", None))
        self.pushButton_9.setText(_translate("Form", "Optimal Day Plans for the City.", None))
        self.pushButton_8.setText(_translate("Form", "Optimal Time to Visit the City.", None))
        self.pushButton_5.setText(_translate("Form", "See Trains", None))
        self.pushButton_3.setText(_translate("Form", "See Weather", None))
        self.pushButton_4.setText(_translate("Form", "See Flights", None))
        self.pushButton.clicked.connect(self.loadCity)
        self.pushButton_2.clicked.connect(self.loadStateReviews)
        self.pushButton_4.clicked.connect(self.loadFlights)
        self.pushButton_7.clicked.connect(self.sightseeing)
    def sightseeing(self):
        self.state=str(self.lineEdit.text())
        lst=get_sightseeing_list(self.state, self.city)
        global ss_window
        ss_window=sslist_Form()
        ss_window.receivepara(lst)
        ss_window.show()
        self.ssid=ss_window.ssid
        
    def loadCity(self):
        self.state=str(self.lineEdit.text())
        city_dic=get_city_list_with_details(self.state)
        global cityWindow
        cityWindow=city_Form()
        cityWindow.getdic(city_dic)
        cityWindow.show()
        
        self.city=cityWindow.city
        
        #print "I am in cover"
        #print cityWindow.city
        
    def loadStateReviews(self):
        self.state=str(self.lineEdit.text())
        print self.state
        result=get_state_reviews(self.state)
        print result[0]
        global state_review_window
        state_review_window=state_review_Form()
        state_review_window.getpara(result)
        state_review_window.show()
        
    
        
    def loadFlights(self):
        global flight_window
        flight_window=Flight_Form()
        flight_window.show()
        


if __name__ == "__main__":
    app=QtGui.QApplication(sys.argv)
    ex=cover_Form()
    ex.show()
    sys.exit(app.exec_())

