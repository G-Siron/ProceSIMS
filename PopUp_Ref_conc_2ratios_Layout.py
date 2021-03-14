# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PopUp_Ref_conc_2ratios_Layout.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_Ref_conc_2ratios(object):
    def setupUi(self, Dialog_Ref_conc_2ratios):
        Dialog_Ref_conc_2ratios.setObjectName("Dialog_Ref_conc_2ratios")
        Dialog_Ref_conc_2ratios.resize(251, 298)
        self.buttonBox_Ref_conc_2ratios_Layout = QtWidgets.QDialogButtonBox(Dialog_Ref_conc_2ratios)
        self.buttonBox_Ref_conc_2ratios_Layout.setGeometry(QtCore.QRect(20, 257, 191, 32))
        self.buttonBox_Ref_conc_2ratios_Layout.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_Ref_conc_2ratios_Layout.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_Ref_conc_2ratios_Layout.setObjectName("buttonBox_Ref_conc_2ratios_Layout")
        self.label_ref_conc1 = QtWidgets.QLabel(Dialog_Ref_conc_2ratios)
        self.label_ref_conc1.setGeometry(QtCore.QRect(30, 47, 141, 16))
        self.label_ref_conc1.setObjectName("label_ref_conc1")
        self.label_conc1 = QtWidgets.QLabel(Dialog_Ref_conc_2ratios)
        self.label_conc1.setGeometry(QtCore.QRect(20, 17, 201, 16))
        self.label_conc1.setObjectName("label_conc1")
        self.label_sigma_conc1 = QtWidgets.QLabel(Dialog_Ref_conc_2ratios)
        self.label_sigma_conc1.setGeometry(QtCore.QRect(30, 90, 151, 16))
        self.label_sigma_conc1.setObjectName("label_sigma_conc1")
        self.label_ref_conc2 = QtWidgets.QLabel(Dialog_Ref_conc_2ratios)
        self.label_ref_conc2.setGeometry(QtCore.QRect(30, 174, 141, 16))
        self.label_ref_conc2.setObjectName("label_ref_conc2")
        self.label_sigma_conc2 = QtWidgets.QLabel(Dialog_Ref_conc_2ratios)
        self.label_sigma_conc2.setGeometry(QtCore.QRect(30, 217, 151, 16))
        self.label_sigma_conc2.setObjectName("label_sigma_conc2")
        self.label_conc2 = QtWidgets.QLabel(Dialog_Ref_conc_2ratios)
        self.label_conc2.setGeometry(QtCore.QRect(20, 143, 201, 16))
        self.label_conc2.setObjectName("label_conc2")
        self.lineEdit_ref_conc1 = QtWidgets.QLineEdit(Dialog_Ref_conc_2ratios)
        self.lineEdit_ref_conc1.setGeometry(QtCore.QRect(190, 40, 40, 30))
        self.lineEdit_ref_conc1.setObjectName("lineEdit_ref_conc1")
        self.lineEdit_sigma_conc1 = QtWidgets.QLineEdit(Dialog_Ref_conc_2ratios)
        self.lineEdit_sigma_conc1.setGeometry(QtCore.QRect(190, 83, 40, 30))
        self.lineEdit_sigma_conc1.setObjectName("lineEdit_sigma_conc1")
        self.lineEdit_ref_conc2 = QtWidgets.QLineEdit(Dialog_Ref_conc_2ratios)
        self.lineEdit_ref_conc2.setGeometry(QtCore.QRect(190, 167, 40, 30))
        self.lineEdit_ref_conc2.setObjectName("lineEdit_ref_conc2")
        self.lineEdit_sigma_conc2 = QtWidgets.QLineEdit(Dialog_Ref_conc_2ratios)
        self.lineEdit_sigma_conc2.setGeometry(QtCore.QRect(190, 210, 40, 30))
        self.lineEdit_sigma_conc2.setObjectName("lineEdit_sigma_conc2")

        self.retranslateUi(Dialog_Ref_conc_2ratios)
        self.buttonBox_Ref_conc_2ratios_Layout.accepted.connect(Dialog_Ref_conc_2ratios.accept)
        self.buttonBox_Ref_conc_2ratios_Layout.rejected.connect(Dialog_Ref_conc_2ratios.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Ref_conc_2ratios)

    def retranslateUi(self, Dialog_Ref_conc_2ratios):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Ref_conc_2ratios.setWindowTitle(_translate("Dialog_Ref_conc_2ratios", "Dialog"))
        self.label_ref_conc1.setText(_translate("Dialog_Ref_conc_2ratios", "Reference value (wt%)"))
        self.label_conc1.setText(_translate("Dialog_Ref_conc_2ratios", "Standard ratio 1 :"))
        self.label_sigma_conc1.setText(_translate("Dialog_Ref_conc_2ratios", "Uncertainty (1SD, wt%)"))
        self.label_ref_conc2.setText(_translate("Dialog_Ref_conc_2ratios", "Reference value (wt%)"))
        self.label_sigma_conc2.setText(_translate("Dialog_Ref_conc_2ratios", "Uncertainty (1SD, wt%)"))
        self.label_conc2.setText(_translate("Dialog_Ref_conc_2ratios", "Standard ratio 2 :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_Ref_conc_2ratios = QtWidgets.QDialog()
    ui = Ui_Dialog_Ref_conc_2ratios()
    ui.setupUi(Dialog_Ref_conc_2ratios)
    Dialog_Ref_conc_2ratios.show()
    sys.exit(app.exec_())

