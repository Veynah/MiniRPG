def gravity_check(self):
            hits = [blocker for blocker in self.blockers if self.rect.colliderect(blocker)]
            if self.vel.y > 0:
                  if hits:
                        lowest = hits[0]
                        for hit in hits:
                              if hit.top > lowest.top:
                                    lowest = hit
                        if self.pos.y < lowest.bottom:
                              self.pos.y = lowest.top + 1
                              self.vel.y = 0
                              self.jumping = False
                              
            self.pos.x = int(self.pos.x)
            self.pos.y = int(self.pos.y)
            self.rect.midbottom = self.pos
            
import pygame
from pygame.locals import K_q, K_d
from pygame.math import Vector2 as vec
import keyboard
import time

pygame.init()
# Les variables pour bouger
# On ajoute de la friction pour que les mouvements soient plus agréables
ACC = 2
FRIC = -0.6

# Les variables de l'écran
HEIGHT = 720
WIDTH = 1280

# Pour le moment je n'arrive pas à comprendre comment implémenter les sprites sheets donc je vais couper 
# les frames et les charger dans un dictionnaire pour faire les animations
player_run_anim_R = [pygame.image.load("img/player/Player_Run_R/Player_Run_R0.png"), pygame.image.load("img/player/Player_Run_R/Player_Run_R1.png"),
                     pygame.image.load("img/player/Player_Run_R/Player_Run_R2.png"), pygame.image.load("img/player/Player_Run_R/Player_Run_R3.png"),
                     pygame.image.load("img/player/Player_Run_R/Player_Run_R4.png"), pygame.image.load("img/player/Player_Run_R/Player_Run_R5.png"), 
                     pygame.image.load("img/player/Player_Run_R/Player_Run_R6.png"), pygame.image.load("img/player/Player_Run_R/Player_Run_R7.png"),]

player_run_anim_L = [pygame.image.load("img/player/Player_Run_L/Player_Run_L0.png"), pygame.image.load("img/player/Player_Run_L/Player_Run_L1.png"),
                     pygame.image.load("img/player/Player_Run_L/Player_Run_L2.png"), pygame.image.load("img/player/Player_Run_L/Player_Run_L3.png"),
                     pygame.image.load("img/player/Player_Run_L/Player_Run_L4.png"), pygame.image.load("img/player/Player_Run_L/Player_Run_L5.png"), 
                     pygame.image.load("img/player/Player_Run_L/Player_Run_L6.png"), pygame.image.load("img/player/Player_Run_L/Player_Run_L7.png"),]

