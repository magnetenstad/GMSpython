from lib.classes.solid import Solid
from lib.game import game
from lib.functions import *

class Wall(Solid):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.collide = False
		self.sprite_index = "wall.png"
		self.rect = rect_from_sprite(self, "wall.png")