from lib.classes.object import Object
from lib.game import game
from lib.functions import *

class Gui(Object):
	def step(self):
		super().step()
		draw_text_gui("FPS_real: " + str(game.fps_real), 0, 0)
		draw_text_gui("Instance_number: " + str(len(game.objects)), 0, 16)
