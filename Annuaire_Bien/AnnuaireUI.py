# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'annuaireUi.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(781, 601)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("image/imageGroupe.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.Editer = QtGui.QPushButton(self.centralwidget)
        self.Editer.setMinimumSize(QtCore.QSize(100, 70))
        self.Editer.setMaximumSize(QtCore.QSize(150, 16777214))
        self.Editer.setStyleSheet(_fromUtf8("background-color: #009e9f"))
        self.Editer.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("image/editerContact.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Editer.setIcon(icon)
        self.Editer.setIconSize(QtCore.QSize(70, 70))
        self.Editer.setObjectName(_fromUtf8("Editer"))
        self.gridLayout_2.addWidget(self.Editer, 1, 0, 1, 1)
        self.Ajouter = QtGui.QPushButton(self.centralwidget)
        self.Ajouter.setMinimumSize(QtCore.QSize(100, 70))
        self.Ajouter.setMaximumSize(QtCore.QSize(150, 16777214))
        self.Ajouter.setSizeIncrement(QtCore.QSize(0, 0))
        self.Ajouter.setBaseSize(QtCore.QSize(0, 0))
        self.Ajouter.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Ajouter.setAutoFillBackground(False)
        self.Ajouter.setStyleSheet(_fromUtf8("background-color: #009e9f"))
        self.Ajouter.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("image/suppContact.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Ajouter.setIcon(icon1)
        self.Ajouter.setIconSize(QtCore.QSize(70, 70))
        self.Ajouter.setAutoDefault(False)
        self.Ajouter.setDefault(False)
        self.Ajouter.setFlat(False)
        self.Ajouter.setObjectName(_fromUtf8("Ajouter"))
        self.gridLayout_2.addWidget(self.Ajouter, 0, 0, 1, 1)
        self.Supprimer = QtGui.QPushButton(self.centralwidget)
        self.Supprimer.setMinimumSize(QtCore.QSize(100, 70))
        self.Supprimer.setMaximumSize(QtCore.QSize(150, 16777214))
        self.Supprimer.setStyleSheet(_fromUtf8("background-color: #009e9f"))
        self.Supprimer.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("image/ajoutContact.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Supprimer.setIcon(icon2)
        self.Supprimer.setIconSize(QtCore.QSize(70, 70))
        self.Supprimer.setObjectName(_fromUtf8("Supprimer"))
        self.gridLayout_2.addWidget(self.Supprimer, 2, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("image/tnew_spotlight-icon2.png")))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_4.addWidget(self.label_2)
        self.Rechercher = QtGui.QLineEdit(self.centralwidget)
        self.Rechercher.setObjectName(_fromUtf8("Rechercher"))
        self.horizontalLayout_4.addWidget(self.Rechercher)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.Annuaire = QtGui.QTreeWidget(self.centralwidget)
        self.Annuaire.setObjectName(_fromUtf8("Annuaire"))
        self.verticalLayout.addWidget(self.Annuaire)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 781, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuNouveau = QtGui.QMenu(self.menubar)
        self.menuNouveau.setObjectName(_fromUtf8("menuNouveau"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNouveau = QtGui.QAction(MainWindow)
        self.actionNouveau.setObjectName(_fromUtf8("actionNouveau"))
        self.actionOuvrir = QtGui.QAction(MainWindow)
        self.actionOuvrir.setObjectName(_fromUtf8("actionOuvrir"))
        self.actionEnregistrer = QtGui.QAction(MainWindow)
        self.actionEnregistrer.setObjectName(_fromUtf8("actionEnregistrer"))
        self.actionEnregistrer_sous = QtGui.QAction(MainWindow)
        self.actionEnregistrer_sous.setObjectName(_fromUtf8("actionEnregistrer_sous"))
        self.actionImprimer = QtGui.QAction(MainWindow)
        self.actionImprimer.setObjectName(_fromUtf8("actionImprimer"))
        self.actionQuitter = QtGui.QAction(MainWindow)
        self.actionQuitter.setObjectName(_fromUtf8("actionQuitter"))
        self.menuNouveau.addAction(self.actionNouveau)
        self.menuNouveau.addAction(self.actionOuvrir)
        self.menuNouveau.addSeparator()
        self.menuNouveau.addAction(self.actionEnregistrer)
        self.menuNouveau.addAction(self.actionEnregistrer_sous)
        self.menuNouveau.addSeparator()
        self.menuNouveau.addAction(self.actionImprimer)
        self.menuNouveau.addSeparator()
        self.menuNouveau.addAction(self.actionQuitter)
        self.menubar.addAction(self.menuNouveau.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_2.setText(_translate("MainWindow", "Recherche", None))
        self.Annuaire.headerItem().setText(0, _translate("MainWindow", "Nom", None))
        self.Annuaire.headerItem().setText(1, _translate("MainWindow", "Prenom", None))
        self.Annuaire.headerItem().setText(2, _translate("MainWindow", "Adresse", None))
        self.Annuaire.headerItem().setText(3, _translate("MainWindow", "@mail", None))
        self.Annuaire.headerItem().setText(4, _translate("MainWindow", "N° telephone", None))
        self.menuNouveau.setTitle(_translate("MainWindow", "Fichier", None))
        self.actionNouveau.setText(_translate("MainWindow", "Nouveau...", None))
        self.actionOuvrir.setText(_translate("MainWindow", "Ouvrir...", None))
        self.actionEnregistrer.setText(_translate("MainWindow", "Enregistrer", None))
        self.actionEnregistrer_sous.setText(_translate("MainWindow", "Enregistrer sous...", None))
        self.actionImprimer.setText(_translate("MainWindow", "Imprimer", None))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter", None))

