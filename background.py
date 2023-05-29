import pygame
# background class, it'll set a different background depending on the level that we are in the game.
class Background(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        
        self.level_background = {
            1: "Background1.png",
            2: "Background2.png",
            3: "Background3.png",
            4: "Background4.png",
            
        }
        
        self.bgimage = pygame.image.load(self.level_backgrounds.get(level, "DefaultBackground.png"))
        
        #stores position of the background so that we can implement a scrolling background.
        self.bgY = 0
        self.bgX = 0
 
    def render(self, screen):  
        screen.blit(self.bgimage, (self.bgX, self.bgY))

    def change_level(self, new_level):
        self.bgimage = pygame.image.load(self.level_backgrounds.get(new_level, "DefaultBackground.png")).convert_alpha()