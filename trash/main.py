import sys
from sys import exit
import pygame
from pygame.locals import KEYDOWN, QUIT
import pytmx  # pytmx permet de charger les fichiers tmx, ce sont les fichiers maps
import pyscroll
from pytmx.util_pygame import load_pygame
from tkinter import filedialog
from tkinter import *
from tilerender import Renderer
from pygame.locals import *
from player import Player
from item import Item
import pygame.font
from inventory import Inventory



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
player = Player("img/player/test.png", 0, 0, blockers)

# Add player to all_sprites group
all_sprites.add(player)

inventory_font = pygame.font.Font(None, 36)

def main():

    all_items = pygame.sprite.Group()

    sword = Item("img/player/sword.png", (0, 0), "Sword", 500)
    sword.rect.midtop = (WIDTH // 2, 100)  # Position sword in middle-top
    all_items.add(sword)

    get_money = Item("img/player/coin.png", (0, 0),"i'm rich!!!", 500)
    get_money.rect.center = (200, 50) # Position money in middle-top right
    all_items.add(get_money)
    money_group = pygame.sprite.Group(get_money)

    get_money = Item("img/player/coin.png",(0, 0), "i'm rich!!!", 500)
    get_money.rect.midleft = (700, 200)  # Position money in middle-top right
    all_items.add(get_money)
    money_group = pygame.sprite.Group(get_money)

    get_money = Item("img/player/coin.png",(0, 0), "i'm rich!!!", 500)
    get_money.rect.topright = (WIDTH, 150)  # Position money in middle-top right
    all_items.add(get_money)
    money_group = pygame.sprite.Group(get_money)

    show_inventory = False
    inventory_font = pygame.font.Font(None, 36)  # Move this line outside the `if show_inventory:` block



    while True:
        player.gravity_check()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    player.jump()

                if event.key == pygame.K_i:  # Toggle inventory visibility on "i" key press
                    show_inventory = not show_inventory

    

        if show_inventory:
            inventory_text = f"Swords: {player.inventory.get_item_count('sword')}"
            inventory_image = inventory_font.render(inventory_text, True, (255, 0, 0))
            screen.blit(inventory_image, (10, 0))

        money_hit_list = pygame.sprite.spritecollide(player, money_group, True)
        if money_hit_list:
            money_text = "Money collected!"
            money_font = pygame.font.Font(None, 36)
            money_image = money_font.render(money_text, True, (255, 0, 0))
            screen.blit(money_image, (WIDTH // 2 - money_image.get_width() // 2, HEIGHT // 2 - money_image.get_height() // 2))

        pygame.display.flip()


        all_sprites.update()
        # On appelle la fonction move() de la classe player pour pouvoir le faire bouger
        player.move()
        
        #on clear d'abord l'écran avant de blit dessus les tiles utilisées par la carte
        screen.fill((0, 0, 0))
        
        # Blit the map_surface onto the screen
        screen.blit(map_surface, (0, 0))

        # Update sprites
        
        # Draw all sprites
        all_sprites.draw(screen)

        all_items.draw(screen)

        items_hit_list = pygame.sprite.spritecollide(player, all_items, True)
        for item in items_hit_list:
            player.pickup(item)

        if show_inventory:
            inventory_text = f"Swords: {player.inventory.get_item_count('sword')}"
            inventory_font = pygame.font.Font(None, 36)
            inventory_image = inventory_font.render(inventory_text, True, (255, 0, 0))
            screen.blit(inventory_image, (10, 0))
            inventory_text = f"Health: {player.inventory.get_health()}"
            inventory_image = inventory_font.render(inventory_text, True, (255, 0, 0))
            screen.blit(inventory_image, (10, 40))

            inventory_text = f"Level: {player.inventory.get_level()}"
            inventory_image = inventory_font.render(inventory_text, True, (255, 0, 0))
            screen.blit(inventory_image, (10, 80))

            inventory_text = f"Money: {player.inventory.get_money()}"
            inventory_image = inventory_font.render(inventory_text, True, (255, 0, 0))
            screen.blit(inventory_image, (10, 120))

            inventory_text = "Items: " + ", ".join([item.type for item in player.inventory.items])
            inventory_image = inventory_font.render(inventory_text, True, (255, 0, 0))
            screen.blit(inventory_image, (10, 160))
        
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
