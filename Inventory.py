import pygame
from InventorySlot import InventorySlot



class Inventory:
    def __init__(self):
    
        self.slots = []
        self.visible = False
        

        self.image = pygame.image.load("img/item/Inventory.png")
        self.rect = self.image.get_rect()
        self.rect.midtop = (700, 10)
    

        self.slots.append(InventorySlot("img/item/coinIcon.png", (410, 15)))
        self.slots.append(InventorySlot("img/item/manapotionIcon.png", (480, 15)))
        self.slots.append(InventorySlot("img/item/shield.ico", (550, 15)))
        self.slots.append(InventorySlot("img/item/weapon.png", (630, 5)))
        self.slots.append(InventorySlot("img/item/xp2.png", (700, 15)))
        self.slots.append(InventorySlot("img/item/money_bag.png", (770, 15)))
        self.slots.append(InventorySlot("img/item/money_bag.png", (770, 15)))
        self.visible = False



    def toggleVisibility(self):
        self.visible = not self.visible

    def update(self, coins, manaPotions, shield, weapon, xp, moneyBag):
        self.slots[0].count = coins
        self.slots[1].count = manaPotions
        self.slots[2].count = shield
        self.slots[3].count = weapon
        self.slots[4].count = xp
        self.slots[5].count = moneyBag   

    def render(self, display):
        if self.visible:  # Only render if the inventory is visible
            display.blit(self.image, self.rect)
            for slot in self.slots:
                slot.render(display)

