class Ground(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        self.level_grounds = {
            1: "Ground1.png",
            2: "Ground2.png",
            3: "Ground3.png",
            4: "Ground4.png"
        }
        self.image = pygame.image.load(self.level_grounds.get(level, "DefaultGround.png"))
        self.rect = self.image.get_rect(center=(350, 350))

    def render(self):
        displaysurface.blit(self.image, (self.rect.x, self.rect.y))
