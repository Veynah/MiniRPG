import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.set_alpha(0) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.right = x + width
        self.left = x
        self.top = y
        self.bottom = y + height