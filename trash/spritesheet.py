#animation de spritesheets tiré de ça https://github.com/HUCORP-admin/Sprite-Animations-in-Pygame/blob/main/spritesheet.py
#code changé pour pouvoir charger plusieurs fichiers de spritesheets
import pygame as pg
from enum import Enum

class SpriteSheet:
	def __init__(self, filename, bg=None):
		self.spritesheet = {}
		self.bg = bg
		for key, filename in filename.items():
			self.spritesheets[key] = pg.image.load(filename).convert()
  

	def get_image(self, key, frame, scale=None, flip=False):
		spritesheet = self.spritesheets.get(key)
		if spritesheet is None:
			return None

		image = spritesheet.subsurface(pg.Rect(frame))
		
		if scale is not None:
			image = pg.transform.scale(image, (frame[2]*scale, frame[3]*scale))

		if flip:
			image = pg.transform.flip(image, True, False)

		if self.bg is not None:
			image.set_colorkey(self.bg)

		return image

	def get_animation(self, key, coords, frame_duration, mode, resize=None, flip=None):
		# extract images & create animation
		frames = [self.get_image(key, frame, resize, flip) for frame in coords]
		return Animation(frames, frame_duration, mode)


class Animation:

	class PlayMode(Enum):
		NORMAL = 1,
		LOOP = 2

	def __init__(self, frames, frame_duration, mode):
		# animation settings
		self.frames = frames
		self.frame_duration = frame_duration
		self.animation_duration = len(self.frames)*self.frame_duration
		self.mode = mode

	def get_frame(self, state_time):
		frame_number = self.get_frame_index(state_time);
		return self.frames[frame_number];

	def get_frame_index(self, state_time):
		if len(self.frames) == 1:
			return 0;

		frame_number = int(state_time/self.frame_duration)

		if self.mode == self.PlayMode.NORMAL:
			frame_number = min(len(self.frames) - 1, frame_number)
		elif self.mode == self.PlayMode.LOOP:
			frame_number = frame_number % len(self.frames)

		return frame_number

	def is_animation_finished(self, state_time):
		frame_number = int(state_time/self.frame_duration)
		return len(self.frames) - 1 < frame_number

