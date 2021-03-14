# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Figure_Add_Info_Layout.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1080, 964)
        self.Frame_FigAddInfo = QtWidgets.QWidget(Form)
        self.Frame_FigAddInfo.setGeometry(QtCore.QRect(9, 9, 1061, 911))
        self.Frame_FigAddInfo.setObjectName("Frame_FigAddInfo")
        self.pushButton_saveFigure = QtWidgets.QPushButton(Form)
        self.pushButton_saveFigure.setGeometry(QtCore.QRect(930, 928, 140, 32))
        self.pushButton_saveFigure.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_saveFigure.setText(_translate("Form", "Save Figure"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

