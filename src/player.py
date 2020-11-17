from lib.classes import room
import pygame
import random

from lib.classes.particle import Particle
from lib.classes.physical import Physical
from lib.game import game
from lib.functions import *

class Player(Physical):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.sprite_index = "panda_run.gif"
		self.rect = rect_from_sprite(self, "panda_run.gif")
		self.image_speed = 0.2

	def step(self):
		super().step()

		if keyboard_check(ord('a')):
			self.speed_x -= self.acceleration
		if keyboard_check(ord('d')):
			self.speed_x += self.acceleration
		if keyboard_check_pressed(ord('w')):
			self.speed_y = self.speed_jump

		self.image_speed = 0.2 * (self.speed_x != 0)

		if self.speed_x > 0:
			self.image_xscale = 1
		elif self.speed_x < 0:
			self.image_xscale = -1
