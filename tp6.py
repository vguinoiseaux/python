"""
phrase = "bonjour"
print (phrase[1:4])
"""
"""
chaine = "NE PARLEZ PAS SI FORT !"
print(chaine.lower())
chaine="nsi"
chaine=chaine.upper()
print(chaine)
"""
"""
w = "Washington"
t= "Touchard"
lycee= w+" "+t
print (lycee)
print (len(lycee))
"""
"""
chaine = "Bonjour"
for i in range(0, len(chaine)):
    print(chaine[i], end = '')

chaine = "Au revoir"
for c in chaine:
    print(c, end = '')
"""
"""
chaine=str(input("votre chaine ?"))
if chaine=='bonjour':
    print('hello')
else:
    print('j\'ai rien compris')
"""
"""
s = "Welcome"
print(s[-1])
print(s[-2])
"""
"""
s = "Welcome"
print(s[:6])
print(s[4:])
print(s[1:-1])
"""
"""
s = "Hello computer"
print(s.endswith("uter"))
print(s.startswith("good"))
print(s.find("comp"))
print(s.rfind("o"))
print(s.count("o"))
"""
"""
chaine = "\r  Bien le bonjour\t \t"
s = chaine.strip()
print(s)
"""
"""
ch = 'A'
print(ord(ch))
"""
"""
valeur=66
print(chr(valeur))
"""
"""
chaine = "10.5"
print(type(chaine))
valeur=float(chaine)
print(type(valeur))
print(valeur)
"""
"""
def compteLettre(lettre,chaine):
    return chaine.count(lettre)
print(compteLettre('e','je vais au cine ce soir'))
"""
"""
def compteLettre(lettre,chaine):
    total =0
    for i in range (len(chaine)):
        if chaine[i]==lettre:
            total+=1
    return total


print(compteLettre('e','je vais au cine ce soir'))
"""
"""
def fonctionpremierMot(chaine):
    i=chaine.find(" ")
    return chaine[:i]


print(fonctionpremierMot("enfin il arrête de pleuvoir "))
"""
"""
print("Un peu \nBeaucoup \nPassionnément")
"""
"""
semaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
for i in range (len(semaine)):
    print(semaine[i],"\n")
"""
"""
semaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
départ=2
for n in range (1,32):
    print(semaine[(n+départ)%7],n,"décembre")

"""

voyelles=['a','e','i','o','u','y']

def compteVoyelles(chaine):
    i=chaine.find(str(voyelles))
    return compteVoyelles(i)


chaine=input("votre chaine ?")
print(chaine,compteVoyelles(chaine))


