"""
def afficheTuple(tuple):
	prenom, nom, adresse, codePostal, ville=tuple
	print('prenom :',prenom)
	print('nom :',nom)
	print('adresse :',adresse)
	print('code postal :',codePostal)
	print('ville :',ville)


tuple=('bruce','wayne','3 impasse de la chauve souris',72000,'le mans')
print(tuple)
"""
"""
def calcul(x, coefficientsDroite):
	a, b=coefficientsDroite
	y=a*x+b
	return y

coefficients=(2,1)
print("La valeur de y pour x=2 est: y=",calcul(2,coefficients))
"""
"""
from math import*
def distance(ptA, ptB ):
	    xA,yA=ptA
	    xB,yB=ptB
	    AB=sqrt((xB-xA)**2+(yB-yA)**2)
	    return AB

pointA=(1,1)
pointB=(2,2)
print(distance(pointA,pointB))
"""
"""
def rechercheMin(liste):
	min = liste[0]
	for indice in range (1,len(liste)):
		if liste[indice] < min:
			min = liste[indice]
	return min
liste=[20,8,9,2,35,49]
print(rechercheMin(liste))
"""
"""
def rechercheMax(liste):
	max = liste[0]
	for indice in range (1,len(liste)):
		if liste[indice] > max:
			max = liste[indice]
	return max
liste=[20,8,9,2,35,49]
print(rechercheMax(liste))
"""
"""
liste=[5,6,7,8,9,4]
somme=0
for n in range(len(liste)):
    somme=somme+liste[n]
print(somme)
"""
"""
def moyenneVersion1(liste):
    total=0
    for i in range(len(lst)):
        total=total+lst[i]
    moyenneVersion1=total/len(lst)

    return moyenneVersion1
lst=[20,8,9,2,35,49]
print(moyenneVersion1(lst))
"""
"""
def moyenneVersion2(liste):
        moy=sum(lst)/len(lst)
        return moy
lst=[20,8,9,2,35,49]
print(moyenneVersion2(lst))
"""
def rechercheMin(liste):
	min = liste[0]
	for indice in range (1,len(liste)):
		if liste[indice] < min:
                    min = liste[indice]
	return min
liste=[20,8,9,2,35,49]
print(rechercheMin(liste))
def rechercheMax(liste):
	max = liste[0]
	for indice in range (1,len(liste)):
		if liste[indice] > max:
			max = liste[indice]
	return max
liste=[20,8,9,2,35,49]
print(rechercheMax(liste))
def moyenneVersion2(liste):
        moy=sum(lst)/len(lst)
        return moy
lst=[20,8,9,2,35,49]
print(moyenneVersion2(lst))
