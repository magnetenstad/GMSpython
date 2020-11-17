import pygame

from lib.game import game

class Room():
	def __init__(self, name, width, height):
		self.name = name
		self.width = width
		self.height = height
		self.objects = []
		game.rooms[name] = self

	