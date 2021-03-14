# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PopUp_Deadtime_Layout.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_New_Deadtime(object):
    def setupUi(self, Dialog_New_Deadtime):
        Dialog_New_Deadtime.setObjectName("Dialog_New_Deadtime")
        Dialog_New_Deadtime.resize(239, 119)
        self.buttonBox_Deadtime_value_Layout = QtWidgets.QDialogButtonBox(Dialog_New_Deadtime)
        self.buttonBox_Deadtime_value_Layout.setGeometry(QtCore.QRect(10, 80, 191, 32))
        self.buttonBox_Deadtime_value_Layout.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_Deadtime_value_Layout.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_Deadtime_value_Layout.setObjectName("buttonBox_Deadtime_value_Layout")
        self.label_Deadtime_value = QtWidgets.QLabel(Dialog_New_Deadtime)
        self.label_Deadtime_value.setGeometry(QtCore.QRect(30, 47, 134, 16))
        self.label_Deadtime_value.setObjectName("label_Deadtime_value")
        self.label_Deadtime_title = QtWidgets.QLabel(Dialog_New_Deadtime)
        self.label_Deadtime_title.setGeometry(QtCore.QRect(20, 17, 201, 16))
        self.label_Deadtime_title.setObjectName("label_Deadtime_title")
        self.lineEdit_New_Deadtime_value = QtWidgets.QLineEdit(Dialog_New_Deadtime)
        self.lineEdit_New_Deadtime_value.setGeometry(QtCore.QRect(180, 40, 40, 30))
        self.lineEdit_New_Deadtime_value.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_New_Deadtime_value.setObjectName("lineEdit_New_Deadtime_value")

        self.retranslateUi(Dialog_New_Deadtime)
        self.buttonBox_Deadtime_value_Layout.accepted.connect(Dialog_New_Deadtime.accept)
        self.buttonBox_Deadtime_value_Layout.rejected.connect(Dialog_New_Deadtime.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_New_Deadtime)

    def retranslateUi(self, Dialog_New_Deadtime):
        _translate = QtCore.QCoreApplication.translate
        Dialog_New_Deadtime.setWindowTitle(_translate("Dialog_New_Deadtime", "Dialog"))
        self.label_Deadtime_value.setText(_translate("Dialog_New_Deadtime", "New values (ns)"))
        self.label_Deadtime_title.setText(_translate("Dialog_New_Deadtime", "New deadtime:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_New_Deadtime = QtWidgets.QDialog()
    ui = Ui_Dialog_New_Deadtime()
    ui.setupUi(Dialog_New_Deadtime)
    Dialog_New_Deadtime.show()
    sys.exit(app.exec_())
