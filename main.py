import pygame

pygame.init()
#On va faire notre interface de jeu
screen = pygame.display.set_mode((800,400))

while True:#dans cette boucle on va update le jeu
    for event in pygame.event.get(): #une boucle qui va check pour n'importe quel input des joueurs
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
    