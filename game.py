import pygame
import pytmx
import pyscroll

from dialog import DialogBox
from npc_dialogues import npc_dialogues
from npc import Maire, Tavernier, Forgeron, Explorer

from new_player import NewPlayer
from enemy import Skeleton1, Skeleton2, Skeleton3
from wall import Wall

from Inventory import Inventory
from HealthBar import HealthBar
from manabar import ManaBar
# Les variables de la taille de la fenêtre du jeu
HEIGHT = 720
WIDTH = 1280


# Classe du jeu avec ses variables
class Game:
    def __init__(self):
        self.running = True
        self.map = "village"

        # Intégration de la boîte de dialogue
        self.npc_dialogues = npc_dialogues
        self.dialog_box = DialogBox()

        # Créer la fenêtre du jeu
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("MiniRPG")

        # Initialize other game components
        self.inventory = Inventory()
        self.healthbar = HealthBar(self, 10, 10)
        self.manabar = ManaBar(self, 10, 31)
        self.fireballs = pygame.sprite.Group()

        # Initialisation des groupes
        self.npc_group = pygame.sprite.Group()
        self.enemies_group = pygame.sprite.Group()

        # Charger la carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame("tiled/data/tmx/village.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        # map_layer va contenir tous les calques
        map_layer = pyscroll.orthographic.BufferedRenderer(
            map_data, self.screen.get_size()
        )
        map_layer.zoom = 2
        self.wall_group = pygame.sprite.Group()

        self.lava_blocks = []
        # Définr une liste qui va stocker les rectangles de collision
        self.walls = []
        for obj in tmx_data.objects:
            if obj.type == "collision":
                wall = Wall(obj.x, obj.y, obj.width, obj.height)
                self.wall_group.add(wall)
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        player_position = tmx_data.get_object_by_name("player_spawn1")
        self.player = NewPlayer(self, player_position.x, player_position.y, self.wall_group)

        # Dessiner le groupe de calque
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=8)
        self.group.add(self.player)
        self.group.add(self.fireballs)

        # Spawn les NPCs -------------------------------------------------------------
        for obj in tmx_data.objects:
            if obj.name == "NPC_Maire":
                if obj.name == "NPC_Maire":
                    npc_maire = Maire(obj.x, obj.y, self.wall_group, self.npc_dialogues["Maire"])
                    self.npc_group.add(npc_maire)
            elif obj.name == "NPC_Tavernier":
                npc_tavernier = Tavernier(obj.x, obj.y, self.wall_group,self.npc_dialogues["Tavernier"])
                self.npc_group.add(npc_tavernier)
            elif obj.name == "NPC_Forgeron":
                npc_forgeron = Forgeron(obj.x, obj.y, self.wall_group,self.npc_dialogues["Forgeron"])
                self.npc_group.add(npc_forgeron)
            elif obj.name == "NPC_Explorer":
                npc_explorer = Explorer(obj.x, obj.y, self.wall_group, self.npc_dialogues["Explorer"])
                self.npc_group.add(npc_explorer)

        # Ajouter les NPCs au groupe Pyscroll
        for npc in self.npc_group:
            self.group.add(npc)

        # On va définir le rectangle de collision pour entrer dans la forêt
        enter_forest = tmx_data.get_object_by_name("enter_forest")
        self.enter_forest_rect = pygame.Rect(
            enter_forest.x, enter_forest.y, enter_forest.width, enter_forest.height
        )
        # FONT pour le game over
        self.game_over_font = pygame.font.Font(None, 75)
        self.game_over_message = self.game_over_font.render(
            "GAME OVER", True, (255, 0, 0)
        )  # Red color
        self.show_game_over = False
    
    def Newplayer_nearby(self):
        interaction_distance = 50 #la distance maximal à laquelle le joeur peut agir

        for npc in self.npc_group:
            #calcule la distance
            distance=abs(self.player.rect.x - npc.rect.x) + abs(self.player.rect.y - npc.rect.y)

            #si le npc est a - de interaction
            if distance<= interaction_distance:
                return npc #retourner le npc

        return None

    # Fonction qui permet de passer du village à la forêt
    def switch_level(self):
        self.map = "forest"
        # Vider le groupe de PNJ
        self.npc_group.empty()

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

        # ce sont les blocs de lave qui vont nous tuer
        self.lava_blocks = []
        for obj in tmx_data.objects:
            if obj.type == "lava":
                self.lava_blocks.append(
                    pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                )

        # Spawn les monstres -------------------------------------------------------------
        for obj in tmx_data.objects:
            if obj.name == "skeleton_spawn":
                skeleton1 = Skeleton1(obj.x, obj.y, self.wall_group)
                self.enemies_group.add(skeleton1)
            elif obj.name == "skeletonshield_spawn":
                skeleton2 = Skeleton2(obj.x, obj.y, self.wall_group)
                self.enemies_group.add(skeleton2)
            elif obj.name == "skeletonlancer_spawn":
                skeleton3 = Skeleton3(obj.x, obj.y, self.wall_group)
                self.enemies_group.add(skeleton3)

        # Dessiner le groupe de calque
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=9)
        self.group.add(self.player)
        self.group.add(self.fireballs)
        for enemy in self.enemies_group:
            self.group.add(enemy)

        # On va définir le rectangle de collision pour entrer dans la forêt
        enter_forest = tmx_data.get_object_by_name("exit_forest_to_village")
        self.enter_forest_rect = pygame.Rect(
            enter_forest.x, enter_forest.y, enter_forest.width, enter_forest.height
        )

        # Au niveau de la forêt
        spawn_village_point = tmx_data.get_object_by_name("spawn_forest")
        self.player.position[0] = spawn_village_point.x + 30
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

        # Spawn les NPCs -------------------------------------------------------------
        for obj in tmx_data.objects:
            if obj.name == "NPC_Maire":
                if obj.name == "NPC_Maire":
                    npc_maire = Maire(obj.x, obj.y, self.wall_group, self.npc_dialogues["Maire"])
                    self.npc_group.add(npc_maire)
            elif obj.name == "NPC_Tavernier":
                npc_tavernier = Tavernier(obj.x, obj.y, self.wall_group,self.npc_dialogues["Tavernier"])
                self.npc_group.add(npc_tavernier)
            elif obj.name == "NPC_Forgeron":
                npc_forgeron = Forgeron(obj.x, obj.y, self.wall_group,self.npc_dialogues["Forgeron"])
                self.npc_group.add(npc_forgeron)
            elif obj.name == "NPC_Explorer":
                npc_explorer = Explorer(obj.x, obj.y, self.wall_group, self.npc_dialogues["Explorer"])
                self.npc_group.add(npc_explorer)

        # Dessiner le groupe de calque
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=8)
        self.group.add(self.player)
        # Ajouter les NPCs au groupe Pyscroll
        for npc in self.npc_group:
            self.group.add(npc)
        self.enemies_group.empty()

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

        if self.show_game_over:
            self.screen.fill((0, 0, 0))
            self.screen.blit(
                self.game_over_message,
                (
                    WIDTH / 2 - self.game_over_message.get_width() / 2,
                    HEIGHT / 2 - self.game_over_message.get_height() / 2,
                ),
            )
            pygame.display.flip()
            pygame.time.delay(3500)
            self.show_game_over = False

    def player_death(self):
        self.healthbar.health = 0
        self.healthbar.health = self.healthbar.max_health
        self.show_game_over = True
        self.switch_back()

        tmx_data = pytmx.util_pygame.load_pygame("tiled/data/tmx/village.tmx")
        player_spawn_point = tmx_data.get_object_by_name("player_spawn1")
        self.player.position[0] = player_spawn_point.x
        self.player.position[1] = player_spawn_point.y

    # Fonction qui run le jeu et dans laquelle se trouve la boucle
    def run(self):
        clock = pygame.time.Clock()
        player_last_damage_time = 0
        player_damage_cooldown = 1500

        # Boucle du jeu
        while self.running:
            self.update()
            for fireball in self.fireballs:
                fireball.update()
            
            if self.player.attacking:
                self.player.attack()
            self.player.move()
            current_time = pygame.time.get_ticks()
            
            if self.healthbar.health <= 0:
                self.player_death()

            for enemy in self.enemies_group:
                enemy.update_enemy(self.player)

                # Check si le joueur rentre en collision avec les enemies ET si l'enemie attaque
                if pygame.sprite.collide_mask(self.player, enemy) and enemy.attacking:
                    # Check si la fênetre de réception de dégâts pour le joueur
                    if current_time - player_last_damage_time > player_damage_cooldown:
                        damage_amount = 1  # adjust this as needed
                        self.healthbar.takeDamage(damage_amount)
                        player_last_damage_time = current_time

            # NPC
            for npc in self.npc_group:
                npc.update_NPC()

            self.group.update()
            self.group.center(self.player.rect.center)

            # System de combat basic, inflige 1 de dégâts à l'ennemie par attack counter
            if self.player.attacking:
                for enemy in self.enemies_group:
                    if pygame.sprite.collide_mask(self.player, enemy):
                        enemy.take_damage(1, self.player.attack_counter)
                        
            if self.player.magic_attacking:
                for fireball in self.fireballs:
                    for enemy in self.enemies_group:
                        if pygame.sprite.collide_mask(fireball, enemy):
                            enemy.take_magic_damage(fireball.damage)
                            fireball.kill()

            # Bloc qui va vérifier si on entre en collision avec la lave, si oui, game over
            for lava_block in self.lava_blocks:
                if self.player.rect.colliderect(lava_block):
                    self.player_death()

            # On va dessiner les calques sur le screen
            self.group.draw(self.screen)
            self.inventory.render(self.screen)
            self.healthbar.render(self.screen)
            #dessiner la box de dialog
            self.dialog_box.render(self.screen)
            self.manabar.render(self.screen)

            # Dessiner la boîte de dialogue
            self.dialog_box.render(self.screen)

            pygame.display.flip()

            for event in pygame.event.get():
                self.manabar.update(event)
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                       npc = self.Newplayer_nearby()
                       if npc is not None:
                           self.dialog_box.execute(npc.dialog)
                    if event.key == pygame.K_t:
                        self.dialog_box.terminate()
                    
                    if event.key == pygame.K_z or event.key == pygame.K_UP:
                        self.player.jump()                 
                    if (
                        event.key == pygame.K_i
                    ):  # Toggle inventory visibility on "i" key press
                        self.inventory.toggleVisibility()
                    if event.key == pygame.K_h or event.key == pygame.K_SPACE and not self.player.healing:
                        self.player.heal()
                        self.player.healing = True
                    if event.key == pygame.K_a or event.key == pygame.K_RETURN:
                        if not self.player.attacking:
                            self.player.attacking = True
                            self.player.attack()
                            self.player.attack_counter = 1  # Premiere attaque
                        else:
                            if self.player.attack_counter < 4:
                                self.player.attack_counter += 1
                    if event.key == pygame.K_f:
                        self.player.fireball(3, 4)

            clock.tick(60)
        pygame.quit()
