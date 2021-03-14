# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PopUp_Ref_conc_1ratio_Layout.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_Ref_1ratio_conc(object):
    def setupUi(self, Dialog_Ref_1ratio_conc):
        Dialog_Ref_1ratio_conc.setObjectName("Dialog_Ref_1ratio_conc")
        Dialog_Ref_1ratio_conc.resize(251, 176)
        self.buttonBox_Ref_conc_1std_Layout = QtWidgets.QDialogButtonBox(Dialog_Ref_1ratio_conc)
        self.buttonBox_Ref_conc_1std_Layout.setGeometry(QtCore.QRect(20, 130, 191, 32))
        self.buttonBox_Ref_conc_1std_Layout.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_Ref_conc_1std_Layout.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_Ref_conc_1std_Layout.setObjectName("buttonBox_Ref_conc_1std_Layout")
        self.label_ref_std = QtWidgets.QLabel(Dialog_Ref_1ratio_conc)
        self.label_ref_std.setGeometry(QtCore.QRect(30, 47, 141, 16))
        self.label_ref_std.setObjectName("label_ref_std")
        self.label_std = QtWidgets.QLabel(Dialog_Ref_1ratio_conc)
        self.label_std.setGeometry(QtCore.QRect(20, 17, 201, 16))
        self.label_std.setObjectName("label_std")
        self.label_sigma_std = QtWidgets.QLabel(Dialog_Ref_1ratio_conc)
        self.label_sigma_std.setGeometry(QtCore.QRect(30, 90, 151, 16))
        self.label_sigma_std.setObjectName("label_sigma_std")
        self.lineEdit_Ref_conc1 = QtWidgets.QLineEdit(Dialog_Ref_1ratio_conc)
        self.lineEdit_Ref_conc1.setGeometry(QtCore.QRect(190, 40, 40, 30))
        self.lineEdit_Ref_conc1.setObjectName("lineEdit_Ref_conc1")
        self.lineEdit_sigma_conc1 = QtWidgets.QLineEdit(Dialog_Ref_1ratio_conc)
        self.lineEdit_sigma_conc1.setGeometry(QtCore.QRect(190, 83, 40, 30))
        self.lineEdit_sigma_conc1.setObjectName("lineEdit_sigma_conc1")

        self.retranslateUi(Dialog_Ref_1ratio_conc)
        self.buttonBox_Ref_conc_1std_Layout.accepted.connect(Dialog_Ref_1ratio_conc.accept)
        self.buttonBox_Ref_conc_1std_Layout.rejected.connect(Dialog_Ref_1ratio_conc.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Ref_1ratio_conc)

    def retranslateUi(self, Dialog_Ref_1ratio_conc):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Ref_1ratio_conc.setWindowTitle(_translate("Dialog_Ref_1ratio_conc", "Dialog"))
        self.label_ref_std.setText(_translate("Dialog_Ref_1ratio_conc", "Reference value (wt%)"))
        self.label_std.setText(_translate("Dialog_Ref_1ratio_conc", "Standard :"))
        self.label_sigma_std.setText(_translate("Dialog_Ref_1ratio_conc", "Uncertainty (1SD, wt%)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_Ref_1ratio_conc = QtWidgets.QDialog()
    ui = Ui_Dialog_Ref_1ratio_conc()
    ui.setupUi(Dialog_Ref_1ratio_conc)
    Dialog_Ref_1ratio_conc.show()
    sys.exit(app.exec_())

