# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PopUp_Ref_conc_3ratios_Layout.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_Ref_conc_3ratios(object):
    def setupUi(self, Dialog_Ref_conc_3ratios):
        Dialog_Ref_conc_3ratios.setObjectName("Dialog_Ref_conc_3ratios")
        Dialog_Ref_conc_3ratios.resize(251, 424)
        self.buttonBox_Ref_conc_3ratios_Layout = QtWidgets.QDialogButtonBox(Dialog_Ref_conc_3ratios)
        self.buttonBox_Ref_conc_3ratios_Layout.setGeometry(QtCore.QRect(20, 384, 191, 32))
        self.buttonBox_Ref_conc_3ratios_Layout.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_Ref_conc_3ratios_Layout.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_Ref_conc_3ratios_Layout.setObjectName("buttonBox_Ref_conc_3ratios_Layout")
        self.label_ref_conc1 = QtWidgets.QLabel(Dialog_Ref_conc_3ratios)
        self.label_ref_conc1.setGeometry(QtCore.QRect(30, 47, 141, 16))
        self.label_ref_conc1.setObjectName("label_ref_conc1")
        self.label_conc1 = QtWidgets.QLabel(Dialog_Ref_conc_3ratios)
        self.label_conc1.setGeometry(QtCore.QRect(20, 17, 201, 16))
        self.label_conc1.setObjectName("label_conc1")
        self.label_sigma_conc1 = QtWidgets.QLabel(Dialog_Ref_conc_3ratios)
        self.label_sigma_conc1.setGeometry(QtCore.QRect(30, 90, 151, 16))
        self.label_sigma_conc1.setObjectName("label_sigma_conc1")
        self.label_ref_conc2 = QtWidgets.QLabel(Dialog_Ref_conc_3ratios)
        self.label_ref_conc2.setGeometry(QtCore.QRect(30, 174, 141, 16))
        self.label_ref_conc2.setObjectName("label_ref_conc2")
        self.label_sigma_conc2 = QtWidgets.QLabel(Dialog_Ref_conc_3ratios)
        self.label_sigma_conc2.setGeometry(QtCore.QRect(30, 217, 151, 16))
        self.label_sigma_conc2.setObjectName("label_sigma_conc2")
        self.label_conc2 = QtWidgets.QLabel(Dialog_Ref_conc_3ratios)
        self.label_conc2.setGeometry(QtCore.QRect(20, 143, 201, 16))
        self.label_conc2.setObjectName("label_conc2")
        self.label_ref_conc3 = QtWidgets.QLabel(Dialog_Ref_conc_3ratios)
        self.label_ref_conc3.setGeometry(QtCore.QRect(30, 301, 141, 16))
        self.label_ref_conc3.setObjectName("label_ref_conc3")
        self.label_sigma_conc3 = QtWidgets.QLabel(Dialog_Ref_conc_3ratios)
        self.label_sigma_conc3.setGeometry(QtCore.QRect(30, 344, 151, 16))
        self.label_sigma_conc3.setObjectName("label_sigma_conc3")
        self.label_conc3 = QtWidgets.QLabel(Dialog_Ref_conc_3ratios)
        self.label_conc3.setGeometry(QtCore.QRect(20, 270, 201, 16))
        self.label_conc3.setObjectName("label_conc3")
        self.lineEdit_ref_conc1 = QtWidgets.QLineEdit(Dialog_Ref_conc_3ratios)
        self.lineEdit_ref_conc1.setGeometry(QtCore.QRect(190, 40, 40, 30))
        self.lineEdit_ref_conc1.setObjectName("lineEdit_ref_conc1")
        self.lineEdit_sigma_conc1 = QtWidgets.QLineEdit(Dialog_Ref_conc_3ratios)
        self.lineEdit_sigma_conc1.setGeometry(QtCore.QRect(190, 83, 40, 30))
        self.lineEdit_sigma_conc1.setObjectName("lineEdit_sigma_conc1")
        self.lineEdit_ref_conc2 = QtWidgets.QLineEdit(Dialog_Ref_conc_3ratios)
        self.lineEdit_ref_conc2.setGeometry(QtCore.QRect(190, 167, 40, 30))
        self.lineEdit_ref_conc2.setObjectName("lineEdit_ref_conc2")
        self.lineEdit_sigma_conc2 = QtWidgets.QLineEdit(Dialog_Ref_conc_3ratios)
        self.lineEdit_sigma_conc2.setGeometry(QtCore.QRect(190, 210, 40, 30))
        self.lineEdit_sigma_conc2.setObjectName("lineEdit_sigma_conc2")
        self.lineEdit_ref_conc3 = QtWidgets.QLineEdit(Dialog_Ref_conc_3ratios)
        self.lineEdit_ref_conc3.setGeometry(QtCore.QRect(190, 294, 40, 30))
        self.lineEdit_ref_conc3.setObjectName("lineEdit_ref_conc3")
        self.lineEdit_sigma_conc3 = QtWidgets.QLineEdit(Dialog_Ref_conc_3ratios)
        self.lineEdit_sigma_conc3.setGeometry(QtCore.QRect(190, 337, 40, 30))
        self.lineEdit_sigma_conc3.setObjectName("lineEdit_sigma_conc3")

        self.retranslateUi(Dialog_Ref_conc_3ratios)
        self.buttonBox_Ref_conc_3ratios_Layout.accepted.connect(Dialog_Ref_conc_3ratios.accept)
        self.buttonBox_Ref_conc_3ratios_Layout.rejected.connect(Dialog_Ref_conc_3ratios.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Ref_conc_3ratios)

    def retranslateUi(self, Dialog_Ref_conc_3ratios):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Ref_conc_3ratios.setWindowTitle(_translate("Dialog_Ref_conc_3ratios", "Dialog"))
        self.label_ref_conc1.setText(_translate("Dialog_Ref_conc_3ratios", "Reference value (wt%)"))
        self.label_conc1.setText(_translate("Dialog_Ref_conc_3ratios", "Standard ratio 1 :"))
        self.label_sigma_conc1.setText(_translate("Dialog_Ref_conc_3ratios", "Uncertainty (1SD, wt%)"))
        self.label_ref_conc2.setText(_translate("Dialog_Ref_conc_3ratios", "Reference value (wt%)"))
        self.label_sigma_conc2.setText(_translate("Dialog_Ref_conc_3ratios", "Uncertainty (1SD, wt%)"))
        self.label_conc2.setText(_translate("Dialog_Ref_conc_3ratios", "Standard ratio 2 :"))
        self.label_ref_conc3.setText(_translate("Dialog_Ref_conc_3ratios", "Reference value (wt%)"))
        self.label_sigma_conc3.setText(_translate("Dialog_Ref_conc_3ratios", "Uncertainty (1SD, wt%)"))
        self.label_conc3.setText(_translate("Dialog_Ref_conc_3ratios", "Standard ratio 3 :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_Ref_conc_3ratios = QtWidgets.QDialog()
    ui = Ui_Dialog_Ref_conc_3ratios()
    ui.setupUi(Dialog_Ref_conc_3ratios)
    Dialog_Ref_conc_3ratios.show()
    sys.exit(app.exec_())

