import pygame
from InventorySlot import InventorySlot

class Inventory:
    def __init__(self):
        self.slots = []
        self.coins = 0 
        self.image = pygame.image.load("img/item/Inventory.png")
        self.rect = self.image.get_rect()
        self.rect.midtop = (700, 10)

        self.coin_img = pygame.image.load("img/item/coinIcon.png")

        coin_slot = InventorySlot("img/item/coinIcon.png", (410, 15))
        self.slots.append(coin_slot)
        self.slots.append(InventorySlot("img/item/manapotionIcon.png", (480, 15)))
        self.slots.append(InventorySlot("img/item/shield.ico", (550, 15)))
        self.slots.append(InventorySlot("img/item/weapon.png", (630, 5)))
        self.slots.append(InventorySlot("img/item/xp2.png", (700, 15)))
        self.slots.append(InventorySlot("img/item/money_bag.png", (770, 15)))

        self.visible = False

        self.font = pygame.font.SysFont(None, 24)  # Define the font for rendering
    
    def add_coins(self, amount):
        self.coins += amount

    def toggleVisibility(self):
        self.visible = not self.visible

    def render(self, display):
        if self.visible:
            display.blit(self.image, self.rect)
            for slot in self.slots:
                slot.render(display)

    def get_coin_quantity(self):
        coin_count = 0
        for slot in self.slots:
            if slot.image == pygame.image.load("img/item/money_bag.png"):
                coin_count += slot.count
        return coin_count

class Maire(Inventory):
    def __init__(self, x, y, walls, inventory):
        super().__init__()
        self.rect.x = x
        self.rect.y = y
        self.walls = walls
        self.inventory = inventory
        inventory = Inventory()
        inventory = Inventory()
        maire = Maire(x, y, walls, inventory)
        
        for slot in inventory.slots:
            print(slot.image) 


        coin_slot = next(
            (slot for slot in inventory.slots if slot.image == pygame.image.load("img/item/money_bag.png")),
            None
        )
        if coin_slot:
            coin_slot.count = 30000  # Initialize with 30000 coins

    def give_coins_to_player(self, player_inventory, amount):
        coin_slot = next(
            (slot for slot in self.inventory.slots if slot.image == pygame.image.load("img/item/money_bag.png")),
            None
        )
        if coin_slot:
            if coin_slot.count >= amount:
                coin_slot.count -= amount
                print("Maire's coin count:", coin_slot.count)
                player_inventory.add_coins(amount)
            else:
                print("Maire does not have enough coins in the inventory.")
        else:
            print("Maire does not have coins in the inventory.")
    
    def remove_coins(self, amount):
        for slot in self.slots:
            if slot.image == pygame.image.load("img/item/money_bag.png"):
                if slot.count >= amount:
                    slot.count -= amount
                    return
                else:
                    amount -= slot.count
                    slot.count = 0

    def render(self, display):
        super().render(display)
        maire_coin_text = self.font.render("Maire Coins: " + str(self.get_coin_quantity()), True, (255, 255, 255))
        display.blit(maire_coin_text, (10, 80))


# Rest of the code...
