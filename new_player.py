import pygame
from pygame.math import Vector2 as vec
from wall import Wall

# Les variables pour bouger
# On ajoute de la friction pour que les mouvements soient plus agréables
ACC = 0.8
FRIC = -0.2

# Les variables de l'écran
HEIGHT = 720
WIDTH = 1280


class NewPlayer(pygame.sprite.Sprite):
    def __init__(self, x, y, walls):
        super().__init__()
        self.sprite_sheet = pygame.image.load('img/player/Idle.png')
        self.image = self.get_image(0, 0)
        # Enlève la couleur noire du fond de l'image du joueur
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.vx = 0
        self.walls = walls
        self.position = vec(x, y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.direction = "RIGHT"
        self.jumping = False
        self.running = False
        self.attacking = False
        self.attack_frame = 0
        
        self.time_since_last_frame = 0
        self.frame_duration = 80
        
        # Time counter for animation
        self.frame_index = 0
        
    def move(self):
    # Constante qui va accélérer vers le bas ce qui va simuler la gravité
        self.acc = vec(0,0.5)
        
        # Running = faux si on est trop slow
        if abs(self.vel.x) > 0.1:
                self.running = True
        else:
                self.running = False

        # Cela va renvoyer les touches pressées 
        pressed_keys = pygame.key.get_pressed()

        # Accélère dans une direction ou une autre suivant la touche utilisée
        if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_q]:  # Q pour aller à gauche
                self.acc.x = -ACC
        elif pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:  # D pour aller à droite
                self.acc.x = ACC

        # Détermine la vélocité en prenant en compte la friciton
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        
        if abs(self.vel.x) < 0.01:
            self.vel.x = 0
        
    
        self.position.x += self.vel.x
        self.rect.x = self.position.x
        collisions = pygame.sprite.spritecollide(self, self.walls, False)
        for wall in collisions:
            if self.vel.x > 0:
                self.position.x = wall.rect.left - self.rect.width
            elif self.vel.x < 0:
                self.position.x = wall.rect.right
            self.vel.x = 0
        
        # Vertical movement
        self.position.y += self.vel.y
        self.rect.y = self.position.y
        self.gravity_check()

        # Outil de debug
        print(f"Acceleration: {self.acc}, Velocity: {self.vel}, Position: {self.position}")
        
        self.rect.topleft = self.position
    def gravity_check(self):
        hits = pygame.sprite.spritecollide(self, self.walls, False)
        if hits:
            # Detect if the character is moving downward
            if self.vel.y > 0:
                # Character is moving down
                for wall in hits:
                    # Place the character just above the wall
                    self.position.y = wall.rect.top - self.rect.height
                    # Stop any downward movement
                    self.vel.y = 0
                    self.jumping = False
            # Detect if character is moving upward
            elif self.vel.y < 0:
                # Character is moving up
                for wall in hits:
                    # Place the character just below the wall
                    self.position.y = wall.rect.bottom
                    # Stop any upward movement
                    self.vel.y = 0
            
    def jump(self):
    # Check if the player is on the ground and not currently jumping
        self.rect.y += 1
        hits = pygame.sprite.spritecollide(self, self.walls, False)
        self.rect.y -= 1

        # If on the ground and not jumping, initiate a jump
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -12
        
    
    def update(self):
        pass
        
    def get_image(self, x, y):
        image = pygame.Surface([27, 47])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 27, 47))
        return image