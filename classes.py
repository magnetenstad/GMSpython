import pygame
import os
import time

from functions import *

class Game():
    def __init__(self):
        self.step_count = 0
        self.object_list = []
        self.fps_max = 60
        self.display_size = (480, 270)
        self.application_surface = pygame.display.set_mode(self.display_size)
        self.assets = get_assets(os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets"))

    def step(self):
        time_begin = time.time()

        game.application_surface.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        global key
        key = pygame.key.get_pressed()

        for i in self.object_list:
            i.step()

        pygame.display.update()

        time.sleep(max(time_begin + 1/self.fps_max - time.time(), 0))

        self.step_count += 1

    def rect_from_sprite(self, instance, sprite_index):
        return self.application_surface.blit(self.assets[sprite_index][0], (instance.rect.x, instance.rect.y))

class Object():
    def __init__(self, x, y):
        self.sprite_index = None
        self.rect = None
        self.image_index = 0
        self.image_speed = 0
        self.depth = 0
        self.rect = pygame.Rect((x, y), (0, 0))
        self.solid = False
        game.object_list.append(self)

    def draw(self):
        if self.sprite_index != None:
            self.image_index += self.image_speed
            self.image_index *= self.image_index < len(game.assets[self.sprite_index])
            game.application_surface.blit(game.assets[self.sprite_index][int(self.image_index)], (self.rect.x, self.rect.y))

    def step(self):
        self.draw()

class Physical(Object):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed_x = 0
        self.speed_y = 0
        self.speed_jump = -6
        self.acceleration = 0.3
        self.damping = 0.9
        self.gravity = 0.2
        self.bounce = 0

    def step(self):
        super().step()

        self.speed_y += self.gravity

        if abs(self.speed_x) < self.acceleration:
            self.speed_x = 0
        self.speed_x *= self.damping
        if self.gravity == 0:
            self.speed_y *= self.damping

        meeting = instance_place(self, self.rect.x + round(self.speed_x), self.rect.y, instance_find(game.object_list, "solid", True))
        if meeting:
            if self.speed_x > 0:
                self.rect.right = meeting.rect.left
            elif self.speed_x < 0:
                self.rect.left = meeting.rect.right
            self.speed_x = 0
        else:
            self.rect.x += round(self.speed_x)

        meeting = instance_place(self, self.rect.x, self.rect.y + round(self.speed_y), instance_find(game.object_list, "solid", True))
        if meeting:
            if self.speed_y > 0:
                self.rect.bottom = meeting.rect.top
            elif self.speed_y < 0:
                self.rect.top = meeting.rect.bottom
            self.speed_y *= meeting.bounce
        else:
            self.rect.y += round(self.speed_y)

class Player(Physical):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite_index = "panda_run.gif"
        self.rect = game.rect_from_sprite(self, "panda_run.gif")
        self.image_speed = 0.2

    def step(self):
        super().step()

        if key[pygame.K_LEFT]:
            self.speed_x -= self.acceleration
        if key[pygame.K_RIGHT]:
            self.speed_x += self.acceleration
        if key[pygame.K_UP]:
            self.speed_y = self.speed_jump

class Solid(Physical):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.solid = True
        self.gravity = 0

class Wall(Solid):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite_index = "wall.png"
        self.rect = game.rect_from_sprite(self, "wall.png")

game = Game()
