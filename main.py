import pygame
from sys import exit #importe le module exit de sys pour pouvoir fermer le programme sans créer d'erreur

pygame.init()
#On va faire notre interface de jeu
screen = pygame.display.set_mode((800,400))

while True:#dans cette boucle on va update le jeu
    for event in pygame.event.get(): #une boucle qui va check pour n'importe quel input des joueurs
        if event.type == pygame.QUIT:
            pygame.quit() #pygame.quit est l'opposé de pygame.init
            exit()
    pygame.display.update()
    