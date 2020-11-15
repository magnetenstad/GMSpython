
from lib.game import game
from lib.functions import *
from src.wall import Wall
from src.player import Player
from src.gui import Gui
from lib.classes.emitter import Emitter

def main():
	game.init()

	gui = Gui(0, 0)
	player = Player(100, 100)
	game.camera.follow(player)

	for i in range(100):
		Wall(48 + i * 16, 132)

	game.run()

if __name__ == '__main__':
	main()
