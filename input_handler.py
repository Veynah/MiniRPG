#On fait une classe InputHandler pour gérer les inputs du joueur
import pygame

class InputHandler:
    def __init__(self):
        self.action = {
            pygame.K_q: self.move_left,
            pygame.K_d: self.move_right,
            pygame.K_s: self.move_down,
            pygame.K_SPACE: self.jump,
            pygame.K_LSHIFT: self.dash,
            pygame.K_1: self.sword_attack,
            pygame.K_2: self.hammer_attack,
            pygame.K_3: self.magic_spell,
            pygame.K_4: self.battle_shout,
        }
    def handle_input(self, event):
        action = self.actions.get(event.key)
        if action:
            action()

    