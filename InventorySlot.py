import pygame


class InventorySlot:
    def __init__(self, name, pos, quantity=0):
        self.image = pygame.image.load(name)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.count = quantity

        self.font = pygame.font.Font("img/Fonts/Frostbite.ttf", 25)

    def render(self, display):
        text = self.font.render(str(self.count), True, (0, 0, 0))
        display.blit(self.image, self.rect)
        display.blit(text, self.rect.midright)

    def get_image_path(self):
        return self.image.get_path()
    
