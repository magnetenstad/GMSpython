from lib.classes.object import Object
from lib.game import game
from random import uniform
from math import cos, pi, sin

class Emitter(Object):
	def __init__(self, x, y, Emission):
		super().__init__(x, y)
		self.Emission = Emission
		self.collide = False
		self.wait = 60
		self.radius = 32

	def step(self):
		super().step()
		if game.step_count % self.wait == 0:
			_dir = uniform(0, 2*pi)
			_x = self.rect.x + self.radius * cos(_dir)
			_y = self.rect.y - self.radius * sin(_dir)
			self.Emission(_x, _y)
