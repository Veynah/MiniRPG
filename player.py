import pygame
from pygame.math import Vector2 as vec
from spritesheet import SpriteSheet, Animation

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # Load the sprite sheet
        self.sprite_sheet = SpriteSheet("img/player/Idle.png", bg=(255, 255, 255)) # Assuming white is the background color you want to make transparent
        
        # Define the frames (x, y, width, height) 
        frames = [(49, 17, 27, 47), (177, 17, 27, 47), (49, 81, 27, 47), (177, 81, 27, 47), (49, 145, 27, 47), (177, 145, 27, 47), (49, 210, 27, 47), (177, 210, 27, 47)]
        
        # Get the animation from the sprite sheet
        self.animation = self.sprite_sheet.get_animation(frames, frame_duration=0.1, mode=SpriteSheet.Animation.PlayMode.LOOP)
        
        # Starting image
        self.image = self.animation.get_frame(0)
        self.rect = self.image.get_rect()

        # Position and direction
        self.vx = 0
        self.pos = vec((150, 150))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.direction = "RIGHT"
        
        # Time counter for animation
        self.time = 0

    def update(self):
        super().update(1/self.screen.game.fps)
        self.animate()

		# update vectors
        self.acc = vec(0, 0)
	    self.get_keys()

		# apply friction
		self.acc.x += self.vel.x*self.player_friction
		# equations of motion
		self.vel += self.acc
		self.pos += self.vel + 0.5*self.acc

		self.rect.midbottom = self.pos
        
    # ... rest of the Player class


    def move(self):
        pass
    
    def update(self):
        pass
    
    def attack(self):
        pass
    
    def jump(self):
        pass
