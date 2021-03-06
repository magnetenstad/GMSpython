import os
import time
import pygame

from lib.assets import get_assets

class Game():
	def __init__(self):
		pygame.init()
		self.display_size = (480, 270)
		self.application_surface = pygame.display.set_mode(self.display_size)
		self.assets = get_assets(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../assets"))
		self.fps_max = 60
		self.fps_real = None
		self.step_count = 0
		self.font = pygame.font.SysFont("monospace", 12)
		self.objects = []
		self.camera = None
		self.solids = []
		self.rooms = {}
		self.room_index = ""
		self.persistants = []

	def init(self):
		from lib.classes.camera import Camera
		from lib.classes.input import Input
		from lib.classes.room import Room

		self.camera = Camera(self.display_size, 0, 0)
		self.input = Input()
		Room("rm_main", self.display_size[0], self.display_size[1])
		self.room_index = "rm_main"

	def run(self):
		while True:
			self.step()
	
	def step(self):
		time_begin = time.time()

		self.application_surface.fill((0, 0, 0))

		self.solids = [i for i in game.objects if 'solid' in i.tags]

		for i in self.persistants:
			i.step()

		for i in self.objects:
			i.step()

		pygame.display.update()

		self.step_count += 1

		t = time.time()
		time.sleep(max(time_begin + 1 / self.fps_max - t, 0))
		self.fps_real = int((max(t - time_begin, 10 ** -10)) ** -1)

game = Game()
