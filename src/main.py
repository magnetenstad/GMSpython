# -*- coding: utf-8 -*-

from lib.game import game
from src.wall import Wall
from src.player import Player


def main():
    game.init()

    player = Player(100, 100)
    game.camera.follow(player)

    for i in range(100):
        Wall(48 + i * 16, 132)

    game.run()


if __name__ == '__main__':
    main()
