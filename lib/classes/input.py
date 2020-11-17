import pygame

from lib.classes.persistant import Persistant

class Input(Persistant):
	def __init__(self):
		super().__init__(0, 0)
		self.key = set()
		self.key_pressed = set()
		self.key_released = set()

	def step(self):
		self.key_pressed.clear()
		self.key_released.clear()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.KEYDOWN:
				self.key_pressed.add(event.key)
				self.key.add(event.key)
			if event.type == pygame.KEYUP:
				self.key_released.add(event.key)
				if event.key in self.key:
					self.key.remove(event.key)
	
	def clear(self):
		self.key.clear()
		self.key_pressed.clear()
		self.key_released.clear()
	