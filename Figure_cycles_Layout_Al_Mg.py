# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Figure_cycles_Layout_Al_Mg.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1080, 725)
        self.Frame_FigCycles = QtWidgets.QWidget(Form)
        self.Frame_FigCycles.setGeometry(QtCore.QRect(9, 9, 1061, 671))
        self.Frame_FigCycles.setObjectName("Frame_FigCycles")
        self.pushButton_saveFigure = QtWidgets.QPushButton(Form)
        self.pushButton_saveFigure.setGeometry(QtCore.QRect(930, 690, 140, 32))
        self.pushButton_saveFigure.setObjectName("pushButton_saveFigure")
        self.comboBox_selection = QtWidgets.QComboBox(Form)
        self.comboBox_selection.setGeometry(QtCore.QRect(20, 690, 141, 32))
        self.comboBox_selection.setObjectName("comboBox_selection")
        self.comboBox_selection.addItem("")
        self.comboBox_selection.addItem("")
        self.comboBox_selection.addItem("")
        self.comboBox_selection.addItem("")
        self.comboBox_selection.addItem("")
        self.comboBox_selection.addItem("")
        self.pushButton_changedeadtime = QtWidgets.QPushButton(Form)
        self.pushButton_changedeadtime.setGeometry(QtCore.QRect(170, 690, 161, 32))
        self.pushButton_changedeadtime.setObjectName("pushButton_changedeadtime")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_saveFigure.setText(_translate("Form", "Save figure"))
        self.comboBox_selection.setItemText(0, _translate("Form", "27Al / 24Mg"))
        self.comboBox_selection.setItemText(1, _translate("Form", "D26Mg"))
        self.comboBox_selection.setItemText(2, _translate("Form", "24Mg (cps)"))
        self.comboBox_selection.setItemText(3, _translate("Form", "25Mg (cps)"))
        self.comboBox_selection.setItemText(4, _translate("Form", "26Mg (cps)"))
        self.comboBox_selection.setItemText(5, _translate("Form", "27Al (cps)"))
        self.pushButton_changedeadtime.setText(_translate("Form", "Change deadtime"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

