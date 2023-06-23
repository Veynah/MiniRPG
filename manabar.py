import pygame
from pygame.math import Vector2 as vec

class ManaBar(pygame.sprite.Sprite):
    """
        Classe représentant la barre de mana d'un personnage dans un jeu.

        Attributes:
            game (pygame): Instance du jeu actuel.
            max_mana (int): Quantité maximale de mana qu'un personnage peut avoir.
            mana (int): Quantité actuelle de mana du personnage.
            image (Surface): Image actuelle à afficher pour la barre de mana.
            pos (vec): Position actuelle de la barre de mana sur l'écran.
            mana_animations (list): Liste des images représentant les différents états de la barre de mana.
    """

    REGEN_EVENT = pygame.USEREVENT + 1
    def __init__(self, game, x, y):
        """
            Initialise une instance de la classe ManaBar.

            Args:
                game (pygame): Instance du jeu actuel.
                x (int): Position x initiale de la barre de mana.
                y (int): Position y initiale de la barre de mana.
        """
        super().__init__()
        self.game = game
        self.load_animations()
        
        self.max_mana = 5
        self.mana = self.max_mana
        self.image = self.mana_animations[self.mana]
        self.pos = vec(x, y)
        
        # REGEN_EVENT va nous rendre de la mana toutes les x secondes
        pygame.time.set_timer(self.REGEN_EVENT, 5000)
        
    def render(self, screen):
        """
                Affiche l'image actuelle de la barre de mana à sa position actuelle.

                Args:
                    screen (Surface): Surface sur laquelle la barre de mana est dessinée.
        """
        screen.blit(self.image, self.pos)
        
    def manaCost(self, manacost):

        """
           Diminue le montant de mana du personnage en fonction du coût en mana spécifié.
           Modifie également l'image de la barre de mana pour refléter le nouveau niveau de mana.

           Args:
               manacost (int): Le coût en mana de l'action effectuée par le personnage.

           Returns:
               bool: True si le personnage a suffisamment de mana pour effectuer l'action, False sinon.
        """

        if self.mana > 0 and self.mana >= manacost:
            self.mana -= manacost
            print(self.mana)
            self.image = self.mana_animations[self.mana]
            return True
        else:
            print("You have no Mana")
            return False
        
    def regen(self):
        """
            Régénère le mana du personnage s'il n'est pas déjà à son maximum.
            Modifie également l'image de la barre de mana pour refléter le nouveau niveau de mana.
        """

        if self.mana < self.max_mana:
            self.mana += 1
            self.image = self.mana_animations[self.mana]
        
    def load_animations(self):
        """
              Charge les images nécessaires pour l'animation de la barre de mana.
        """
        self.mana_animations = [
            pygame.image.load("img/item/mana0.png").convert_alpha(),
            pygame.image.load("img/item/mana1.png").convert_alpha(),
            pygame.image.load("img/item/mana2.png").convert_alpha(),
            pygame.image.load("img/item/mana3.png").convert_alpha(),
            pygame.image.load("img/item/mana4.png").convert_alpha(),
            pygame.image.load("img/item/mana5.png").convert_alpha(),
        ]
        
    def update(self, event):
        """ Met à jour la barre de mana et vérifie si l'événement REGEN_EVENT a été déclenché.
    Si c'est le cas, la méthode regen() est appelée pour régénérer le mana.

    Args:
        event (pygame.event.Event): L'événement à vérifier.
    """
        if event.type == self.REGEN_EVENT:
            self.regen()