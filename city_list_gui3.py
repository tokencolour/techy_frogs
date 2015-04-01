# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'city_list.ui'
#
# Created: Sat Mar 21 23:26:55 2015
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
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

class city_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
 
    def setupUi(self, Form):
        self.city_lst=[]
        self.i=0
        self.city=''
        ##self.flag=0# to check whether a city is yet selected or not
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(635, 541)
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(130, 150, 391, 361))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 160, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(120, 160, 231, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(120, 210, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textEdit = QtGui.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(13, 30, 371, 111))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(150, 10, 331, 61))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
##        self.pushButton_2 = QtGui.QPushButton(Form)
##        self.pushButton_2.setGeometry(QtCore.QRect(30, 210, 75, 23))
##        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
##        self.pushButton_3 = QtGui.QPushButton(Form)
##        self.pushButton_3.setGeometry(QtCore.QRect(530, 210, 75, 23))
##        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
####
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "List of Cities", None))
        self.label.setText(_translate("Form", "ENTER HERE", None))
        self.pushButton.setText(_translate("Form", "Submit", None))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">LIST OF CITIES</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">ENTER THE INDEX AGAINST THE CITY OF YOUR CHOICE IN THE BAR BELOW</span></p></body></html>", None))
##        self.pushButton_2.setText(_translate("Form", "Previous", None))
##        self.pushButton_3.setText(_translate("Form", "Next", None))
##
##        self.pushButton_2.clicked.connect(self.showprevious)
##        self.pushButton_3.clicked.connect(self.shownext)
        self.pushButton.clicked.connect(self.takecity)
    def getdic(self, dic):
        self.city_lst=dic.keys()
        stri=''
        for city in self.city_lst:
            stri=stri+str(self.city_lst.index(city)+1)+")"+city+"\n"
        self.textEdit.setText(stri)
        
##        self.textEdit.setText(str(self.i+1)+")"+self.city_lst[0])
##    def shownext(self):
##
##        self.i+=1
##        try:
##            
##            self.textEdit.setText(str(self.i+1)+")"+self.city_lst[self.i])
##            
##        except:
##            self.i-=1
##            
##    def showprevious(self):
##        self.i-=1
##        try:
##            
##            self.textEdit.setText(str(self.i+1)+")"+self.city_lst[self.i])
##            
##        except:
##            self.i+=1
##            

    def takecity(self):
        inp=int(self.lineEdit.text())
        self.city=self.city_lst[inp-1]
        print self.city

        


##if __name__ == "__main__":
##    import sys
##    app = QtGui.QApplication(sys.argv)
##    Form = QtGui.QWidget()
##    ui = Ui_Form()
##    ui.setupUi(Form)
##    Form.show()
##    sys.exit(app.exec_())

