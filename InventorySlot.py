import pygame


class InventorySlot:
    """
    Représente un emplacement dans l'inventaire.

    Attributs :
        image (pygame.Surface) : L'image de l'emplacement.
        rect (pygame.Rect) : Le rectangle de collision de l'emplacement.
        count (int) : Le nombre d'éléments dans l'emplacement.
        font (pygame.font.Font) : La police d'écriture pour afficher le nombre d'éléments.

    Méthodes :
        __init__(self, name, pos) : Initialise l'objet InventorySlot.
        render(self, display) : Affiche l'emplacement de l'inventaire à l'écran.
    """

    def __init__(self, name, pos):
        """
        Initialise l'objet InventorySlot.

        Args:
            name (str) : Le nom du fichier d'image de l'emplacement.
            pos (tuple) : La position (x, y) de l'emplacement.
        """
        self.image = pygame.image.load(name)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.count = 0

        self.font = pygame.font.Font("img/Fonts/Frostbite.ttf", 25)

    def render(self, display):
        """
        Affiche l'emplacement de l'inventaire à l'écran.

        Args:
            display (pygame.Surface) : La surface sur laquelle afficher l'emplacement.
        """
        text = self.font.render(str(self.count), True, (0, 0, 0))
        display.blit(self.image, self.rect)
        display.blit(text, self.rect.midright)
