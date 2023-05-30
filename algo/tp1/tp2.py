# Créé par VALENTIN.GUINOISEAUX, le 04/10/2022 en Python 3.7
"""
for n in range (1,16):
    print(n)
"""
"""
for n in range (15,-1,-1):
    print(n)
"""
"""
d=int(input("votre valeur de debut est :"))
f=int(input("votre valeur de fin est :"))
for n in range(d,f+1,1):
    print(n)
"""
"""
x=int(input("les 10 nombres suivant de "))
print("sont : ")
for n in range(x+1,x+10,1):
  print(n)
"""
"""
n=int(input("choisi un chiffre "))
for i in range (1,11):
    print(n,"*",i,"=",n*i)
"""
"""
n=int(input("choisi un chiffre "))
for i in range (1,6):
    print(n,"*",i,"=",n*i)
if n>=0:
    print("le nombre le plus grand est",n*5)
else:
    print("le nombre le plus grand est",n*1)
"""
"""
valeur=0
max=0
while valeur>=0:
    valeur=int(input("choisi un chiffre "))
    if valeur>max:
        max=valeur
print("le nombre le plus grand est",max)
"""
"""
valeur=0
somme=0
while valeur >=0:
    valeur=int(input("choisi des nombres positif "))
    somme=somme+valeur
    if valeur<0:
        print("la somme des nombres est",somme)
    else:
        print("la somme =",somme)
"""
"""
menu=0
while menu !="q":
    print("1 : charger le fichier")
    print ("2 : sauvegarder le fichier")
    print ("3 : afficher les données")
    print ("4 : modifier les données")
    print ("q : quitter")
    menu=input("votre choix ?")
    if menu=='1':
        print("Chargement...")
    elif menu=='2':
        print("Sauvegarde...")
    elif menu=='3':
        print("Affichage...")
    elif menu=='4':
        print("modification...")
    elif menu=='q':
        print("Au revoir")
    else:
        print("erreur")
"""
"""
from random import *
nombre=randint(1,20)
valeur=0
while valeur != nombre :
    print("votre chiffre")
    valeur=int(input("choisi un chiffre"))
    if valeur>nombre:
	       print("chiffre trop grand")
    elif valeur<nombre:
	       print("chiffre trop petit")
    else:
	       print("exact")
"""
"""
from random import *
nombre=randint(1,10)
valeur=0
coups=0
while valeur != nombre :
    coups=coups+1
    print("votre chiffre")
    valeur=int(input("choisi un chiffre "))
    if valeur>nombre:
	       print("chiffre trop grand ")
    elif valeur<nombre:
	       print("chiffre trop petit ")
    else:
           print("exact vous avez trouvé en",coups,"coups")
"""
from random import*
rep='O'



