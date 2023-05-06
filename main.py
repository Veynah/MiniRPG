import pygame
from pygame.locals import *
from sys import exit #importe le module exit de sys pour pouvoir fermer le programme sans créer d'erreur

pygame.init()
#On va faire notre interface de jeu
screen = pygame.display.set_mode((1920,1080))
pygame.display.set_caption('MiniRPG') #Titre du jeu
clock = pygame.time.Clock() #clock pour limiter le framerate

while True:#dans cette boucle on va update le jeu
    for event in pygame.event.get(): #une boucle qui va check pour n'importe quel input des joueurs
        if event.type == pygame.QUIT:
            pygame.quit() #pygame.quit est l'opposé de pygame.init
            exit()
    pygame.display.update()
    clock.tick(60) #max fps 60
    