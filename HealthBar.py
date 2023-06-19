import pygame


vec = pygame.math.Vector2


class HealthBar(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.load_animations()

        self.health = 5
        self.image = self.health_animations[self.health]
        self.pos = vec(x, y)

    def render(self, display):
        display.blit(self.image, self.pos)

    def takeDamage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

        self.image = self.health_animations[self.health]

    def Heal(self, heal):
        self.health += heal
        if self.health > 5:
            self.health = 5

        self.image = self.health_animations[self.health]

    def load_animations(self):
        self.health_animations = [
            pygame.image.load("img/item/heart0.png").convert_alpha(),
            pygame.image.load("img/item/heart1.png").convert_alpha(),
            pygame.image.load("img/item/heart2.png").convert_alpha(),
            pygame.image.load("img/item/heart3.png").convert_alpha(),
            pygame.image.load("img/item/heart4.png").convert_alpha(),
            pygame.image.load("img/item/heart5.png").convert_alpha(),
        ]
