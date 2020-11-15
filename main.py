
from lib.game import game
from lib.functions import *
from src.wall import Wall
from src.player import Player
from src.gui import Gui
from lib.classes.emitter import Emitter
from lib.room import Room

def main():
	game.init()

	gui = Gui(0, 0)
	player = Player(100, 100)

	for i in range(100):
		Wall(48 + i * 16, 132)

	Room("rm_other", 1920, 1080)

	room_goto("rm_other")

	player = Player(100, 100)
	
	for i in range(10):
		Wall(48 + i * 16, 132)
		Wall(48 + i * 16, 168)

	room_goto("rm_main")
	game.camera.follow(player)
	
	game.run()

if __name__ == '__main__':
	main()
