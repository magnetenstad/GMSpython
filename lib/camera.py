from lib.classes.persistant import Persistant
from lib.functions import instance_find_tag


class Camera(Persistant):
	def __init__(self, display_size, x, y):
		super().__init__(x, y)
		self.x = 0
		self.y = 0
		self.width = display_size[0]
		self.height = display_size[1]
		self.target = None

	def follow(self, instance):
		self.target = instance

	def step(self):
		if not self.target is None:
			target_x = self.target.rect.x - self.width / 2
			target_y = self.target.rect.y - self.height / 2
			self.x += (target_x - self.x) / 10
			self.y += (target_y - self.y) / 10
			