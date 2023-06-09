import pygame
import sys
import time
from pygame.locals import *
from sys import exit
import pytmx  # pytmx permet de charger les fichiers tmx, ce sont les fichiers maps
from pytmx.util_pygame import load_pygame
from tkinter import filedialog
from tkinter import *
from pygame.locals import QUIT, KEYDOWN
from tilerender import Renderer

import pygame
import sys
import pytmx
from pygame.locals import *

# Place the Renderer class here

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('MiniRPG')
clock = pygame.time.Clock()

# Create a Renderer object with the path to your tmx file
renderer = Renderer('tiled/data/tmx/village.tmx')

# Create the map surface
map_surface = renderer.make_map()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Blit the map_surface onto the screen
        screen.blit(map_surface, (0, 0))

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
