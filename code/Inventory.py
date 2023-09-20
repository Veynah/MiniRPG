import pygame
from InventorySlot import InventorySlot


class Inventory:
    """
    Représente l'inventaire d'un joueur.

    Attributs :
        slots (list) : Liste des emplacements d'inventaire.
        image (pygame.Surface) : L'image de l'inventaire.
        rect (pygame.Rect) : Le rectangle de collision de l'inventaire.
        visible (bool) : Indique si l'inventaire est visible ou non.

    Méthodes :
        __init__(self) : Initialise l'objet Inventory.
        toggleVisibility(self) : Bascule la visibilité de l'inventaire.
        render(self, display) : Affiche l'inventaire à l'écran.
    """

    def __init__(self):
        """
        Initialise l'objet Inventory.
        """
        self.slots = []

        self.image = pygame.image.load("img/item/Inventory.png")
        self.rect = self.image.get_rect()
        self.rect.midtop = (700, 10)

        self.slots.append(InventorySlot("img/item/coinIcon.png", (410, 15)))
        self.slots.append(InventorySlot("img/item/manapotionIcon.png", (480, 15)))
        self.slots.append(InventorySlot("img/item/shield.ico", (550, 15)))
        self.slots.append(InventorySlot("img/item/weapon.png", (630, 5)))
        self.slots.append(InventorySlot("img/item/xp2.png", (700, 15)))
        self.slots.append(InventorySlot("img/item/money_bag.png", (770, 15)))

        self.visible = False

    def toggleVisibility(self):
        """
        Bascule la visibilité de l'inventaire.
        """
        self.visible = not self.visible

    def render(self, display):
        """
        Affiche l'inventaire à l'écran.

        Args:
            display (pygame.Surface) : La surface sur laquelle afficher l'inventaire.
        """
        if self.visible:  # Afficher uniquement si l'inventaire est visible
            display.blit(self.image, self.rect)
            for slot in self.slots:
                slot.render(display)
