import pygame, sys
import time
from pygame.locals import *
from sys import exit
from input_handler import InputHandler
from player import Player
from level import Level  
import pytmx #pytmx permet de charger les fichiers tmx, ce sont les fichiers maps
from pytmx.util_pygame import load_pygame


class Game:
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((800,600))
        
        pygame.display.set_caption('MiniRPG')
        
        self.clock = pygame.time.Clock()

        self.player = Player("Player1", "C:/Users/dark-/VSC/MiniRPG/img/player/test.png", -36, 19)  # Added a name to the player
        
        self.input_handler = InputHandler(self.player)

        self.all_sprites = pygame.sprite.Group()
        
        self.all_sprites.add(self.player)
        
        self.current_level = None

    def load_level(self, tmx_file):
        if self.current_level is not None:
            # Clean up the current level if necessary
            pass
        self.current_level = Level(tmx_file, self.player, self.screen)



    def run(self):
        self.load_level("C:/Users/dark-/VSC/MiniRPG/tiled/data/tmx/village.tmx")
        
        while True:
            self.current_level.render()  # Render the level (which includes background and ground)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                else:
                    self.input_handler.handle_event(event)

            

            self.all_sprites.update()
            self.all_sprites.draw(self.screen)
            pygame.display.update()
            self.clock.tick(60)

            if self.current_level.player_has_reached_end_of_level():
                self.load_level("C:/Users/dark-/VSC/MiniRPG/tiled/data/tmx/village.tmx")
if __name__ == "__main__":
    Game().run()