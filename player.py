import pygame
from pygame.locals import K_q, K_d
from pygame.math import Vector2 as vec
import keyboard
import time


# Les variables pour bouger
# On ajoute de la friction pour que les mouvements soient plus agréables
ACC = 0.3
FRIC = -0.10

# Les variables de l'écran
HEIGHT = 720
WIDTH = 1280


class Player(pygame.sprite.Sprite):
      def __init__(self, blockers):
            super().__init__()
            self.image = pygame.image.load("img/player/test.png")
            self.rect = self.image.get_rect()

            # Position and direction
            self.vx = 0
            self.pos = vec((340, 240))
            self.vel = vec(0, 0)
            self.acc = vec(0, 0)
            self.direction = "RIGHT"
            self.jumping = False
            self.blockers = blockers

            # Time counter for animation
            self.time = 0

      def move(self):
        # Constante qui va accélérer vers le bas ce qui va simuler la gravité
            self.acc = vec(0,0.5)


            # Cela va renvoyer les touches pressées 
            pressed_keys = pygame.key.get_pressed()

            # Accélère dans une direction ou une autre suivant la touche utilisée
            if pressed_keys[K_q]:  # Q pour aller à gauche
                  self.acc.x = -ACC
            if pressed_keys[K_d]:  # D pour aller à droite
                  self.acc.x = ACC

        # Détermine la vélocité en prenant en compte la friciton
            self.acc.x += self.vel.x * FRIC
            self.vel += self.acc
            self.pos += self.vel + 0.5 * self.acc  # Update la position

        # Ce sera le blink
            if self.pos.x > WIDTH:
                  self.pos.x = 0
            if self.pos.x < 0:
                  self.pos.x = WIDTH

            self.rect.midbottom = self.pos  # Update rect with new pos
            
            self.pos.x += self.vel.x
            for blocker in self.blockers:
                  if self.rect.colliderect(blocker):
                        self.pos.x -= self.vel.x
                        self.vel.x = 0

            
            self.pos.y += self.vel.y
            for blocker in self.blockers:
                  if self.rect.colliderect(blocker):
                        self.pos.y -= self.vel.y
                        self.vel.y = 0

      def update(self):
            pass

      def attack(self):
            pass

      def jump(self):
            pass

