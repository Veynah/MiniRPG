import pygame
import time
from pygame.locals import *
from sys import exit
from input_handler import InputHandler
from player import Player
from background import Background
from ground import Ground
from level import Level  

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption('MiniRPG')
        self.clock = pygame.time.Clock()

        self.player = Player("Player1", "player.png", 100, 100)  # Added a name to the player
        self.input_handler = InputHandler(self.player)

        self.level = Level(1, self.player, self.screen)  # Init the Level

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

    def run(self):
        while True:
            self.level.render()  # Render the level (which includes background and ground)
            
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