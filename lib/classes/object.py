import pygame

from lib.game import game


class Object():
    def __init__(self, x, y):
        self.sprite_index = None
        self.image_index = 0
        self.image_speed = 0
        self.depth = 0
        self.rect = pygame.Rect((x, y), (0, 0))
        self.solid = False
        self.tags = set()
        game.object_list.append(self)

    def add_tag(self, tag):
        self.tags.add(tag)

    def remove_tag(self, tag):
        self.tags.discard(tag)

    def draw(self):
        if self.sprite_index != None:
            self.image_index += self.image_speed
            self.image_index *= self.image_index < len(game.assets[self.sprite_index])
            game.draw_instance(self)

    def step(self):
        self.draw()

    def destroy(self):
        game.object_list.remove(self)
        del self
