#On fait une classe InputHandler pour gérer les inputs du joueur
import pygame

class InputHandler:
    def __init__(self):
        self.actions = {
            pygame.K_a: 'move_left',
            pygame.K_d: 'move_right',
            pygame.K_s: 'move_down',
            pygame.K_SPACE: 'jump',
            pygame.K_LSHIFT: 'dash',
            pygame.K_1: 'sword_attack',
            pygame.K_2: 'hammer_attack',
            pygame.K_3: 'magic_spell',
            pygame.K_4: 'battle_shout',
        }
        self.current_action = None

    def handle_input(self, event):
        self.current_action = self.actions.get(event.key)

    def get_current_action(self):
        return self.current_action
    