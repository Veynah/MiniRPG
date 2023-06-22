import sys
import pygame

vec = pygame.math.Vector2


class HealthBar(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.load_animations()

        self.max_health = 5
        self.health = self.max_health
        self.image = self.health_animations[self.health]
        self.pos = vec(x, y)

    def render(self, display):
        display.blit(self.image, self.pos)

    def takeDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.game.player_death()

        self.image = self.health_animations[self.health]

    def Heal(self, heal):
        self.health += heal
        if self.health > self.max_health:
            self.health = self.max_health

        self.image = self.health_animations[self.health]

    def load_animations(self):
        self.health_animations = [
            pygame.image.load("img/item/hearts0.png").convert_alpha(),
            pygame.image.load("img/item/hearts1.png").convert_alpha(),
            pygame.image.load("img/item/hearts2.png").convert_alpha(),
            pygame.image.load("img/item/hearts3.png").convert_alpha(),
            pygame.image.load("img/item/hearts4.png").convert_alpha(),
            pygame.image.load("img/item/hearts5.png").convert_alpha(),
        ]
