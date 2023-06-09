import pygame
from pygame.locals import *

class Background(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.bgimage = pygame.image.load("Background.png")        
            self.bgY = 0
            self.bgX = 0
 
      def render(self):
            screen.blit(self.bgimage, (self.bgX, self.bgY))