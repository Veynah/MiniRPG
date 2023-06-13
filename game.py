import pygame
import pytmx
import pyscroll

from new_player import NewPlayer


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
        
        player_position = tmx_data.get_object_by_name("player_spawn1")
        self.player = NewPlayer(player_position.x, player_position.y)
        
        # Dessiner le groupe de calque
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        self.group.add(self.player)
        
    def handle_input(self):
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_UP] or pressed[pygame.K_z]:
            print("Haut")
        elif pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
            print("Droite")
        elif pressed[pygame.K_LEFT] or pressed[pygame.K_q]:
            print("Gauche")
        
    def run(self):
        
        # Boucle du jeu
        running = True
        
        while running:
            
            self.handle_input()
            self.group.update()
            self.group.center(self.player.rect.center)
            # On va dessiner les calques sur le screen
            self.group.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
        pygame.quit()
            