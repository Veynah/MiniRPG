import pygame
import pytmx
import pyscroll
from Inventory import Inventory
from pygame.locals import *
import sys
from HealthBar import HealthBar
from InventorySlot import InventorySlot

from new_player import NewPlayer
from wall import Wall

pygame.init()


# Les variables de la taille de la fenêtre du jeu
HEIGHT = 720
WIDTH = 1280


class Game:
    
    def __init__(self):

        # Creer la fenêtre du jeu
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("MiniRPG")

        # Initialize other game components
        self.inventory = Inventory()
        self.healthbar = HealthBar(x=10, y=10)
        
        # Charger la carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame('tiled/data/tmx/village.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        # map_layer va contenir tous les calques
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2
        
        self.wall_group = pygame.sprite.Group()
        
        # Définr une liste q`ui` va stocker les rectangles de collision
        self.walls = []
        for obj in tmx_data.objects:
            if obj.type == 'collision':
                wall = Wall(obj.x, obj.y, obj.width, obj.height)
                self.wall_group.add(wall)
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        
        player_position = tmx_data.get_object_by_name("player_spawn1")
        self.player = NewPlayer(player_position.x, player_position.y, self.wall_group)
        
        
        
        # Dessiner le groupe de calque
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=10)
        self.group.add(self.player)
        
        
    def run(self):

        # Boucle du jeu
        clock = pygame.time.Clock()
        running = True

        while running:
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z or event.key == pygame.K_UP:
                        self.player.jump()
                    if event.key == pygame.K_i:  # Toggle inventory visibility on "i" key press
                        self.inventory.toggleVisibility()
                    if event.key == pygame.K_SPACE:  # Assuming space key causes damage to the player
                        damage_amount = 1  # Adjust the damage amount as per your requirements
                        self.healthbar.takeDamage(damage_amount)
                    if event.key == pygame.K_h:  # Assuming "h" key triggers healing
                        healing_amount = 1  # Adjust the healing amount as per your requirements
                        self.healthbar.Heal(healing_amount)
            
            self.player.move()
            self.group.update()
            #print(self.walls)
            self.group.center(self.player.rect.center)
            
            # On va dessiner les calques sur le screen
            self.group.draw(self.screen)
        
            self.inventory.render(self.screen)
            self.healthbar.render(self.screen)

            pygame.display.flip() 
            clock.tick(60)

        pygame.quit()
            