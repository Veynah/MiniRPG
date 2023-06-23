import pygame
from pygame.math import Vector2 as vec


class FireBall(pygame.sprite.Sprite):
    def __init__(self, game, x, y, direction, damage):
        super().__init__()
        self.load_animation()
        self.frame = 0
        self.image = self.fireball_animation[self.frame]
        self.mask = pygame.mask.from_surface(self.image)
        self.position = vec(x, y)
        self.vel = vec(8, 0)
        if direction == "LEFT":
            self.vel.x *= -1
            self.image = pygame.transform.flip(self.fireball_animation[self.frame], True, False)
        self.direction = direction
        self.damage = 4
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.game = game
        
        self.distance_travelled = 0
        self.max_distance = 500
        
    def update(self):
        self.position += self.vel
        self.rect.topleft = self.position
        print(self.position)
        if self.frame < len(self.fireball_animation) - 1:
            self.frame += 1
        
        collisions = pygame.sprite.spritecollide(self, self.game.enemies_group, False)
        for enemy in collisions:
            enemy.health -= self.damage
            self.kill()
        
        self.image = self.fireball_animation[self.frame]
        self.mask = pygame.mask.from_surface(self.image)
        self.distance_travelled += self.vel.length()
        if self.distance_travelled > self.max_distance:
            self.kill()
        
    def load_animation(self):
        self.fireball_animation = [
            pygame.image.load("img/magic/fireball0.png"),
            pygame.image.load("img/magic/fireball0.png"),
            pygame.image.load("img/magic/fireball1.png"),
            pygame.image.load("img/magic/fireball1.png"),
            pygame.image.load("img/magic/fireball2.png"),
            pygame.image.load("img/magic/fireball2.png"),
            pygame.image.load("img/magic/fireball3.png"),
            pygame.image.load("img/magic/fireball3.png"),
            pygame.image.load("img/magic/fireball3.png"),
        ]