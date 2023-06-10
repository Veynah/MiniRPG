import pygame
from pygame.math import Vector2 as vec
from spritesheet import SpriteSheet

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        sprite_sheet_image = pygame.image.load("img/player/Idle.png").convert_alpha()
        self.sprite_sheet = SpriteSheet(sprite_sheet_image)
        
        # Extract frames from the sprite sheet
        self.images = [self.sprite_sheet.get_image(i, 64, 16, 1, (0, 0, 0)) for i in range(8)]
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        # Position and direction
        self.vx = 0
        self.pos = vec((150, 150))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.direction = "RIGHT"

    def move(self):
        pass
    
    def update(self):
        pass
    
    def attack(self):
        pass
    
    def jump(self):
        pass
