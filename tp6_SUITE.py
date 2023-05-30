# Créé par VALENTIN.GUINOISEAUX, le 08/12/2022 en Python 3.7
"""
brailles = ['⠀','⠮','⠐','⠼','⠫','⠩','⠯','⠄','⠷','⠾','⠡','⠬','⠠','⠤','⠨','⠌','⠴','⠂','⠆','⠒','⠲','⠢','⠖','⠶','⠦','⠔','⠱','⠰','⠣','⠿','⠜','⠹','⠈','⠁','⠃','⠉','⠙','⠑','⠋','⠛','⠓','⠊','⠚','⠅','⠇','⠍','⠝','⠕','⠏','⠟','⠗','⠎','⠞','⠥','⠧','⠺','⠭','⠽','⠵']

def affichagebaille(texte):
    texte=texte.upper()
    texteBraille=''
    for indice in range(0,len(texte)):
        if texte[indice]>=' 'and texte[indice]<='Z':
            texteBraille+=brailles[ord(texte[indice])-32]
    return texteBraille


texte=str(input("votre texte ?"))
print(affichagebaille(texte))
"""
"""
chaine="touchard"
print(chaine[:1],"*",chaine[1:2],"*",chaine[2:3],"*",chaine[3:4],"*",chaine[4:5],"*",chaine[5:6],"*",chaine[6:7],"*",chaine[7:])
"""
"""
def insertionTexte(texte):
    nouveauTexte=''
    for i in range( len(texte)-1):
        nouveauTexte+=texte[i]+"*"
    nouveauTexte+=texte[-1]
    return nouveauTexte
texte=str(input("votre texte ?"))
print(insertionTexte(texte))
"""
"""
chaine=str(input("la chaine est "))
total=""
for i in range(len(chaine)-1,-1,-1):
    total+=chaine[i]
print(total)
"""
"""
chaine=str(input("la chaine est "))
total=""
for i in range(len(chaine)-1,-1,-1):
    total+=chaine[i]
print(total)
if total==chaine:
    print("vrai")
else:
    print("faux")
"""
"""
def codecesar(phrase,cle):
    total=""
    for i in range(0,len(phrase)):
        ascii=ord(phrase[i])
        conv=ascii-65+cle
        caract=chr(conv+65)
        total+=caract+""
    return total
cle=int(input("clef : "))
phrase=str(input("phrase : "))
print(codecesar(phrase,cle))
"""
from string import ascii_uppercase as ascUp
vigenereTable = [ascUp[i:]+ascUp[:i] for i in range(len(ascUp))]
for ligne in range(0,len(vigenereTable)):
 print (ligne, vigenereTable[ligne])
