import pygame


vec = pygame.math.Vector2

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, itemtype, name):
        super().__init__()

        self.ID = itemtype
        self.image = pygame.image.load(name).convert_alpha()
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.rect.topleft = self.pos

    def update(self, player):

        hits = self.rect.colliderect(player.rect)

        if hits:
            if self.ID == 0:
                pass
            elif self.ID == 1:
                player.healthBar.Heal(1)

            self.kill()


    def render(self, display):
        display.blit(self.image, self.pos)



# ID -> 0 -> Coin
# ID -> 1 -> Health

        

        
