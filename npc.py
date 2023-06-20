import pygame
from pygame.math import Vector2 as vec
ACC = 0.2
FRIC = -0.1


#Classe NPC dont vont etre les different npc

class NPC(pygame.sprite.Sprite):
    def __init__(self, x, y, walls, image_path):
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
    
    def update_NPC(self):
        self.acc = vec(0, 0.5)

        # Running = faux si on est trop slow
        if abs(self.vel.x) > 0.1:
            self.running = True
        else:
            self.running = False
        # Donne sa position
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.position.y += self.vel.y
        self.rect.y = self.position.y
        # Vérifie s'il entre en collision avec walls
        self.collision_check()  
        self.rect.topleft = self.position

    def collision_check(self):
        move_by = int(self.vel.x)
        for _ in range(abs(move_by)):
            # Increment or decrement x position by 1 pixel
            if move_by > 0:
                self.position.x += 1
            else:
                self.position.x -= 1
            # Update le rectangle
            self.rect.x = self.position.x
            # Check pour les collisions
            collisions = pygame.sprite.spritecollide(self, self.walls, False)
            if collisions:
                # Si je bouge vers la droite ajuste ma position à 1 pixel à gauche du mur
                if move_by > 0:
                    self.position.x = collisions[0].rect.left - self.rect.width - 3
                # Si je bouge vers la gauche ajuste ma position à 1 pixel à droite du mur
                elif move_by < 0:
                    self.position.x = collisions[0].rect.right + 3
                # Stop any horizontal movement
                self.vel.x = 0
                break

        collisions = pygame.sprite.spritecollide(self, self.walls, False)
        if collisions:
            # Détecet si le joueur bouge vers le bas
            if self.vel.y > 0:
                # Personnage bouge vers le bas
                for wall in collisions:
                    # Place le joueur sur le mur
                    self.position.y = wall.rect.top - self.rect.height
                    # Stoppe la chute verticale
                    self.vel.y = 0
            # Détecte si le personnage saute
            elif self.vel.y < 0:
                # Saut
                for wall in collisions:
                    # Place le joueur sous le mur
                    self.position.y = wall.rect.bottom
                    # Stop mouvement vers le haut
                    self.vel.y = 0

# Sous-classe pour le NPC Maire
class Maire(NPC):
    def __init__(self, x, y,walls):
        super().__init__(x, y, walls, "img/NPCs/NPC_Maire1.png")


# Sous-classe pour le NPC Forgeron
class Forgeron(NPC):
    def __init__(self, x, y,walls):

        super().__init__(x, y, walls,"img/NPCs/NPC_forgeron1.png")


# Sous-classe pour le NPC Tavernier
class Tavernier(NPC):
    def __init__(self, x, y, walls):
     
        super().__init__(x, y, walls,"img/NPCs/NPC_Tavernier1.png")


# Sous-classe pour le NPC Explorer
class Explorer(NPC):
    def __init__(self, x, y,walls):
       
        super().__init__(x, y, walls, "img/NPCs/NPC_Explorer1.png")


