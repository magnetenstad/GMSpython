# -*- coding: utf-8 -*-

import pygame
import os
import time

class Game():
    
    def __init__(self):
        self.step_count = 0
        self.object_list = []
        self.path_main = os.path.dirname(os.path.realpath(__file__))
        self.path_asset = os.path.join(self.path_main, "assets")
        self.fps_max = 60
        self.display_size = (480, 270)
        self.display = pygame.display.set_mode(self.display_size)
        
    def step(self):
        self.time_begin = time.time()
        
        game.display.fill((0, 0, 0))
        
        for i in self.object_list:
            i.step()
        
        pygame.display.update()
        
        time.sleep(max(self.time_begin + 1/self.fps_max - time.time(), 0))
        
        self.step_count += 1
        
    def file_load(self, file, path):
        return os.path.join(path, file)
        
    def image_load(self, file):
        return pygame.image.load(self.file_load(file, self.path_asset))
    
    def sound_load(self, file):
        return pygame.mixer.Sound(self.file_load(file, self.path_asset))

class Object():
    
    def __init__(self):
        self.sprite_index = []
        self.mask_index = None
        self.image_index = 0
        self.image_speed = 0
        self.depth = 0
        game.object_list.append(self)
    
    def draw(self):
        pass
        
    def step(self):
        pass


class Rectangle(Object):
    
    def __init__(self):
        super().__init__()
        self.sprite_index = game.image_load("player.png")
        pass

    def step(self):
        super().step()
        game.display.blit(self.sprite_index, (100, 100))
    


pygame.init()
pygame.display.init()

game = Game()

Rectangle()

while True:
    game.step()
    













