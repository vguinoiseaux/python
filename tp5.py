# Créé par VALENTIN.GUINOISEAUX, le 15/11/2022 en Python 3.7
"""
from PIL import Image,ImageDraw,ImageFont
img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
draw=ImageDraw.Draw(img)

def traceDroite(nbDroites,ecart):
    a=0
    for i in range (1,nbDroites+1):
        draw.line((a,0,a,255),fill=(0,255,0))
        a+=20
traceDroite(10,20)

img.show()
"""
"""
from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
draw=ImageDraw.Draw(img)

def cercle(x,y,rayon,couleur):
    draw.ellipse((x-rayon,y-rayon,x+rayon, y+rayon),fill=couleur)

def tracecible(nbcercle):

        cercle(128,128,60,(0,0,255))
        cercle(128,128,40,(255,0,0))
        cercle(128,128,20,(255,255,0))

tracecible(3)
img.show()
"""
"""
from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(255,255,255))
largeur,hauteur=img.size
draw=ImageDraw.Draw(img)

def rectangle(x,y,largeur,hauteur,couleur):
    draw.rectangle((x,y,x+largeur, y+hauteur),fill=couleur)


    rectangle((10,10,50,50(0,0,0))



img.show()
"""
"""
from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
for y in range(hauteur):
    for x in range(largeur):
         img.putpixel((x,y),(0,0+x,0))
img.show()
img.save("degrade_vert.jpg")
"""
"""
from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
for y in range(hauteur):
    for x in range(largeur):
         img.putpixel((x,y),(0+x,0+y,0+x))

img.show()
img.save("degrade_bicolor.jpg")
"""
"""
from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(1536,256),(0,0,0))
largeur,hauteur=img.size


for y in range(hauteur):
    for x in range(largeur):
         img.putpixel((x,y),(0+x,0+x,0+x))




img.show()
img.save("degradex6.jpg")
"""

from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size

title=[]
for n in range(0,12):
    print('image/00.png'.format(n))
    title.append(Image.open('image/00.png'.format(n)))
    title.append(Image.open('image/01.png'.format(n)))
    title.append(Image.open('image/02.png'.format(n)))
    title.append(Image.open('image/03.png'.format(n)))
    title.append(Image.open('image/04.png'.format(n)))
    title.append(Image.open('image/05.png'.format(n)))
    title.append(Image.open('image/06.png'.format(n)))
    title.append(Image.open('image/07.png'.format(n)))
    title.append(Image.open('image/08.png'.format(n)))
    title.append(Image.open('image/09.png'.format(n)))
    title.append(Image.open('image/10.png'.format(n)))

map=[[0,0,0,0,0,0,0,0],
     [0,1,5,2,1,5,2,0],
     [0,6,0,7,9,0,6,0],
     [0,3,10,4,3,10,4,0],
     [0,0,6,0,0,6,0,0],
     [0,0,6,0,0,6,0,0],
     [0,0,3,5,5,4,0,0],
     [0,0,0,0,0,0,0,0]]

for ligne in range(0,8):
    for colonne in range(0,8):
        numero=map[ligne][colonne]
        print(map[ligne][colonne],end=' ')
        img.paste(title[numero], (colonne*32,ligne*32))
    print()


img.show()
img.save("map.png")
"""
from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size

title=[]
for n in range(0,12):
    print('image/00.png'.format(n))
    title.append(Image.open('image/00.png'.format(n)))
    title.append(Image.open('image/01.png'.format(n)))
    title.append(Image.open('image/02.png'.format(n)))
    title.append(Image.open('image/03.png'.format(n)))
    title.append(Image.open('image/04.png'.format(n)))
    title.append(Image.open('image/05.png'.format(n)))
    title.append(Image.open('image/06.png'.format(n)))
    title.append(Image.open('image/07.png'.format(n)))
    title.append(Image.open('image/08.png'.format(n)))
    title.append(Image.open('image/09.png'.format(n)))
    title.append(Image.open('image/10.png'.format(n)))


map=[[1,5,5,5,10,5,5,2],
     [6,0,0,0,6,0,0,6],
     [6,0,0,0,6,0,0,6],
     [6,0,0,0,6,0,0,6],
     [6,0,0,0,6,0,0,6],
     [6,0,0,0,6,0,0,6],
     [6,0,0,0,6,0,0,6],
     [3,5,5,5,8,5,5,4]]

for ligne in range(0,8):
    for colonne in range(0,8):
        numero=map[ligne][colonne]
        print(map[ligne][colonne],end=' ')
        img.paste(title[numero], (colonne*32,ligne*32))
    print()


img.show()
img.save("map.png")
"""