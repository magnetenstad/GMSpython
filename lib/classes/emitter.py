from lib.classes.object import Object
from lib.game import game
from random import uniform
from math import cos, pi, sin

class Emitter(Object):
	def __init__(self, x, y, emission):
		super().__init__(x, y)
		self.emission = emission
		self.collide = False
		self.wait = 60
		self.radius = 32

	def step(self):
		super().step()
		if game.step_count % self.wait == 0:
			direction = uniform(0, 2*pi)
			self.emission(self.rect.x + self.radius * cos(direction), self.rect.y - self.radius * sin(direction))
