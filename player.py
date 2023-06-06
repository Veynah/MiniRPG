import pygame
from pygame import Vector2 as vec
import time

class Player(pygame.sprite.Sprite):
    def __init__(self, name, image_path, pos_x, pos_y):
        super().__init__()
        self.name = name
        self.image = pygame.image.load("img/player/test.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.speed = pygame.Vector2(5, 5)
        self.health = 100
        self.defense = 5
        self.attack_power = 10
        self.level = 1
        self.experience = 0
        
        self.vx = 0
        self.pos = vec((340, 240))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.direction = "RIGHT"

        
        self.direction = 'right'  # default direction of the player
        self.last_dash_time = 0  
        self.dash_cooldown = 5
        self.dash_distance = 50
        
    def dash(self): # dash in the direction you're facing / Didn't add collisions detection
        current_time = time.time()
        if current_time - self.last_dash_time >= self.dash_cooldown:
            if self.direction == 'right':
                self.rect.x += self.dash_distance
            elif self.direction == 'left':
                self.rect.x -= self.dash_distance
            
            self.last_dash_time = current_time
        
    def move_left(self):
        self.speed = pygame.Vector2(-5, self.speed.y)

    def move_right(self):
        self.speed = pygame.Vector2(5, self.speed.y)

    def stop_moving(self):
        self.speed = pygame.Vector2(0, self.speed.y)

    def update(self):   # Update the player's position
        self.rect.move_ip(self.speed.x, self.speed.y) 

    def render(self, screen):
        screen.blit(self.image, self.rect)   

    def sword_attack(self, enemy):
        damage = self.attack_power
        enemy.take_physical_damage(damage)

    def magic_bolt(self, enemy):
        if self.mana >= 20:
            damage = self.attack_power * 1.5
            enemy.take_magic_damage(damage)
            self.mana -= 20
        else:
            print("Not enough mana to cast the spell.")

    def take_damage(self, damage):
        # chaque point de défense de 0.5% les dégats reçu
        reduction = self.defense / 200
        net_damage = damage * (1 - reduction)
        self.health -= net_damage

        if self.health <= 0:
            return True
        return False

 
    def gain_experience(self, experience):
        self.experience += experience
        if self.experience >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.health += 20
        self.attack_power += 5
        self.mana += 10
        self.defense += 2
        self.experience = 0
        self.physical_armor += 5
        self.magic_armor += 5

