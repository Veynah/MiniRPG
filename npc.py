import pygame
from pygame.math import Vector2 as vec

ACC = 0.05
FRIC = -0.1


class NPC(pygame.sprite.Sprite):
    """
    Classe de base pour les NPCs (Non-Player Characters) dans un jeu Pygame.

    Args:
        x (int): Position initiale en x du NPC.
        y (int): Position initiale en y du NPC.
        walls (pygame.sprite.Group): Groupe de sprites représentant les murs ou obstacles.
        image_path (list of str): Chemins des images pour les animations du NPC.
        dialog (str): Dialogue du NPC.

    Attributs:
        images (list of pygame.Surface): Liste des images d'animation du NPC.
        image_index (int): Indice de l'image actuelle dans la liste des images.
        images_delay (int): Délai entre les images d'animation.
        counter (int): Compteur pour le délai des images.
        image (pygame.Surface): Image actuelle du NPC.
        rect (pygame.Rect): Rect représentant la position et la taille du NPC.
        dialog (str): Dialogue du NPC.
        vx (float): Vitesse en x du NPC.
        walls (pygame.sprite.Group): Groupe de sprites représentant les murs ou obstacles.
        position (pygame.math.Vector2): Position du NPC.
        vel (pygame.math.Vector2): Vitesse du NPC.
        acc (pygame.math.Vector2): Accélération du NPC.
        direction (str): Direction actuelle du NPC.
    """
    def __init__(self, x, y, walls, image_path, dialog):
        super().__init__()
        self.images = [pygame.image.load(path) for path in image_path]
        self.image_index = 0
        self.images_delay = 10
        self.counter = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        self.dialog = dialog
        self.vx = 0
        self.walls = walls
        self.position = vec(x, y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.direction = "LEFT"


    def update(self):
        """
         Met à jour l'image du NPC à chaque frame selon le délai des images.
        """
        self.counter += 1
        if self.counter >= self.images_delay:
            self.counter = 0
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]

    def update_NPC(self):
        """
        Met à jour la position, la vitesse et l'accélération du NPC.
        Applique également la friction.
        """
        self.acc = vec(0, 0.5)
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.position.x += self.vel.x
        self.position.y += self.vel.y
        self.rect.y = self.position.y
        self.rect.x = self.position.x
        self.collision_check()

    def collision_check(self):
        """
        Vérifie s'il y a une collision entre le NPC et les murs.
        Si c'est le cas, corrige la position du NPC et met sa vitesse à zéro.
        """

        move_by = int(self.vel.x)
        for _ in range(abs(move_by)):
            if move_by > 0:
                self.position.x += 1
            else:
                self.position.x -= 1
            self.rect.x = self.position.x
            collisions = pygame.sprite.spritecollide(self, self.walls, False)
            if collisions:
                if move_by > 0:
                    self.position.x = collisions[0].rect.left - self.rect.width - 3
                elif move_by < 0:
                    self.position.x = collisions[0].rect.right + 3
                self.vel.x = 0
                break

        collisions = pygame.sprite.spritecollide(self, self.walls, False)
        if collisions:
            if self.vel.y > 0:
                for wall in collisions:
                    self.position.y = wall.rect.top - self.rect.height
                    self.vel.y = 0
            elif self.vel.y < 0:
                for wall in collisions:
                    self.position.y = wall.rect.bottom
                    self.vel.y = 0


class Maire(NPC):
    """
       Classe pour le Maire, un type spécifique de NPC.
       Args:
           x (int): Position initiale en x du Maire.
           y (int): Position initiale en y du Maire.
           walls (pygame.sprite.Group): Groupe de sprites représentant les murs ou obstacles.
           dialog (str): Dialogue du Maire.
    """
    def __init__(self, x, y, walls, dialog):
        image_paths = [
            "img/NPCs/NPC_Maire1.png",
            "img/NPCs/NPC_Maire2.png",
            "img/NPCs/NPC_Maire3.png",
            "img/NPCs/NPC_Maire4.png"
        ]
        super().__init__(x, y, walls, image_paths, dialog)
        self.feet = self.rect.inflate(-10, -10)


class Forgeron(NPC):
    """
      Classe pour le Forgeron, un type spécifique de NPC.

      Args:
          x (int): Position initiale en x du Forgeron.
          y (int): Position initiale en y du Forgeron.
          walls (pygame.sprite.Group): Groupe de sprites représentant les murs ou obstacles.
          dialog (str): Dialogue du Forgeron.
    """
    def __init__(self, x, y, walls, dialog):
        image_paths = [
            "img/NPCs/NPC_forgeron1.png",
            "img/NPCs/NPC_forgeron2.png",
            "img/NPCs/NPC_forgeron3.png",
            "img/NPCs/NPC_forgeron4.png"
        ]
        super().__init__(x, y, walls, image_paths, dialog)
        self.feet = self.rect.inflate(-10, -10)


class Tavernier(NPC):
    """
     Classe pour le Tavernier, un type spécifique de NPC.

     Args:
         x (int): Position initiale en x du Tavernier.
         y (int): Position initiale en y du Tavernier.
         walls (pygame.sprite.Group): Groupe de sprites représentant les murs ou obstacles.
         dialog (str): Dialogue du Tavernier.
    """
    def __init__(self, x, y, walls, dialog):
        image_paths = [
            "img/NPCs/NPC_Tavernier1.png",
            "img/NPCs/NPC_Tavernier2.png",
            "img/NPCs/NPC_Tavernier3.png",
            "img/NPCs/NPC_Tavernier4.png"
        ]
        super().__init__(x, y, walls, image_paths, dialog)
        self.feet = self.rect.inflate(-10, -10)


class Explorer(NPC):
    """
       Classe pour l'Explorer, un type spécifique de NPC.

       Args:
           x (int): Position initiale en x de l'Explorer.
           y (int): Position initiale en y de l'Explorer.
           walls (pygame.sprite.Group): Groupe de sprites représentant les murs ou obstacles.
           dialog (str): Dialogue de l'Explorer.
    """
    def __init__(self, x, y, walls, dialog):
        image_paths = [
            "img/NPCs/NPC_Explorer1.png",
            "img/NPCs/NPC_Explorer2.png",
            "img/NPCs/NPC_Explorer3.png",
            "img/NPCs/NPC_Explorer4.png"
        ]
        super().__init__(x, y, walls, image_paths, dialog)
        self.feet = self.rect.inflate(-10, -10)
