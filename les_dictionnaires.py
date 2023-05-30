import csv
from pylab import *


def listePourUneCle(liste_dico, cle):
    resultat=[]
    for dico in liste_dico:
        resultat.append(float(dico[cle]))
    return resultat


fichier = open("ballon2019.csv", "r", encoding="utf-8")
lecture_fichier = csv.DictReader(fichier, delimiter=',')
liste_enregistrements = []
for ligne in lecture_fichier:
    liste_enregistrements.append(dict(ligne))
fichier.close()

liste_altitudes = listePourUneCle(liste_enregistrements,"Altitude m")
liste_temperatures = listePourUneCle(liste_enregistrements,"Temp Ext C")

x = liste_altitudes
y = liste_temperatures
plot(x,y)

show()
