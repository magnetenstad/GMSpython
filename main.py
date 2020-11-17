
from lib.game import game
from lib.functions import *
from src.wall import Wall
from src.player import Player
from src.gui import Gui
from lib.classes.emitter import Emitter
from lib.classes.room import Room

def main():
	game.init()

	Gui(0, 0)
	player = Player(100, 100)

	for i in range(100):
		for j in range(10):
			Wall(48 + i * 16, 132 + j * 16)

	game.camera.follow(player)
	
	game.run()

if __name__ == '__main__':
	main()
