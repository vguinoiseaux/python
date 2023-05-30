#Ex02-bouton
#Quand on clique sur le bouton, on change le nom du label par Bonjour

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtGui,uic
import sys



class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        uic.loadUi('Ex04-bouton.ui', self)  #chargement du formulaire XML
        self.setFixedSize(self.size())  #la fenêtre principale n'est pas modifiable
        #Quand on clique sur le pushButton, on appelle la méthode boutonOK
        self.PushButton.clicked.connect(self.boutonOk)
        #Quand on clique sur la checkbox, on appelle la méthode chkBox
        self.checkBox.stateChanged.connect(self.chkBox)
        self.show()

    def boutonOk(self):
        print('bouton cliqué')
        chk=self.checkBox.isChecked()    #récupére l'état du checkBox
        print('chk',chk,type(chk)) #affiche dans la console l'état du check box et le type

    def chkBox(self):
        chk=self.checkBox.isChecked()   #récupére l'état du checkBox
        if chk==True:
            self.label.setText("checkBox True") #affiche le résultat dans le label
        else:
            self.label.setText("checkBox False") #affiche le résultat dans le label

app = QApplication(sys.argv)
window = MainWindows()
app.exec_()






