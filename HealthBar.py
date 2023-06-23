import pygame
from pygame.math import Vector2 as vec


class HealthBar(pygame.sprite.Sprite):
    """
    Représente une barre de santé pour un personnage de jeu.

    Attributs :
        game (Game) : L'instance du jeu.
        max_health (int) : La valeur maximale de santé.
        health (int) : La valeur actuelle de santé.
        image (pygame.Surface) : L'image actuelle de la barre de santé.
        pos (vec) : La position de la barre de santé.

    Méthodes :
        __init__(self, game, x, y) : Initialise l'objet HealthBar.
        render(self, screen) : Affiche la barre de santé à l'écran.
        takeDamage(self, damage) : Diminue la santé selon le montant de dégâts donné.
        heal(self, heal) : Augmente la santé selon le montant de guérison donné.
        load_animations(self) : Charge les images d'animation de la barre de santé.
    """

    def __init__(self, game, x, y):
        """
        Initialise l'objet HealthBar.

        Args:
            game (Game) : L'instance du jeu.
            x (int) : La coordonnée x de la position de la barre de santé.
            y (int) : La coordonnée y de la position de la barre de santé.
        """
        super().__init__()
        self.game = game
        self.load_animations()

        self.max_health = 5
        self.health = self.max_health
        self.image = self.health_animations[self.health]
        self.pos = vec(x, y)

    def render(self, screen):
        """
        Affiche la barre de santé à l'écran.

        Args:
            screen (pygame.Surface) : La surface sur laquelle afficher la barre de santé.
        """
        screen.blit(self.image, self.pos)

    def takeDamage(self, damage):
        """
        Diminue la santé selon le montant de dégâts donné.

        Args:
            damage (int) : Le montant de dégâts à soustraire de la santé.
        """
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.game.player_death()

        self.image = self.health_animations[self.health]

    def heal(self, heal):
        """
        Augmente la santé selon le montant de guérison donné.

        Args:
            heal (int) : Le montant de santé à ajouter.
        """
        self.health += heal
        if self.health > self.max_health:
            self.health = self.max_health

        self.image = self.health_animations[self.health]

    def load_animations(self):
        """
        Charge les images d'animation de la barre de santé.
        """
        self.health_animations = [
            pygame.image.load("img/item/hearts0.png").convert_alpha(),
            pygame.image.load("img/item/hearts1.png").convert_alpha(),
            pygame.image.load("img/item/hearts2.png").convert_alpha(),
            pygame.image.load("img/item/hearts3.png").convert_alpha(),
            pygame.image.load("img/item/hearts4.png").convert_alpha(),
            pygame.image.load("img/item/hearts5.png").convert_alpha(),
        ]
