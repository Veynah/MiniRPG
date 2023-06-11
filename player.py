import pygame
from pygame.math import Vector2 as vec


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/player/test.png")
        self.rect = self.image.get_rect()
 
        # Position and direction
        self.vx = 0
        self.pos = vec((340, 240))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.direction = "RIGHT"

        # Time counter for animation
        self.time = 0

    def update(self):
      pass

    def move(self):
        pass

    def attack(self):
        pass

    def jump(self):
        pass



