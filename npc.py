import pygame
from pygame.math import Vector2 as vec

#Classe NPC

class NPC(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

        #physique et collision
      
        self.vx = 0
        self.walls = walls
        self.position = vec(x, y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.direction = "LEFT"
        
        #animation des npc
        self.frame_index = 0
        self.time_since_last_frame = 0
        self.frame_duration = 60

        # Donne sa position
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.position.y += self.vel.y
        self.rect.y = self.position.y
        # Vérifie s'il entre en collision avec walls
        self.collision_check()

# Sous-classe pour le NPC Maire
class Maire(NPC):
    def __init__(self, x, y):
        image_path = "img/NPCs/NPC_Maire1.png"
        super().__init__(x, y, image_path)

    def update(self):
        # Implémentez ici le comportement spécifique du Maire
        pass


# Sous-classe pour le NPC Forgeron
class Forgeron(NPC):
    def __init__(self, x, y):
        image_path = "img/NPCs/NPC_forgeron1.png"
        super().__init__(x, y, "img/NPCs/NPC_forgeron1.png")


# Sous-classe pour le NPC Tavernier
class Tavernier(NPC):
    def __init__(self, x, y):
        image_path = "img/NPCs/NPC_Tavernier1.png"
        super().__init__(x, y, "img/NPCs/NPC_Tavernier1.png")


# Sous-classe pour le NPC Explorer
class Explorer(NPC):
    def __init__(self, x, y):
        image_path = "img/NPCs/NPC_Explorer1.png"
        super().__init__(x, y, "img/NPCs/NPC_Explorer1.png")


