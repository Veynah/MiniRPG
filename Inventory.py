import pygame
from InventorySlot import InventorySlot

class Inventory:
    def __init__(self):
        self.slots = []

        self.image = pygame.image.load("img/Inventory.png")
        self.rect = self.image.get_rect()
        self.rect.midtop = (700, 10)

        self.slots.append(InventorySlot("img/coinIcon.png", (410, 15)))
        self.slots.append(InventorySlot("img/manapotionIcon.png", (480, 15)))
        self.slots.append(InventorySlot("img/shield.ico", (550, 15)))
        self.slots.append(InventorySlot("img/weapon.png", (630, 5)))
        self.slots.append(InventorySlot("img/xp2.png", (700, 15)))
        
        self.visible = False 

    def toggleVisibility(self):
        self.visible = not self.visible
        
    def render(self, display):
        if self.visible:  # Only render if the inventory is visible
            display.blit(self.image, self.rect)
            for slot in self.slots:
                slot.render(display)

        
