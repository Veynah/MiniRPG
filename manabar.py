import pygame
from pygame.math import Vector2 as vec

class ManaBar(pygame.sprite.Sprite):
    REGEN_EVENT = pygame.USEREVENT + 1
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.load_animations()
        
        self.max_mana = 5
        self.mana = self.max_mana
        self.image = self.mana_animations[self.mana]
        self.pos = vec(x, y)
        
        # REGEN_EVENT va nous rendre de la mana toutes les x secondes
        pygame.time.set_timer(self.REGEN_EVENT, 5000)
        
    def render(self, screen):
        screen.blit(self.image, self.pos)
        
    def manaCost(self, manacost):
        if self.mana > 0 and self.mana >= manacost:
            self.mana -= manacost
            print(self.mana)
            self.image = self.mana_animations[self.mana]
            return True
        else:
            print("You have no Mana")
            return False
        
    def regen(self):
        if self.mana < self.max_mana:
            self.mana += 1
            self.image = self.mana_animations[self.mana]
        
    def load_animations(self):
        self.mana_animations = [
            pygame.image.load("img/item/mana0.png").convert_alpha(),
            pygame.image.load("img/item/mana1.png").convert_alpha(),
            pygame.image.load("img/item/mana2.png").convert_alpha(),
            pygame.image.load("img/item/mana3.png").convert_alpha(),
            pygame.image.load("img/item/mana4.png").convert_alpha(),
            pygame.image.load("img/item/mana5.png").convert_alpha(),
        ]
        
    def update(self, event):
        if event.type == self.REGEN_EVENT:
            self.regen()