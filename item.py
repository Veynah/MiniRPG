import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self, image_path, position, item_type, extra_argument):
        super().__init__()
        self.image = None
        self.rect = None
        self.type = item_type
        self.position = position
        self.extra_argument = extra_argument
        self.load_image(image_path)

    def load_image(self, image_path):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
