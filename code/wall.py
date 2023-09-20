import pygame


class Wall(pygame.sprite.Sprite):
    """
    Classe représentant un mur dans un jeu Pygame.

    Les murs sont des objets immobiles qui bloquent les mouvements des autres objets du jeu.
    Ces murs sont utilisés pour créer les limites et les obstacles du jeu.

    Args:
        x (int): Position initiale en x du mur.
        y (int): Position initiale en y du mur.
        width (int): Largeur du mur.
        height (int): Hauteur du mur.
    """
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.right = x + width
        self.left = x
        self.top = y
        self.bottom = y + height
