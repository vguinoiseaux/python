"""
Programme du tron
nom(s), prénom(s), classe(s)
"""
import pygame
from random import *

#constantes de la fenêtre d'affichage
LARGEUR=1200      #hauteur de la fenêtre
HAUTEUR=600      #largeur de la fenêtre
ROUGE=(255,0,0)     # définition de 3 couleurs
VERT=(0,255,0)
BLEU=(0,0,255)
NOIR=(0,0,0)
JAUNE=(255,255,0)

#Utilisation de la bibliothèque pygame
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Tron")             #titre de la fenêtre
font = pygame.font.Font('freesansbold.ttf', 20)     #choix de la police de caractères
frequence = pygame.time.Clock()                  #mode animation dans pygame





moto1X=LARGEUR//4*3-200
moto1Y=HAUTEUR//2
moto1_direction = 'haut'

moto2X=LARGEUR//4-200
moto2Y=HAUTEUR//2
moto2_direction = 'haut'

tempsPartie=0

def dessineDecor():
    """
    dessine un decor
    """
    pygame.draw.rect(fenetre, ROUGE, [1, 1, LARGEUR-1-200, HAUTEUR-1],1)
    for i in range(0,30):
        pygame.draw.circle(fenetre, ROUGE, (randint(0,LARGEUR-250),randint(0,HAUTEUR)), 50)      #cercle plein aux coord x,y de rayon 10
        pygame.draw.rect(fenetre, BLEU, [randint(0,LARGEUR-250),randint(0,HAUTEUR), 50, 50],0)   #rectangle plein aux coord x,y
    pygame.draw.rect(fenetre, NOIR , [ LARGEUR//4-300, HAUTEUR//2-100, 200, 200],0)
    pygame.draw.rect(fenetre, NOIR , [ LARGEUR//4*3-300, HAUTEUR//2-100, 200, 200],0)


def afficheTexte():
    """
    affiche un texte aux coordonnées x,y
    """
    texteAfficher = font.render(str(tempsPartie), True, ROUGE)
    fenetre.blit(texteAfficher,(LARGEUR-100,HAUTEUR//2))

def collisionMur(x,y):
    """
    verifie si on touche un mur ou autre chose
    aucun obstacle correspond à une couleur noire
    """
    color=fenetre.get_at((x, y))[:3]
    somme=color[0]+color[1]+color[2]
    if somme==0:
        collision=False
    else:
        collision=True
    return collision


def deplacementmoto1():
    """
    Déplace la moto 1 si c'est possible
    """
    global moto1X, moto1Y
    touche = False
    if moto1_direction == 'haut':
        x = moto1X
        y = moto1Y - 1
        touche = collisionMur(x, y)
    elif moto1_direction == 'bas':
        x = moto1X
        y = moto1Y + 1
        touche = collisionMur(x, y)
    elif moto1_direction == 'droite':
        x = moto1X + 1
        y = moto1Y
        touche = collisionMur(x, y)
    elif moto1_direction == 'gauche':
        x = moto1X - 1
        y = moto1Y
        touche = collisionMur(x, y)

    if touche==False:       #si pas d'obstacle alors on trace le point de la moto
        moto1X=x
        moto1Y=y
    fenetre.set_at((x, y), VERT)
    return touche           #retourne la variable booleenne touche pour savoir si la partie est terminée

def deplacementmoto2():
    """
    Déplace la moto 2 si c'est possible
    """
    global moto2X, moto2Y
    touche = False
    if moto2_direction == 'haut':
        x = moto2X
        y = moto2Y - 1
        touche = collisionMur(x, y)
    elif moto2_direction == 'bas':
        x = moto2X
        y = moto2Y + 1
        touche = collisionMur(x, y)
    elif moto2_direction == 'droite':
        x = moto2X + 1
        y = moto2Y
        touche = collisionMur(x, y)
    elif moto2_direction == 'gauche':
        x = moto2X - 1
        y = moto2Y
        touche = collisionMur(x, y)

    if touche==False:       #si pas d'obstacle alors on trace le point de la moto
        moto2X=x
        moto2Y=y
    fenetre.set_at((x, y), JAUNE)
    return touche


loop=True
dessineDecor()
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()            #fermeture de la fenêtre (croix rouge)
        if event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            if event.key == pygame.K_ESCAPE or event.unicode == 'a': #touche q pour quitter
                loop = False
            #fenetre.set_at((200, 200), color)

    keys = pygame.key.get_pressed()         #recupération des touches appuyées en continu
    if keys[pygame.K_UP]:
        moto1_direction = 'haut'
    elif keys[pygame.K_DOWN]:
        moto1_direction = 'bas'
    elif keys[pygame.K_RIGHT]:
        moto1_direction = 'droite'
    elif keys[pygame.K_LEFT]:
        moto1_direction = 'gauche'
    elif keys[pygame.K_w]:
        moto2_direction = 'haut'
    elif keys[pygame.K_s]:
        moto2_direction = 'bas'
    elif keys[pygame.K_d]:
        moto2_direction = 'droite'
    elif keys[pygame.K_a]:
            moto2_direction = 'gauche'


    #fenetre.fill((0,0,0))   #efface la fenêtre, non utilisé ici

    if deplacementmoto1()==True:
        loop=False
    if deplacementmoto2()==True:
        loop=False
    frequence.tick(60)
    afficheTexte()
    pygame.display.update() #mets à jour la fenêtre graphique
    tempsPartie+=1
    pygame.draw.rect(fenetre, NOIR , [ LARGEUR-200, 0, 200, HAUTEUR],0)

pygame.quit()
print('perdu')
print('temps partie',tempsPartie)