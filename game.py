from turtle import Screen
import pygame
import pytmx
import pyscroll

from new_player import NewPlayer
from wall import Wall
from inventory import Inventory
from item import Item


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

        # Items
        self.all_items = pygame.sprite.Group()
        print(f"[DEBUG] All items after initialization: {self.all_items}")

        self.all_items = pygame.sprite.Group()

        #sword = Item("img/player/sword.png", (0, 0), "Sword", 500)
        #sword.rect.midtop = (WIDTH // 2, 400)  # Position sword in middle-top
        #self.all_items.add(sword)

        get_money = Item("img/player/coin.png", (0, 0),"i'm rich!!!", 500)
        get_money.rect.center = (200, 400) # Position money in middle-top right
        self.all_items.add(get_money)

        get_money = Item("img/player/coin.png",(0, 0), "i'm rich!!!", 500)
        get_money.rect.midleft = (700, 400)  # Position money in middle-top right
        self.all_items.add(get_money)

        get_money = Item("img/player/coin.png",(0, 0), "i'm rich!!!", 500)
        get_money.rect.topright = (WIDTH, 400)  # Position money in middle-top right
        self.all_items.add(get_money)
        
        self.show_inventory = False
        self.inventory_font = pygame.font.Font(None, 36)

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
        self.show_inventory = False
        # Boucle du jeu

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_i:
                        self.show_inventory = not self.show_inventory

                    if event.key == pygame.K_z or event.key == pygame.K_UP:
                        self.player.jump()

            self.update()
            self.player.move()
            self.group.update()

            
            self.group.center(self.player.rect.center)

            self.group.draw(self.screen)
            self.all_items.draw(self.screen)

            items_hit_list = pygame.sprite.spritecollide(self.player, self.all_items, True)
            for item in items_hit_list:
                self.player.pickup(item)
                print(self.player.inventory.items)
            
            if self.show_inventory:
                inventory_text = f"Swords: {self.player.inventory.get_item_count('sword')}"
                inventory_image = self.inventory_font.render(inventory_text, True, (255, 0, 0))
                self.screen.blit(inventory_image, (10, 0))

                inventory_text = f"Health: {self.player.inventory.get_health()}"
                inventory_image = self.inventory_font.render(inventory_text, True, (255, 0, 0))
                self.screen.blit(inventory_image, (10, 40))

                inventory_text = f"Level: {self.player.inventory.get_level()}"
                inventory_image = self.inventory_font.render(inventory_text, True, (255, 0, 0))
                self.screen.blit(inventory_image, (10, 80))

                inventory_text = f"Money: {self.player.inventory.get_money()}"
                inventory_image = self.inventory_font.render(inventory_text, True, (255, 0, 0))
                self.screen.blit(inventory_image, (10, 120))

                inventory_text = "Items: " + ", ".join([item.type for item in self.player.inventory.items])
                inventory_image = self.inventory_font.render(inventory_text, True, (255, 255, 255))
                self.screen.blit(inventory_image, (10, 160))

        
            money_text = "Money collected!"
            money_font = pygame.font.Font(None, 36)
            money_image = money_font.render(money_text, True, (255, 0, 0))
            self.screen.blit(money_image, (WIDTH // 2 - money_image.get_width() // 2, HEIGHT // 2 - money_image.get_height() // 2))
            self.update()
            self.player.move()
            self.group.update()
            # print(self.walls)
            self.group.center(self.player.rect.center)
            # On va dessiner les calques sur le screen
            self.group.draw(self.screen)
            self.all_items.draw(self.screen)
            
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()