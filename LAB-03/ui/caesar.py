# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/caesar.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(732, 567)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(220, 20, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(300, 60, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 220, 55, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 280, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.plaintext_txt = QtWidgets.QPlainTextEdit(Dialog)
        self.plaintext_txt.setGeometry(QtCore.QRect(150, 110, 531, 87))
        self.plaintext_txt.setObjectName("plaintext_txt")
        self.key_txt = QtWidgets.QLineEdit(Dialog)
        self.key_txt.setGeometry(QtCore.QRect(150, 230, 531, 22))
        self.key_txt.setObjectName("key_txt")
        self.ciphertext_txt = QtWidgets.QPlainTextEdit(Dialog)
        self.ciphertext_txt.setGeometry(QtCore.QRect(150, 280, 531, 171))
        self.ciphertext_txt.setObjectName("ciphertext_txt")
        self.encrypt_btn = QtWidgets.QPushButton(Dialog)
        self.encrypt_btn.setGeometry(QtCore.QRect(210, 500, 93, 28))
        self.encrypt_btn.setObjectName("encrypt_btn")
        self.decrypt_btn = QtWidgets.QPushButton(Dialog)
        self.decrypt_btn.setGeometry(QtCore.QRect(470, 500, 93, 28))
        self.decrypt_btn.setObjectName("decrypt_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "CAESAR CIPHER"))
        self.label_2.setText(_translate("Dialog", "Lê Duy Hải - 2280600799"))
        self.label_3.setText(_translate("Dialog", "Plain text"))
        self.label_4.setText(_translate("Dialog", "Key"))
        self.label_5.setText(_translate("Dialog", "Cipher text"))
        self.encrypt_btn.setText(_translate("Dialog", "Encrypt"))
        self.decrypt_btn.setText(_translate("Dialog", "Decrypt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
