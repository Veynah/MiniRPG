#On fait une classe InputHandler pour gérer les inputs du joueur
import pygame

class InputHandler:
    def __init__(self, player):
        self.player = player

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.player.move_left()
            elif event.key == pygame.K_d:
                self.player.move_right()
            elif event.key == pygame.K_w:
                self.player.jump()
            elif event.key == pygame.K_SPACE:
                self.player.dash()
            elif event.key == pygame.K_1:
                self.player.sword_attack()
            elif event.key == pygame.K_2:
                self.player.hammer_attack()
            elif event.key == pygame.K_3:
                self.player.magic_spell()
            elif event.key == pygame.K_4:
                self.player.battle_shout()

        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_a, pygame.K_d]:
                self.player.stop_moving()

    