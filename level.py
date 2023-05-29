class Level:
    def __init__(self, level_number, player, screen):
        self.level_number = level_number
        self.player = player
        self.screen = screen
        self.background = Background(self.level_number)
        self.ground = Ground(self.level_number)

    def change_level(self, new_level_number):
        self.level_number = new_level_number
        self.background.change_level(new_level_number)
        self.ground = Ground(new_level_number)  
        self.player.rect.center = (100, 100)  
    def render(self):
        self.background.render(self.screen)
        self.ground.render(self.screen)
