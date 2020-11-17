import pygame

from lib.game import game
from lib.functions import *

class Object():
	def __init__(self, x, y):
		self.sprite_index = None
		self.image_index = 0
		self.image_speed = 0
		self.image_xscale = 1
		self.image_yscale = 1
		self.depth = 0
		self.rect = pygame.Rect((x, y), (0, 0))
		self.solid = False
		self.tags = set()
		self.visible = True
		game.objects.append(self)
		self.create()
	
	def create(self):
		pass
	
	def tag_add(self, tag):
		self.tags.add(tag)

	def tag_remove(self, tag):
		self.tags.discard(tag)

	def draw_self(self):
		if self.sprite_index != None and game.camera.x - self.rect.width <= self.rect.x <= game.camera.x + game.camera.width and game.camera.y - self.rect.height <= self.rect.y <= game.camera.y + game.camera.y + game.camera.width:
			draw_instance(self)

	def step(self):
		if self.sprite_index != None:
			self.image_index += self.image_speed
			self.image_index *= self.image_index < len(game.assets[self.sprite_index])
		if self.visible:
			self.draw_self()

	def destroy(self):
		game.objects.remove(self)
		del self
