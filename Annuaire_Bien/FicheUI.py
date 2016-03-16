# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ficheUi.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(487, 191)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.Nom = QtGui.QLabel(Dialog)
        self.Nom.setMinimumSize(QtCore.QSize(16, 0))
        self.Nom.setObjectName(_fromUtf8("Nom"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.Nom)
        self.lineNom = QtGui.QLineEdit(Dialog)
        self.lineNom.setObjectName(_fromUtf8("lineNom"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineNom)
        self.Prenom = QtGui.QLabel(Dialog)
        self.Prenom.setObjectName(_fromUtf8("Prenom"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.Prenom)
        self.linePrenom = QtGui.QLineEdit(Dialog)
        self.linePrenom.setObjectName(_fromUtf8("linePrenom"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.linePrenom)
        self.lineAdresse = QtGui.QLineEdit(Dialog)
        self.lineAdresse.setObjectName(_fromUtf8("lineAdresse"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineAdresse)
        self.Mail = QtGui.QLabel(Dialog)
        self.Mail.setObjectName(_fromUtf8("Mail"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.Mail)
        self.lineMail = QtGui.QLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineMail.sizePolicy().hasHeightForWidth())
        self.lineMail.setSizePolicy(sizePolicy)
        self.lineMail.setObjectName(_fromUtf8("lineMail"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineMail)
        self.NumeroTel = QtGui.QLabel(Dialog)
        self.NumeroTel.setObjectName(_fromUtf8("NumeroTel"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.NumeroTel)
        self.lineNumeroTel = QtGui.QLineEdit(Dialog)
        self.lineNumeroTel.setObjectName(_fromUtf8("lineNumeroTel"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineNumeroTel)
        self.Adresse = QtGui.QLabel(Dialog)
        self.Adresse.setObjectName(_fromUtf8("Adresse"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.Adresse)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.Nom.setText(_translate("Dialog", "Nom", None))
        self.Prenom.setText(_translate("Dialog", "Prenom", None))
        self.Mail.setText(_translate("Dialog", "@mail", None))
        self.NumeroTel.setText(_translate("Dialog", "Numero tel", None))
        self.Adresse.setText(_translate("Dialog", "Adresse", None))