class Player(pygame.sprite.Sprite):
      def __init__(self, blockers):
            super().__init__()
            self.image = pygame.image.load("img/player/test.png").convert_alpha()
            self.rect = self.image.get_rect()
            
            # Position and direction
            self.vx = 0
            self.pos = vec((340, 240))
            self.vel = vec(0, 0)
            self.acc = vec(0, 0)
            self.direction = "RIGHT"
            self.jumping = False
            self.running = False
            self.blockers = blockers
            
            self.time_since_last_frame = 0
            self.frame_duration = 100

            # Time counter for animation
            self.frame_index = 0

      def move(self):
        # Constante qui va accélérer vers le bas ce qui va simuler la gravité
            self.acc = vec(0,0.5)
            
            self.running = False
            
            # Cela va renvoyer les touches pressées 
            pressed_keys = pygame.key.get_pressed()

            # Accélère dans une direction ou une autre suivant la touche utilisée
            if pressed_keys[K_q]:  # Q pour aller à gauche
                  self.acc.x = -ACC
                  self.running = True
                  
            if pressed_keys[K_d]:  # D pour aller à droite
                  self.acc.x = ACC
                  self.running = True
                  
                  
                  

        # Détermine la vélocité en prenant en compte la friciton
            self.acc.x += self.vel.x * FRIC
            self.vel += self.acc
            new_pos = self.pos + self.vel + 0.5 * self.acc
            
            self.handle_collisions(new_pos)
            self.running = self.vel.x != 0
            

        
           
                        
            self.rect.midbottom = self.pos  # Update rect with new pos
            
            # Outil de debug
            print(f"Acceleration: {self.acc}, Velocity: {self.vel}, Position: {self.pos}")

      def gravity_check(self):
            hits = [blocker for blocker in self.blockers if self.rect.colliderect(blocker)]
            if self.vel.y > 0:
                  if hits:
                        lowest = hits[0]
                        for hit in hits:
                              if hit.top > lowest.top:
                                    lowest = hit
                        if self.pos.y < lowest.bottom:
                              self.pos.y = lowest.top + 1
                              self.vel.y = 0
                              self.jumping = False
                              
            self.pos.x = int(self.pos.x)
            self.pos.y = int(self.pos.y)
            self.rect.midbottom = self.pos
      
      def handle_collisions(self, new_pos):
            # This function checks for collisions and updates self.pos
            x_next = self.pos.x + self.vel.x
            y_next = self.pos.y + self.vel.y
            
            hitX = False
            hitY = False
            
            for blocker in self.blockers:
                  # Horizontal collisions
                  if self.vel.x > 0:  # moving right
                        if self.rect.right < blocker.left and x_next + self.rect.width >= blocker.left:
                              x_next = blocker.left - self.rect.width
                              hitX = True
                        elif self.vel.x < 0:  # moving left
                              if self.rect.left > blocker.right and x_next < blocker.right:
                                    x_next = blocker.right
                                    hitX = True

                  # Vertical collisions
                  if self.vel.y > 0:  # moving down
                        if self.rect.bottom < blocker.top and y_next + self.rect.height >= blocker.top:
                              y_next = blocker.top - self.rect.height
                              hitY = True
                  elif self.vel.y < 0:  # moving up
                        if self.rect.top > blocker.bottom and y_next < blocker.bottom:
                              y_next = blocker.bottom
                              hitY = True

            # Update the position
            self.pos.x = x_next
            self.pos.y = y_next

            # Adjust velocity if there was a collision
            if hitX:
                  self.vel.x = 0
            if hitY:
                  self.vel.y = 0
                  self.jumping = False
      
      
                              
      def jump(self):
            self.rect.y += 2
            hits = [blocker for blocker in self.blockers if self.rect.colliderect(blocker)]
            self.rect.y -= 2
            
            if hits and not self.jumping:
                  self.vel.y = -7
                  self.jumping = True
 
            
      
      def update(self):
            
            time_passed = pygame.time.get_ticks() - self.time_since_last_frame
            
            if time_passed > self.frame_duration:
                  self.time_since_last_frame = pygame.time.get_ticks()
                  if self.frame_index > 7: # Comme nous avons 8 images pour les animations, ceci nous permet de revenir à l'image 0 apres la 8eme frame
                        self.frame_index = 0
                        return
            
                  if self.jumping == False and self.running == True:
                        if self.vel.x > 0:
                              self.image = player_run_anim_R[self.frame_index]
                              self.direction = "RIGHT"
                        elif self.vel.x < 0:
                              self.image = player_run_anim_L[self.frame_index]
                              self.direction = "LEFT"
                        self.frame_index += 1
                  
                  # Returns to base frame if standing still and incorrect frame is showing
                  if abs(self.vel.x) < 0.2 and self.frame_index != 0:
                        self.frame_index = 0
                        if self.direction == "RIGHT":
                              self.image = player_run_anim_R[self.frame_index]
                        elif self.direction == "LEFT":
                              self.image = player_run_anim_L[self.frame_index]
            
            

      def attack(self):
            pass

      
def handle_collisions(self, new_pos):
            # This function checks for collisions and updates self.pos
            x_next = self.pos.x + self.vel.x
            y_next = self.pos.y + self.vel.y
            
            hitX = False
            hitY = False
            
            for blocker in self.blockers:
                  # Horizontal collisions
                  if self.vel.x > 0:  # moving right
                        if self.rect.right < blocker.left and x_next + self.rect.width >= blocker.left:
                              x_next = blocker.left - self.rect.width
                              hitX = True
                        elif self.vel.x < 0:  # moving left
                              if self.rect.left > blocker.right and x_next < blocker.right:
                                    x_next = blocker.right
                                    hitX = True

                  # Vertical collisions
                  if self.vel.y > 0:  # moving down
                        if self.rect.bottom < blocker.top and y_next + self.rect.height >= blocker.top:
                              y_next = blocker.top - self.rect.height
                              hitY = True
                  elif self.vel.y < 0:  # moving up
                        if self.rect.top > blocker.bottom and y_next < blocker.bottom:
                              y_next = blocker.bottom
                              hitY = True

            # Update the position
            self.pos.x = x_next
            self.pos.y = y_next

            # Adjust velocity if there was a collision
            if hitX:
                  self.vel.x = 0
            if hitY:
                  self.vel.y = 0
                  self.jumping = False

            
