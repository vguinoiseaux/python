"""
Programme de scrolling texte
"""
import pygame

#constantes de la fenêtre d'affichage
LARGEUR=1300       #hauteur de la fenêtre
HAUTEUR=256      #largeur de la fenêtre
ROUGE=(255,0,0)     # définition de 3 couleurs
VERT=(0,255,0)
BLEU=(0,0,255)

#Utilisation de la bibliothèque pygame
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Scrolling")             #titre de la fenêtre
font = pygame.font.Font('freesansbold.ttf', 20)     #choix de la police de caractères
frequence = pygame.time.Clock()                     #mode animation dans pygame

texteX=LARGEUR//2
texteY=150
sensY=5

def afficheTexte(x,y,txt):
    """
    affiche un texte aux coordonnées x,y
    """
    texteAfficher = font.render(str(txt), True, VERT)
    fenetre.blit(texteAfficher,(x,y))

def defilementTexte():
    global texteX,texteY,sensY
    texteX=texteX-1
    if texteX<-200:
        texteX=LARGEUR



loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenêtre (croix rouge)
        if event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False


    fenetre.fill((0,0,0))   #efface la fenêtre
    afficheTexte(texteX,texteY,'Lycée Gabriel Touchard')
    defilementTexte()
    frequence.tick(0)
    pygame.display.update() #mets à jour la fenêtre graphique
pygame.quit()


