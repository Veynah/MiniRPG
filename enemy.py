import pygame
from pygame.math import Vector2 as vec


ACC = 0.4

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, walls, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        print("Loaded Image:", self.image) # Debug print statement
        self.rect = self.image.get_rect()
        # Physique et collision et mouvement
        self.vx = 0
        self.walls = walls
        self.position = vec(x, y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.direction = "LEFT"
        self.running = False
        self.attacking = False
        # Animation
        self.attack_frame = 0
        self.frame_index = 0
        self.time_since_last_frame = 0
        self.frame_duration = 60
    
    # IA de monstre
    def update_enemy(self, player):
        print("Updating enemy")  # Debug print statement
        if self.see_player(player):
            self.chase_player(player)
            if self.close_to_player(player):
                self.attack_player()
        else:
            self.patrol()
            
        self.rect.topleft = self.position
    
    # Donne la distance à laquelle le monstre voit le joueur 
    def see_player(self, player):
        pass
    
    # Le monstre bouge vers le joueur
    def chase_player(self, player):
        if self.position.x < player.position.x:
            self.acc.x = ACC
        else:
            self.acc.x = -ACC
    
    # Donne la distance à laquelle le monstre peut attaquer le joueur
    def close_to_player(self, player):
        pass
    
    def attack_player(self):
        pass
    
    # Donne le comportement du monstre si le joueur n'est pas dans le coin
    def patrol(self):
        pass
        
        
            


class Skeleton1(Enemy):
    def __init__(self, x, y, walls):
        super().__init__(x, y, walls, "img/enemies/skeleton1/attack-A1.png")
