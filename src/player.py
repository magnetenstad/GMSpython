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
        if game.key[pygame.K_LEFT]:
            self.speed_x -= self.acceleration
        if game.key[pygame.K_RIGHT]:
            self.speed_x += self.acceleration
        if game.key[pygame.K_UP]:
            self.speed_y = self.speed_jump
        if game.key[pygame.K_DOWN]:
            for _ in range(10):
                Particle(self.rect.x, self.rect.y, 600, random.randint(-10, 10), random.randint(-10, 10))
