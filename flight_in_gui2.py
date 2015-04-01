# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'flights_in2.ui'
#
# Created: Sat Mar 21 10:35:25 2015
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
from flight_op_gui import *
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

class Flight_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(767, 560)
        self.prc=0
        self.orig=''
        self.dest=''
        self.date=''
        self.sol=''
        self.ad=0
        self.cd=0
        self.sd=0
        self.infl=0
        self.infs=0
        self.maxpr='0'


        
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 10, 451, 361))
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
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtGui.QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.spinBox = QtGui.QSpinBox(self.frame)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.spinBox)
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.spinBox_2 = QtGui.QSpinBox(self.frame)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.spinBox_2)
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_6)
        self.spinBox_3 = QtGui.QSpinBox(self.frame)
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.spinBox_3)
        self.label_7 = QtGui.QLabel(self.frame)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_7)
        self.spinBox_4 = QtGui.QSpinBox(self.frame)
        self.spinBox_4.setObjectName(_fromUtf8("spinBox_4"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.spinBox_4)
        self.label_8 = QtGui.QLabel(self.frame)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtGui.QLabel(self.frame)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_9)
        self.spinBox_5 = QtGui.QSpinBox(self.frame)
        self.spinBox_5.setObjectName(_fromUtf8("spinBox_5"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.spinBox_5)
        self.spinBox_6 = QtGui.QSpinBox(self.frame)
        self.spinBox_6.setObjectName(_fromUtf8("spinBox_6"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.spinBox_6)
        self.label_10 = QtGui.QLabel(self.frame)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_4 = QtGui.QLineEdit(self.frame)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_11 = QtGui.QLabel(self.frame)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.LabelRole, self.label_11)
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.FieldRole, self.pushButton_2)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(530, 200, 141, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.menu=QtGui.QMenu()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Find_Flight", None))
        self.label.setText(_translate("Form", "Origin", None))
        self.label_2.setText(_translate("Form", "Destination", None))
        self.label_3.setText(_translate("Form", "Date", None))
        self.label_4.setText(_translate("Form", "No. of Air Solutions", None))
        self.label_5.setText(_translate("Form", "No. of Adults", None))
        self.label_6.setText(_translate("Form", "No. of Children", None))
        self.label_7.setText(_translate("Form", "No. of Senior Citizens", None))
        self.label_8.setText(_translate("Form", "No. of infants who don\'t require a seat", None))
        self.label_9.setText(_translate("Form", "No. of infants who require a seat", None))
        self.label_10.setText(_translate("Form", "Maximum Fare you can afford", None))
        self.label_11.setText(_translate("Form", "Preferred Coach", None))
        self.pushButton_2.setText(_translate("Form", "Select Coach", None))
        self.pushButton.setText(_translate("Form", "Find Flights", None))



        self.lineEdit_3.setText("yyyy-mm-dd")
        self.pushButton.clicked.connect(self.showoutput)
        self.pushButton.clicked.connect(self.make_op_window)
        self.menu.addAction('COACH', self.setprc1)
        self.menu.addAction('PREMIUM_COACH', self.setprc2)
        self.menu.addAction('BUSINESS', self.setprc3)
        self.menu.addAction('FIRST', self.setprc4)
        self.pushButton_2.setMenu(self.menu)
        

###############################################################
        
    def setprc1(self):
        self.prc=1
        print self.prc
        
    def setprc2(self):
        self.prc=2
        print self.prc

        
    def setprc3(self):
        self.prc=3
        print self.prc

        
    def setprc4(self):
        self.prc=4
        print self.prc
    
        
    def showoutput(self):
        self.orig=str(self.lineEdit.text())
        self.dest=str(self.lineEdit_2.text())
        
        self.orig=self.orig.upper()
        self.dest=self.dest.upper()
        self.date=str(self.lineEdit_3.text())
        self.sol=str(self.spinBox.value())
        self.ad=int(self.spinBox_2.value())
        self.cd=int(self.spinBox_3.value())
        self.sd=int(self.spinBox_4.value())
        self.infl=int(self.spinBox_5.value())
        self.infs=int(self.spinBox_6.value())
        self.maxpr=str(self.lineEdit_4.text())
        
        print self.date
        print self.orig
        print self.dest
        print self.ad
        print self.sd
        print self.infl
        print self.infs
        print self.maxpr
    def make_op_window(self):
        global output
        output=Op_form()
        output.receivepara(self.orig, self.dest, self.date, self.sol, self.ad, self.cd, self.sd, self.infl, self.infs,self.prc, self.maxpr)
        output.show()
        
##        output.receivepara(self.orig, self.dest, self.date, self.sol, self.ad, self.cd, self.sd, self.infl, self.infs,self.prc, self.maxpr)
        
        
        
        
    

##if __name__ == "__main__":
##    
##    app=QtGui.QApplication(sys.argv)
##    output = None
##    ex=Ui_Form()
##    ex.show()
##    
##    sys.exit(app.exec_())
