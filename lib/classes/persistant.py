import pygame

from lib.game import game
from lib.functions import *

class Persistant():
	def __init__(self, x, y):
		game.persistant.append(self)
		self.create()
	
	def create(self):
		pass
	
	def step(self):
		pass
	
	def destroy(self):
		game.persistant.remove(self)
		del self
