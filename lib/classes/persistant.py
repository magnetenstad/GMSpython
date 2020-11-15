import pygame

from lib.game import game
from lib.functions import *

class Persistant():
	def __init__(self, x, y):
		game.persistants.append(self)
		self.create()
	
	def create(self):
		pass
	
	def step(self):
		pass
	
	def destroy(self):
		game.persistants.remove(self)
		del self
