# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sslist.ui'
#
# Created: Sun Mar 22 08:51:42 2015
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

class sslist_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
    
    def setupUi(self, Form):
        self.lst=[]
        self.ssid=0
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(652, 519)
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(170, 80, 331, 321))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(170, 430, 331, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(170, 470, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(5, 10, 641, 51))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Submit", None))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">PLACES TO VISIT</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Fill in the index against the place of your choice to get its reviews</span></p></body></html>", None))
        self.pushButton.clicked.connect(self.takeEntry)
    def receivepara(self, lst):
        self.lst=lst
        self.showlist()
    def showlist(self):
        print self.lst
        if lst=="Data not available for this choice":
            self.textEdit.setText("Data not available for this choice")
        else:   
            stri=''
            for el in self.lst:
                stri=stri+str(self.lst.index(el)+1)+")"+el+"\n"
    
            self.textEdit.setText(stri)
    def takeEntry(self):
        self.ssid=int(self.lineEdit.text())
        
        

##if __name__ == "__main__":
##    import sys
##    app = QtGui.QApplication(sys.argv)
####    Form = QtGui.QWidget()
##    ui = Ui_Form()
##    ui.setupUi(Form)
##    Form.show()
##    sys.exit(app.exec_())
##
