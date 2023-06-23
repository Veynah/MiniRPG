import pygame
from pygame.math import Vector2 as vec

class FireBall(pygame.sprite.Sprite):
    def __init__(self, game, x, y, direction, damage):
        """
        La classe de boule de feu, mais celle-ci n'est pas fonctionnelle 

        Args:
            game (Game): L'instance principale du jeu.
            x (int): La coordonnée x de départ de la boule de feu.
            y (int): La coordonnée y de départ de la boule de feu.
            direction (str): La direction de la boule de feu ("LEFT" pour gauche, "RIGHT" pour droite).
            damage (int): Les dégâts infligés par la boule de feu.
        """
        super().__init__()

        # Chargement de l'animation de la boule de feu
        self.load_animation()

        # Variables de l'animation
        self.frame = 0
        self.image = self.fireball_animation[self.frame]
        self.mask = pygame.mask.from_surface(self.image)

        # Position et vitesse de la boule de feu
        self.position = vec(x, y)
        self.vel = vec(8, 0)
        if direction == "LEFT":
            self.vel.x *= -1
            self.image = pygame.transform.flip(self.fireball_animation[self.frame], True, False)
        self.direction = direction

        # Dégâts de la boule de feu
        self.damage = 4

        # Rectangle de collision de la boule de feu
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        # Référence au jeu principal
        self.game = game

        # Variables de distance parcourue
        self.distance_travelled = 0
        self.max_distance = 500

    def update(self):
        """
        Met à jour la boule de feu à chaque frame du jeu.
        """
        self.position += self.vel
        self.rect.topleft = self.position
        print(self.position)

        # Vérification des collisions avec les ennemis
        collisions = pygame.sprite.spritecollide(self, self.game.enemies_group, False)
        for enemy in collisions:
            enemy.health -= self.damage
            self.kill()

        # Mise à jour de l'image de la boule de feu
        if self.frame < len(self.fireball_animation) - 1:
            self.frame += 1
            self.image = self.fireball_animation[self.frame]
            self.mask = pygame.mask.from_surface(self.image)

        # Mise à jour de la distance parcourue
        self.distance_travelled += self.vel.length()
        if self.distance_travelled > self.max_distance:
            self.kill()

    def load_animation(self):
        """
        Charge les images de l'animation de la boule de feu.
        """
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
