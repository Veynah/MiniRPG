import pygame
from pygame.locals import K_q, K_d
from pygame.math import Vector2 as vec
import keyboard
import time


# Les variables pour bouger
ACC = 0.3
FRIC = -0.10

# Les variables de l'écran
HEIGHT = 720
WIDTH = 1280


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/player/test.png")
        self.rect = self.image.get_rect()

        # Position and direction
        self.vx = 0
        self.pos = vec((340, 240))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.direction = "RIGHT"

        # Time counter for animation
        self.time = 0

    def move(self):
        # Keep a constant acceleration of 0.5 in the downwards direction (gravity)
        # self.acc = vec(0,0.5)

        # Will set running to False if the player has slowed down to a certain extent
        if abs(self.vel.x) > 0.3:
            self.running = True
        else:
            self.running = False

        # Returns the current key presses
        pressed_keys = pygame.key.get_pressed()

        # Accelerates the player in the direction of the key press
        if pressed_keys[K_q]:  # 'q' for going left
            self.acc.x = -ACC
        if pressed_keys[K_d]:  # 'd' for going right
            self.acc.x = ACC

        # Formulas to calculate velocity while accounting for friction
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc  # Updates Position with new values

        # This causes character warping from one point of the screen to the other
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos  # Update rect with new pos

    def update(self):
        pass

    def attack(self):
        pass

    def jump(self):
        pass

