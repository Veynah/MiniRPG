import pygame
import sys
sys.path.insert(0, 'code')
from game import Game

if __name__ == "__main__":
    pygame.init()
    myGame = Game()
    myGame.run()