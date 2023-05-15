import pygame
from settings import *

class Editor:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        
    def run(self, dt):
        self.display_surface.fill('White')