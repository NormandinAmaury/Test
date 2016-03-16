from PyQt4 import QtCore, QtGui
from AnnuaireUI import Ui_MainWindow
from FicheUI import Ui_Dialog
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from SupprimerUI import Ui_Dialog_Supprimer


class View(QtGui.QMainWindow):# La classe view qui sera utilisée dans le main.
    """La classe View"""
    ui = Ui_MainWindow()#Le ui est la fenetre afficher qui sera appelé a etre afficher
    #ici la MainWindow qui est la fenetre principal créer dans annuaire.
    nombreItems = 0# Nombre d'items dans l'annuiare.

    def __init__(self, app=QtGui.QApplication, parent=None):#définition du constructeur.
        super(View,self).__init__(parent)#Constructeur Parent (ici rien)


        self.ui.setupUi(self)#Afiche dès qu'un classe view est créer le ui déclarer précédemment (MainWindow)

        QtCore.QObject.connect(self.ui.actionQuitter, QtCore.SIGNAL('triggered()'), app, QtCore.SLOT('quit()'))#les bouton et leurs actions.
        QtCore.QObject.connect(self.ui.actionEnregistrer_sous, QtCore.SIGNAL('triggered()'), self.saveas)
        QtCore.QObject.connect(self.ui.actionOuvrir, QtCore.SIGNAL('triggered()'), self.open)
        QtCore.QObject.connect(self.ui.Ajouter, QtCore.SIGNAL('clicked()'), self.ouvrirFiche)
        QtCore.QObject.connect(self.ui.Editer, QtCore.SIGNAL('clicked()'), self.editerFiche)
        QtCore.QObject.connect(self.ui.Supprimer, QtCore.SIGNAL('clicked()'), self.supprimerFiche)
        QtCore.QObject.connect(self.ui.Rechercher, QtCore.SIGNAL('textChanged(QString)'), self.rechercherNom)


    def open (self):
        file = open('newfile.txt', 'r')
        caractere=","
        for line in file:
            item = QtGui.QTreeWidgetItem()
            y=-1
            for x in line.split(caractere):
                y+=1
                item.setText(y,x)
            self.ui.Annuaire.addTopLevelItem(item)
            self.nombreItems = (self.nombreItems + 1)
        print (self.nombreItems)

        """
            for a in line:
                if (a!=' '):
                    nom += a
                else:
                    print (nom)
                    item.setText(0, "".join(nom))
                    self.ui.Annuaire.addTopLevelItem(item)
                    nom=[]
                    self.nombreItems += 1
                    break"""

            # for a in line:
             #  while (a!=' '):
              #      nom += a
               #     break
                #print (nom)


    def saveas (self):
        file = open("newfile.txt", "w")
        for a in range(self.nombreItems):
                nom = self.ui.Annuaire.topLevelItem(a).text(0)
                prenom = self.ui.Annuaire.topLevelItem(a).text(1)
                adresse = self.ui.Annuaire.topLevelItem(a).text(2)
                mail = self.ui.Annuaire.topLevelItem(a).text(3)
                numeroTel = self.ui.Annuaire.topLevelItem(a).text(4)
                file.write(nom+" ,"+prenom+" ,"+adresse+" ,"+mail+" ,"+numeroTel+','+'\n')

        file.close()



    def ouvrirFiche(self):#Methode pour ajouter quelqu'un dans l'annuaire.
        ui = Ui_Dialog()#nouvel UI de type dialogue
        fiche = QtGui.QDialog()

        ui.setupUi(fiche)#affichage deuxième fenetre.

        if fiche.exec_():#Si la dialogue est validé.

            item = QtGui.QTreeWidgetItem()#Item est le QTreeWidgetItem ici note receptacle et afficheur de personne.
            item.setText(0, ui.lineNom.text())#Chaque ligne est remplie en fct de de ce qui est remplie dans la dialogue.
            item.setText(1, ui.linePrenom.text())
            item.setText(2, ui.lineAdresse.text())
            item.setText(3, ui.lineMail.text())
            item.setText(4, ui.lineNumeroTel.text())
            if self.nombreItems == 0:#si le tableau est vide .
                self.ui.Annuaire.addTopLevelItem(item)#on ajjoute directement l'item dans le tableau
                self.nombreItems = (self.nombreItems + 1)#le nombreItem passe de 0 à 1.
            else:
                for a in range(self.nombreItems):#On parcours le tableau grace à sa taille (nbre de personnes)
                    if ui.lineNom.text() == self.ui.Annuaire.topLevelItem(a).text(0):#Si le txt de lineNom ajouté égal au txt
                        #de la premiere colone (le nom) de l'object parcourue.
                        print("Déja dans l'annuaire")#Afficher (console)
                        break#Terminer la boucle
                else:
                    self.ui.Annuaire.addTopLevelItem(item)#Sinon ajouter en haut du widget le nouvel objet
                    self.nombreItems = (self.nombreItems + 1)#ajouter 1 au nombres d'éléménts

        self.triOrdreAlphabetique()#Trier par orde alphabétique à la fin.




    def supprimerFiche(self):#fct supprimer un élément.
        for a in range(self.nombreItems):#Parcour tableau
            if self.ui.Annuaire.topLevelItem(a).isSelected():#Si l'objet parcouru est séléctioner dans le widget
                self.ui.Annuaire.topLevelItem(a).removeChild(self.ui.Annuaire.topLevelItem(a))#Supression de l'object
                self.nombreItems = (self.nombreItems - 1)#Il y a un objet en moins
                break#fin
        else:
            print("il n'y a pas ce nom dans l'annuaire!")


    def editerFiche(self):#fct pour éditer la fiche.
        for a in range(self.nombreItems):#Parcours le treewidget
            if self.ui.Annuaire.topLevelItem(a).isSelected():#Si l'objet parcouru est séléctioner dans le widget
                nom = self.ui.Annuaire.topLevelItem(a).text(0)#on met dans des variables les valeurs du treewidget
                prenom = self.ui.Annuaire.topLevelItem(a).text(1)
                adresse = self.ui.Annuaire.topLevelItem(a).text(2)
                mail = self.ui.Annuaire.topLevelItem(a).text(3)
                numeroTel = self.ui.Annuaire.topLevelItem(a).text(4)

                ui = Ui_Dialog()#Nouvel Ui de type dialogue
                fiche = QtGui.QDialog()

                ui.setupUi(fiche)#Création de la fiche.
                ui.lineNom.setText(nom)#Les variables enregistrée précédement sont mise dans les zones de textes de la fenetre
                ui.linePrenom.setText(prenom)
                ui.lineAdresse.setText(adresse)
                ui.lineMail.setText(mail)
                ui.lineNumeroTel.setText(numeroTel)

                if fiche.exec_():#same thing as the ouvrir fiche
                    item = QtGui.QTreeWidgetItem()
                    item.setText(0, ui.lineNom.text())
                    item.setText(1, ui.linePrenom.text())
                    item.setText(2, ui.lineAdresse.text())
                    item.setText(3, ui.lineMail.text())
                    item.setText(4, ui.lineNumeroTel.text())

                    for b in range(self.nombreItems):#parcours treewidget
                        if ui.lineNom.text() == self.ui.Annuaire.topLevelItem(b).text(0):#Si le txt de lineNom ajouté égal au txt
                        #de la premiere colone (le nom) de l'object parcourue.
                            print("Déja dans l'annuaire")
                            break
                    else:
                        self.ui.Annuaire.topLevelItem(a).removeChild(self.ui.Annuaire.topLevelItem(a))#supression ancien item
                        self.ui.Annuaire.addTopLevelItem(item)#ajout nouveau item
                        self.triOrdreAlphabetique()#trie
                break

    def triOrdreAlphabetique(self):
        self.ui.Annuaire.sortItems(0,QtCore.Qt.AscendingOrder)



    def rechercherNom(self):
        print('ok')

        '''ui = Ui_Dialog_Supprimer()
        rechercher = QtGui.QDialog()

        ui.setupUi(rechercher)

        if rechercher.exec_():
            item = ui.lineNom.text()
            for a in range(self.nombreItems):
                if item == (self.ui.Annuaire.topLevelItem(a)).text(0):
                    print("Nom : " + self.ui.Annuaire.topLevelItem(a).text(0))
                    print("Prenom : " + self.ui.Annuaire.topLevelItem(a).text(1))
                    print("Age : " + self.ui.Annuaire.topLevelItem(a).text(2))
                    print("Adresse : " + self.ui.Annuaire.topLevelItem(a).text(3))
                    print("Numero Telephone : " + self.ui.Annuaire.topLevelItem(a).text(4))
                    break
            else:
                print("il n'y a pas ce nom dans l'annuaire!")'''