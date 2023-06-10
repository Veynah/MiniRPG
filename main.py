import sys
from sys import exit
import pygame
from pygame.locals import *
import pytmx  # pytmx permet de charger les fichiers tmx, ce sont les fichiers maps
from pytmx.util_pygame import load_pygame
from tkinter import filedialog
from tkinter import *
from tilerender import Renderer
from pygame.locals import *
from player import Player



pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('MiniRPG')
clock = pygame.time.Clock()

# Create a Renderer object with the path to your tmx file
renderer = Renderer('tiled/data/tmx/village.tmx')

# Create the map surface
map_surface = renderer.make_map()

all_sprites = pygame.sprite.Group()

# Create player
player = Player()

# Add player to all_sprites group
all_sprites.add(player)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #on clear d'abord l'écran avant de blit dessus les tiles utilisées par la carte
        screen.fill((0, 0, 0))
        
        # Blit the map_surface onto the screen
        screen.blit(map_surface, (0, 0))

        # Update sprites
        all_sprites.update()

        # Draw all sprites
        all_sprites.draw(screen)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
