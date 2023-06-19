import pygame
import pytmx
import pyscroll

from new_player import NewPlayer
from npc import NPC
from wall import Wall


# Les variables de la taille de la fenêtre du jeu
HEIGHT = 720
WIDTH = 1280


# Classe du jeu avec ses variables
class Game:
    def __init__(self):
        self.running = True
        self.map = "village"
        # Creer la fenêtre du jeu
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("MiniRPG")
        # Charger la carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame("tiled/data/tmx/village.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        self.NPC_image_path="img/NPCs/NPC_Mairie1.png"
        self.npc1=None
        # Trouver le groupe d'objets qui contient les NPCs
        npc_group = None
        for obj_group in tmx_data.objectgroups:
            if obj_group.name == "NPCs":
                npc_group = obj_group
                break

        npc_x = None
        npc_y = None
        npc_image_path = None
        # Vérifier si le groupe d'objets NPCs a été trouvé
        if npc_group is not None:
         # Parcourir les objets du groupe NPCs pour trouver le NPC "NPC_Maire"
            for obj in npc_group:
                if obj.name == "NPC_Maire":
                    npc_x = obj.x
                    npc_y = obj.y
                    npc_image_path = obj.properties.get("image_path", "")
                    break
         # Initialiser l'objet NPC
        if npc_x is not None and npc_y is not None and npc_image_path is not None:
            self.npc1 = NPC(npc_x, npc_y, npc_image_path)
        else:
            self.npc1 = None
          #déclaration de la variable npc1
       
        NPC_image_path = "img/NPCs/NPC_Maire1.png"
        self.NPC_image_path = NPC_image_path

       
       
        # map_layer va contenir tous les calques
        map_layer = pyscroll.orthographic.BufferedRenderer(
            map_data, self.screen.get_size()
        )
        map_layer.zoom = 2

        self.wall_group = pygame.sprite.Group()

        # Définr une liste qui va stocker les rectangles de collision
        self.walls = []
        for obj in tmx_data.objects:
            if obj.type == "collision":
                wall = Wall(obj.x, obj.y, obj.width, obj.height)
                self.wall_group.add(wall)
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        player_position = tmx_data.get_object_by_name("player_spawn1")
        self.player = NewPlayer(player_position.x, player_position.y, self.wall_group)
     
        # Dessiner le groupe de calque
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=8)
        self.group.add(self.player)

        # On va définir le rectangle de collision pour entrer dans la forêt
        enter_forest = tmx_data.get_object_by_name("enter_forest")
        self.enter_forest_rect = pygame.Rect(
            enter_forest.x, enter_forest.y, enter_forest.width, enter_forest.height
        )
    
   
    # Fonction qui permet de passer du village à la forêt
    def switch_level(self):
        self.map = "forest"
        # Charger la carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame("tiled/data/tmx/forest.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        # map_layer va contenir tous les calques
        map_layer = pyscroll.orthographic.BufferedRenderer(
            map_data, self.screen.get_size()
        )
        map_layer.zoom = 2

        self.wall_group = pygame.sprite.Group()

        # Définr une liste qui va stocker les rectangles de collision
        self.walls = []
        for obj in tmx_data.objects:
            if obj.type == "collision":
                wall = Wall(obj.x, obj.y, obj.width, obj.height)
                self.wall_group.add(wall)
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Dessiner le groupe de calque
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=9)
        self.group.add(self.player)

        # On va définir le rectangle de collision pour entrer dans la forêt
        enter_forest = tmx_data.get_object_by_name("exit_forest_to_village")
        self.enter_forest_rect = pygame.Rect(
            enter_forest.x, enter_forest.y, enter_forest.width, enter_forest.height
        )

        # Au niveau de la forêt
        spawn_village_point = tmx_data.get_object_by_name("spawn_forest")
        self.player.position[0] = spawn_village_point.x + 50
        self.player.position[1] = spawn_village_point.y
        self.player.update_walls(self.wall_group)

    # Fonction qui permet de passer de la forêt au village
    def switch_back(self):
        self.map = "village"
        # Charger la carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame("tiled/data/tmx/village.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        # map_layer va contenir tous les calques
        map_layer = pyscroll.orthographic.BufferedRenderer(
            map_data, self.screen.get_size()
        )
        map_layer.zoom = 2

        self.wall_group = pygame.sprite.Group()

        # Définr une liste qui va stocker les rectangles de collision
        self.walls = []
        for obj in tmx_data.objects:
            if obj.type == "collision":
                wall = Wall(obj.x, obj.y, obj.width, obj.height)
                self.wall_group.add(wall)
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Dessiner le groupe de calque
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=8)
        self.group.add(self.player)

        # On va définir le rectangle de collision pour entrer dans la forêt
        enter_forest = tmx_data.get_object_by_name("enter_forest")
        self.enter_forest_rect = pygame.Rect(
            enter_forest.x, enter_forest.y, enter_forest.width, enter_forest.height
        )

        spawn_village_point = tmx_data.get_object_by_name("enter_forest_exit")
        self.player.position[0] = spawn_village_point.x - 20
        self.player.position[1] = spawn_village_point.y
        self.player.update_walls(self.wall_group)

    # Fonction qui donne les conditions pour switcher de niveau
    def update(self):
        if self.map == "village" and self.player.rect.colliderect(
            self.enter_forest_rect
        ):
            self.switch_level()
            self.map = "forest"

        if self.map == "forest" and self.player.rect.colliderect(
            self.enter_forest_rect
        ):
            self.switch_back()
            self.map = "village"

    # Fonction qui run le jeu et dans laquelle se trouve la boucle
    def run(self):
        clock = pygame.time.Clock()
            # Boucle du jeu
        while self.running:
            self.update()
            self.player.move()
            self.group.update()
             #assignation de la variable npc1
           # Vérifier si l'objet NPC existe
            if self.npc1 is not None:
                self.npc1.update()
            self.npc1 = NPC(1585.33, 237.333, self.NPC_image_path)
            # print(self.walls)
            self.group.center(self.player.rect.center)
            # dessiné le pnc
            self.screen.blit(self.npc1.image, self.npc1.rect)
            self.npc1.draw(self.screen)
            # On va dessiner les calques sur le screen
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z or event.key == pygame.K_UP:
                        self.player.jump()

            clock.tick(60)
        pygame.quit()
