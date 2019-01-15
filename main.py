# -*- coding: utf-8 -*-

import pygame
import os
import time
from PIL import Image, ImageSequence

from functions import *
from classes import *

pygame.init()
pygame.display.init()
pygame.mixer.init()

game = Game()
game.assets = get_assets(game.path_assets)
player = Player(100, 100)

while True:
    game.step()
