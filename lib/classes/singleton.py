import pygame

from lib.game import game
from lib.functions import *

class Singleton():
	def __init__(self, x, y):
		game.singletons.append(self)
		self.create()
	
	def create(self):
		pass
	
	def step(self):
		pass
	
	def destroy(self):
		game.singletons.remove(self)
		del self
