import pygame


vec = pygame.math.Vector2


class Item(pygame.sprite.Sprite):
    """
    Représente un objet dans le jeu.

    Attributs :
        ID (int) : L'identifiant de l'objet.
        image (pygame.Surface) : L'image de l'objet.
        rect (pygame.Rect) : Le rectangle de collision de l'objet.
        pos (vec) : La position de l'objet.

    Méthodes :
        __init__(self, x, y, itemtype, name) : Initialise l'objet Item.
        update(self, player) : Met à jour l'objet en fonction de l'interaction avec le joueur.
        render(self, display) : Affiche l'objet à l'écran.
    """

    def __init__(self, x, y, itemtype, name):
        """
        Initialise l'objet Item.

        Args:
            x (int) : La coordonnée x de la position de l'objet.
            y (int) : La coordonnée y de la position de l'objet.
            itemtype (int) : Le type d'objet (ID).
            name (str) : Le nom du fichier d'image de l'objet.
        """
        super().__init__()

        self.ID = itemtype
        self.image = pygame.image.load(name).convert_alpha()
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.rect.topleft = self.pos

    def update(self, player):
        """
        Met à jour l'objet en fonction de l'interaction avec le joueur.

        Args:
            player (Player) : Le joueur avec lequel l'objet interagit.
        """
        hits = self.rect.colliderect(player.rect)

        if hits:
            if self.ID == 0:
                pass
            elif self.ID == 1:
                player.healthBar.Heal(1)

            self.kill()

    def render(self, display):
        """
        Affiche l'objet à l'écran.

        Args:
            display (pygame.Surface) : La surface sur laquelle afficher l'objet.
        """
        display.blit(self.image, self.pos)


# ID -> 0 -> Pièce
# ID -> 1 -> Santé
