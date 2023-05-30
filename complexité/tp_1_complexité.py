from PIL import Image
import time

img=Image.open("image/phare2.jpg")
largeur,hauteur=img.size
debut = time.time()
for y in range(hauteur):
    for x in range(largeur):
        r,v,b=img.getpixel((x,y))
        moyenne=(r+v+b)//3
        r = moyenne
        v = moyenne
        b = moyenne
        img.putpixel((x,y),(r,v,b))
fin = time.time()
print("taille img \t durée de traitement")
print(largeur*hauteur,"\t",fin-debut)
img.show()