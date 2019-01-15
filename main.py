# -*- coding: utf-8 -*-

import pygame

from functions import *
from classes import *

pygame.init()
pygame.display.init()
pygame.mixer.init()

player = Player(100, 100)

for i in range(10):
    Wall(48 + i*16, 132)

while True:
    game.step()
