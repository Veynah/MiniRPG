import pygame
import sys
import time
from pygame.locals import *
from sys import exit
import pytmx  # pytmx permet de charger les fichiers tmx, ce sont les fichiers maps
from pytmx.util_pygame import load_pygame
from tkinter import filedialog
from tkinter import *
import random
from pygame.locals import QUIT, KEYDOWN


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)


pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('MiniRPG')
clock = pygame.time.Clock()

tiled_map = pytmx.load_pygame('tiled/data/tmx/village.tmx', invert_y=True)
sprite_group = pygame.sprite.Group()

# Create Tile objects for each tile and add them to the sprite group
for layer in tiled_map.visible_tile_layers:
    if isinstance(layer, pytmx.TiledTileLayer):
        for x, y, gid in layer:
            tile = tiled_map(gid)
            if tile:
                pos = (x * 16, y * 16)
                Tile(pos=pos, surf=tile, groups=sprite_group)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill('black')

        # Draw all sprites in the group
        sprite_group.draw(screen)

        clock.tick(60)
        pygame.display.update()


if __name__ == "__main__":
    main()
