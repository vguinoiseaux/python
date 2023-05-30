"""
Programme animation balle
"""
import pygame

#constantes de la fenêtre d'affichage
LARGEUR=256       #hauteur de la fenêtre
HAUTEUR=256      #largeur de la fenêtre
ROUGE=(255,0,0)     # définition de 3 couleurs
VERT=(0,255,0)
BLEU=(0,0,255)

#Utilisation de la bibliothèque pygame
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Balle")             #titre de la fenêtre
font = pygame.font.Font('freesansbold.ttf', 20)     #choix de la police de caractères
frequence = pygame.time.Clock()                     #mode animation dans pygame

#variables de gestion de la balle
RAYONBALLE=10
balleX=LARGEUR//2
balleY=HAUTEUR//2          #position x y de la balle au milieu dans la fenêtre
vecteurBalleX=0            #vecteur de déplacement
vecteurBalleY=0


def afficheBalle():
    """
    affiche une balle aux coordonnées balleX,balleY avec un RAYON prédéfini
    """
    pygame.draw.circle(fenetre, ROUGE, (balleX,balleY), RAYONBALLE)

def deplacementBalle():
    """
    deplace la balle
    """
    global balleX,balleY        #permet de modifier les variables balleX,balleY
    balleX=balleX+vecteurBalleX #on deplace la balle selon l'axeX
    balleY=balleY+vecteurBalleY #on deplace la balle selon l'axeY

def testCollisionMurs():
    """
    test les collisions avec les murs en tenant compte du rayon
    """
    global balleX,balleY
    if balleX+RAYONBALLE>LARGEUR:
        balleX=LARGEUR-RAYONBALLE
    elif balleX-RAYONBALLE<0:
        balleX=RAYONBALLE
    elif balleY+RAYONBALLE>HAUTEUR:
        balleY=HAUTEUR-RAYONBALLE
    elif balleY-RAYONBALLE<0:
        balleY=RAYONBALLE

loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenêtre (croix rouge)
        if event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False

    keys = pygame.key.get_pressed()         #recupération des touches appuyées en continu
    if keys[pygame.K_UP]:    #est-ce la touche UP
        vecteurBalleY=-1
    elif keys[pygame.K_DOWN]:  #est-ce la touche DOWN
        vecteurBalleY=1
    elif keys[pygame.K_RIGHT]:  #est-ce la touche RIGHT
        vecteurBalleX=1
    elif keys[pygame.K_LEFT]:  #est-ce la touche LEFT
        vecteurBalleX=-1
    else:
        vecteurBalleY=0
        vecteurBalleX=0

    fenetre.fill((0,0,0))   #efface la fenêtre
    afficheBalle()
    deplacementBalle()
    testCollisionMurs()
    frequence.tick(60)
    pygame.display.update() #mets à jour la fenêtre graphique
pygame.quit()



