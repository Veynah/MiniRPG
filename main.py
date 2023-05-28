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
        self.player = Player("Player1")  # Added a name to the player
        self.background = Background(1)
        

    def run(self):
        while True:
            self.background.render()
            self.ground.render()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    self.input_handler.handle_input(event)

            action = self.input_handler.get_current_action()
            if action:
                action_method = getattr(self.player, action, None)
                if action_method:
                    action_method()

            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    Game().run()