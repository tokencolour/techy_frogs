# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'flights_op.ui'
#
# Created: Sat Mar 21 08:20:18 2015
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
from flight_func import *
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

class Op_form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        #self.showInvolvedFlights(self)
    def setupUi(self, Form):
        self.orig=''
        self.dest=''
        self.date=''
        self.sol=''
        self.ad=0
        self.cd=0
        self.sd=0
        self.infl=0
        self.infs=0
        self.prc=0
        self.maxpr='0'
        self.response=[]
        self.i=1

        
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(757, 548)
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(40, 60, 681, 461))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.textEdit = QtGui.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(140, 20, 421, 381))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(30, 170, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 180, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        #self.showInvolvedFlights(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Previous", None))
        self.pushButton_2.setText(_translate("Form", "Next", None))

        self.pushButton.clicked.connect(self.showprevious)
        
        
        self.pushButton_2.clicked.connect(self.shownext)
    def receivepara(self, orig, dest, date, sol, ad, cd, sd, infl, infs, prc, maxpr):
        self.orig=orig
        self.dest=dest
        self.date=date
        self.sol=sol
        self.ad=ad
        self.cd=cd
        self.sd=sd
        self.infl=infl
        self.infs=infs
        self.prc=prc
        self.maxpr=maxpr
        print"Iam the control and I am in output sscript"
        print "I have received this"
        print self.date
        print self.orig
        print self.dest
        print self.ad
        print self.sd
        print self.infl
        print self.infs
        print self.maxpr
        print type(self.date)
        print type(self.orig)
        print type(self.dest)
        print type(self.sol)
        print type(self.ad)
        print type(self.cd)
        print type(self.sd)
        print type(self.infl)
        print type(self.infs)
        print type(self.prc)
        print type(self.maxpr)
        self.showInvolvedFlights()

    def showInvolvedFlights(self):
        self.response=findflight(self.orig, self.dest, self.date, self.sol, self.ad, self.cd, self.sd, self.infl, self.infs,self.prc, self.maxpr)
        self.textEdit.setText(self.response[0])
    def shownext(self):
        if self.i< (int(self.sol)):
            
            self.textEdit.setText(self.response[self.i])
            self.i+=1
        
        
    def showprevious(self):
        if (self.i>0):
            
            self.textEdit.setText(self.response[self.i])
            self.i-=1
        
    
##
##if __name__ == "__main__":
##    import sys
##    app = QtGui.QApplication(sys.argv)
##    Form = QtGui.QWidget()
##    ui = Ui_Form()
##    ui.setupUi(Form)
##    Form.show()
##    sys.exit(app.exec_())

