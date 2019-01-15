import pygame
import os
import time

class Game():

    def __init__(self):
        self.step_count = 0
        self.object_list = []
        self.path_main = os.path.dirname(os.path.realpath(__file__))
        self.path_assets = os.path.join(self.path_main, "assets")
        self.fps_max = 60
        self.display_size = (480, 270)
        self.application_surface = pygame.display.set_mode(self.display_size)

    def step(self):
        time_begin = time.time()

        game.application_surface.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()


        for i in self.object_list:
            i.step()

        pygame.display.update()

        time.sleep(max(time_begin + 1/self.fps_max - time.time(), 0))

        self.step_count += 1

class Object():

    def __init__(self, x, y):
        self.sprite_index = -1
        self.mask_index = None
        self.image_index = 0
        self.image_speed = 0
        self.depth = 0
        self.rect = pygame.Rect((x, y), (0, 0))
        game.object_list.append(self)

    def draw(self):
        if self.sprite_index != -1:
            self.image_index += self.image_speed
            self.image_index *= self.image_index < len(self.sprite_index)
            game.application_surface.blit(game.assets[self.sprite_index][self.image_index], (self.rect.x, self.rect.y))

    def step(self):
        self.draw()

class Player(Object):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite_index = "player.png"
        self.mask_index = game.application_surface.blit(game.assets[self.sprite_index][self.image_index], (self.rect.x, self.rect.y))

game = Game()
