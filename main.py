import pygame
from pygame.locals import *
from sys import exit #importe le module exit de sys pour pouvoir fermer le programme sans créer d'erreur
from input_handler import InputHandler
from player_class import Player
from background import Background
from ground import Ground

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption('MiniRPG')
        self.clock = pygame.time.Clock()
        self.input_handler = InputHandler()
        self.player = Player("Player1", "player.png", 100, 100)  # Added a name to the player
        self.input_handler = InputHandler(self.player)
        self.background = Background(1)
        self.ground = Ground()
        self.level = Level(1, self.player, self.screen)
        
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

    def run(self):
        while True:
            self.level.render()
            self.background.render(self.screen)
            self.ground.render(self.screen)
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                else:
                    self.input_handler.handle_event(event)

            action = self.input_handler.get_current_action()
            if action:
                action_method = getattr(self.player, action, None)
                if action_method:
                    action_method()

            self.all_sprites.update()
            self.all_sprites.draw(self.screen)
            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    Game().run()