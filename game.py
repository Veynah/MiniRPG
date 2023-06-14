import pygame
import pytmx
import pyscroll

from new_player import NewPlayer
from wall import Wall


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
        
        self.wall_group = pygame.sprite.Group()
        
        # Définr une liste qui va stocker les rectangles de collision
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
        
    #def handle_input(self):
        #pressed = pygame.key.get_pressed()
        
        #if pressed[pygame.K_UP] or pressed[pygame.K_z]:
            #print("Haut")
        #elif pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
            #print("Droite")
        #elif pressed[pygame.K_LEFT] or pressed[pygame.K_q]:
            #print("Gauche")
        
    def run(self):
        
        clock = pygame.time.Clock()
        # Boucle du jeu
        running = True
        
        while running:
            
            self.player.move()
            self.group.update()
            #print(self.walls)
            self.group.center(self.player.rect.center)
            # On va dessiner les calques sur le screen
            self.group.draw(self.screen)
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z or event.key == pygame.K_UP:
                        self.player.jump()
                
                    
            clock.tick(60)
        pygame.quit()
            