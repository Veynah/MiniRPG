import pygame
from pygame.math import Vector2 as vec

# Les variables pour bouger
# On ajoute de la friction pour que les mouvements soient plus agréables
ACC = 2
FRIC = -0.6

# Les variables de l'écran
HEIGHT = 720
WIDTH = 1280


class NewPlayer(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('img/player/Idle.png')
        self.image = self.get_image(0, 0)
        # Enlève la couleur noire du fond de l'image du joueur
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = vec(x, y)
        
    def update(self):
        self.rect.topleft = self.position
        
    def get_image(self, x, y):
        image = pygame.Surface([27, 47])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 27, 47))
        return image