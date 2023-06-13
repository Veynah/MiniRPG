import pygame
import pytmx
import pyscroll

from player import Player


# Les variables de la taille de la fenêtre du jeu
HEIGHT = 720
WIDTH = 1280


class Game:
    
    def __init__(self):
        # Creer la fenêtre du jeu
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("MiniRPG")
        
        # Charger la carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame('tiled/data/tmx/village.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        # map_layer va contenir tous les calques
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2
        # Dessiner le groupe de calque
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
    def run(self):
        
        # Boucle du jeu
        running = True
        
        while running:
            
            # On va dessiner les calques sur le screen
            self.group.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
        pygame.quit()
            