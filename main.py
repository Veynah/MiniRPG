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

# Les variables de l'écran
HEIGHT = 720
WIDTH = 1280

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('MiniRPG')
clock = pygame.time.Clock()

# Create a Renderer object with the path to your tmx file
renderer = Renderer('tiled/data/tmx/village.tmx')

# Create the map surface
map_surface = renderer.make_map()

all_sprites = pygame.sprite.Group()

blockers = []
tilewidth = renderer.tmx_data.tilewidth
tileheight = renderer.tmx_data.tileheight

ground_layer = None
for layer in renderer.tmx_data.visible_layers:
    if isinstance(layer, pytmx.TiledTileLayer) and layer.name == "Ground":
        ground_layer = layer
        break
    
if ground_layer:
    for x, y, gid in ground_layer:
        if gid:  # Check if there is a tile here
            new_rect = pygame.Rect(x * tilewidth, y * tileheight, tilewidth, tileheight)
            blockers.append(new_rect)


# Create player
player = Player(blockers)

# Add player to all_sprites group
all_sprites.add(player)


def main():
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    player.jump()

        # On appelle la fonction move() de la classe player pour pouvoir le faire bouger
        player.move()
        player.gravity_check()
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
