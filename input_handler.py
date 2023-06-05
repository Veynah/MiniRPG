#On fait une classe InputHandler pour gérer les inputs du joueur
import pygame
class InputHandler:
    def __init__(self, player):
        self.player = player

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and hasattr(self.player, 'move_left'):
                self.player.move_left()
            
            elif event.key == pygame.K_d and hasattr(self.player, 'move_right'):
                self.player.move_right()
            
            elif event.key == pygame.K_w and hasattr(self.player, 'jump'):
                self.player.jump()
            
            elif event.key == pygame.K_SPACE and hasattr(self.player, 'dash'):
                self.player.dash()
            
            elif event.key == pygame.K_1 and hasattr(self.player, 'sword_attack'):
                self.player.sword_attack()

            elif event.key == pygame.K_2 and hasattr(self.player, 'magic_spell'):
                self.player.magic_spell()


        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_a, pygame.K_d] and hasattr(self.player, 'stop_moving'):
                self.player.stop_moving()

    