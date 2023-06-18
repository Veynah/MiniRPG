import pygame
from InventorySlot import InventorySlot

class Inventory:
    def __init__(self):
        self.slots = []

        self.image = pygame.image.load("img/Inventory.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 350)

        self.slots.append(InventorySlot("img/coinIcon.png", (10, 360)))
        self.slots.append(InventorySlot("img/manapotionIcon.png", (110, 360)))
        
        self.visible = False 

    def toggleVisibility(self):
        self.visible = not self.visible
        
    def render(self, display):
        if self.visible:  # Only render if the inventory is visible
            display.blit(self.image, self.rect)
            for slot in self.slots:
                slot.render(display)

        
