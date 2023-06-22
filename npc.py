import pygame
from Inventory import Inventory
from InventorySlot import InventorySlot 
from pygame.math import Vector2 as vec
ACC = 0.05
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
        
    def update_NPC(self):
        self.acc = vec(0, 0.5)
        # Donne sa position
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc

        self.position.x += self.vel.x
        self.position.y += self.vel.y
        self.rect.y = self.position.y
        self.rect.x = self.position.x
        # Vérifie s'il entre en collision avec walls
        self.collision_check()  
        
        self.rect.topleft = self.position
        # Pour debug
        #print(self.position)
        #print(self.acc)
        #print(self.vel)
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
    def __init__(self, x, y,walls, inventory):
        super().__init__(x, y, walls, "img/NPCs/NPC_Maire1.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.walls = walls
        self.inventory = inventory
        coin_slot = next(
            (slot for slot in inventory.slots if slot.image == pygame.image.load("img/item/money_bag.png")),
            None
        )
        if coin_slot:
            coin_slot.count = 30000  # Initialize with 30000 coins

    def update_NPC(self):
        # NPC logic goes here
        pass

    def add_coins(self, coins):
        coin_slot = next(
            (slot for slot in self.slots if slot.image == pygame.image.load("img/item/money_bag.png", (770, 15))),
             None
        )
        if coin_slot:
            coin_slot.count += coins


    def give_coins_to_player(self, player_inventory, amount):
        coin_slot = next(
            (slot for slot in self.inventory.slots if slot.image == pygame.image.load("img/item/coinIcon.png")),
            None
        )
        if coin_slot:
            if coin_slot.count >= amount:
                coin_slot.count -= amount
                player_inventory.add_coins(amount)
            else:
                print("Maire does not have enough coins in the inventory.")
        else:
            print("Maire does not have coins in the inventory.")


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


