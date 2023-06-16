<<<<<<< Updated upstream
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
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        # On va définir le rectangle de collision pour entrer dans la forêt
        enter_forest = tmx_data.get_object_by_name("enter_forest")
        self.enter_forest_rect = pygame.Rect(
            enter_forest.x, enter_forest.y, enter_forest.width, enter_forest.height
        )

    # Fonction qui run le jeu et dans laquelle se trouve la boucle
    def run(self):
        clock = pygame.time.Clock()
        # Boucle du jeu
        running = True

        while running:
            self.player.move()
            self.group.update()
            # print(self.walls)
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
=======
from item import Sword
from inventory import Inventory

class Game:
    def __init__(self):
        self.inventory = Inventory()
        self.player_action = None

    def add_sword(self):
        sword = Sword()
        self.inventory.add_item(sword)

    def remove_sword(self):
        for item in self.inventory.items:
            if isinstance(item, Sword):
                self.inventory.remove_item(item)
                break

    def combat(self, enemy):
        # Placeholder combat logic
        self.inventory.decrease_health(enemy.strength)
        if self.inventory.get_health() == 0:
            print("Game Over")
            return

        self.inventory.increase_level()

    def purchase_item(self, item, cost):
        if self.inventory.get_money() >= cost:
            self.inventory.decrease_money(cost)
            self.inventory.add_item(item)
        else:
            print("Not enough money to purchase item")

    def player_actions(self, action):
        if action == "P":
            self.add_sword()
        elif action == "R":
            self.remove_sword()
        else:
            print("Invalid action")
>>>>>>> Stashed changes
