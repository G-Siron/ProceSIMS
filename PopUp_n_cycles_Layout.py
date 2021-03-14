# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PopUp_n_cycles_Layout.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_new_n_cycles(object):
    def setupUi(self, Dialog_new_n_cycles):
        Dialog_new_n_cycles.setObjectName("Dialog_new_n_cycles")
        Dialog_new_n_cycles.resize(239, 127)
        self.buttonBox_Ref_iso_Layout = QtWidgets.QDialogButtonBox(Dialog_new_n_cycles)
        self.buttonBox_Ref_iso_Layout.setGeometry(QtCore.QRect(10, 90, 191, 32))
        self.buttonBox_Ref_iso_Layout.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_Ref_iso_Layout.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_Ref_iso_Layout.setObjectName("buttonBox_Ref_iso_Layout")
        self.label_n_cycles = QtWidgets.QLabel(Dialog_new_n_cycles)
        self.label_n_cycles.setGeometry(QtCore.QRect(30, 47, 134, 16))
        self.label_n_cycles.setObjectName("label_n_cycles")
        self.label_new_n_cycles = QtWidgets.QLabel(Dialog_new_n_cycles)
        self.label_new_n_cycles.setGeometry(QtCore.QRect(20, 17, 201, 16))
        self.label_new_n_cycles.setObjectName("label_new_n_cycles")
        self.lineEdit_n_cycles = QtWidgets.QLineEdit(Dialog_new_n_cycles)
        self.lineEdit_n_cycles.setGeometry(QtCore.QRect(180, 40, 40, 30))
        self.lineEdit_n_cycles.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_n_cycles.setObjectName("lineEdit_n_cycles")

        self.retranslateUi(Dialog_new_n_cycles)
        self.buttonBox_Ref_iso_Layout.accepted.connect(Dialog_new_n_cycles.accept)
        self.buttonBox_Ref_iso_Layout.rejected.connect(Dialog_new_n_cycles.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_new_n_cycles)

    def retranslateUi(self, Dialog_new_n_cycles):
        _translate = QtCore.QCoreApplication.translate
        Dialog_new_n_cycles.setWindowTitle(_translate("Dialog_new_n_cycles", "Dialog"))
        self.label_n_cycles.setText(_translate("Dialog_new_n_cycles", "Number of cylces"))
        self.label_new_n_cycles.setText(_translate("Dialog_new_n_cycles", "New number of cycles:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_new_n_cycles = QtWidgets.QDialog()
    ui = Ui_Dialog_new_n_cycles()
    ui.setupUi(Dialog_new_n_cycles)
    Dialog_new_n_cycles.show()
    sys.exit(app.exec_())
