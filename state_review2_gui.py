# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'review.ui'
#
# Created: Sun Mar 22 01:31:53 2015
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

class state_review_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
    
    def setupUi(self, Form):
        self.i=0

        self.st_p_name=[]
        self.st_title=[]
        self.st_review=[]
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(716, 529)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 100, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(190, 100, 301, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit_2 = QtGui.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(190, 140, 301, 31))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.textEdit_3 = QtGui.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(193, 190, 301, 281))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(165, 10, 351, 51))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(60, 280, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 280, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Reviewer", None))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Reviews of the State of your choice</span></p></body></html>", None))
        self.pushButton.setText(_translate("Form", "Previous", None))
        self.pushButton_2.setText(_translate("Form", "Next", None))
        self.pushButton.clicked.connect(self.showprevious)
        self.pushButton_2.clicked.connect(self.shownext)



    def getpara(self, result):
        self.st_p_name=result[0]
        self.st_title=result[1]
        self.st_review=result[2]
        
        #(self.st_p_name,self.st_title,self.st_review)=st_p_name,st_title,st_review
        print self.st_p_name
        self.show_rev()
    def show_rev(self):
        self.textEdit.setText(self.st_p_name[0])
        self.textEdit_2.setText(self.st_title[0])
        self.textEdit_3.setText(self.st_review[0])
    def shownext(self):
        self.i+=1
        try:
            self.textEdit.setText(self.st_p_name[self.i])
            self.textEdit_2.setText(self.st_title[self.i])
            self.textEdit_3.setText(self.st_review[self.i])
        except:
            self.i-=1
    def showprevious(self):
        self.i-=1
        try:
            self.textEdit.setText(self.st_p_name[self.i])
            self.textEdit_2.setText(self.st_title[self.i])
            self.textEdit_3.setText(self.st_review[self.i])
        except:
            self.i+=1


##
##if __name__ == "__main__":
##    import sys
##    app = QtGui.QApplication(sys.argv)
##    Form = QtGui.QWidget()
##    ui = Ui_Form()
##    ui.setupUi(Form)
##    Form.show()
##    sys.exit(app.exec_())

