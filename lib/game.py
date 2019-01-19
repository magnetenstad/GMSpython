import os
import time
import pygame

from lib.assets import get_assets


class Game():
    def __init__(self):
        pygame.init()
        self.display_size = (480, 270)
        self.application_surface = pygame.display.set_mode(self.display_size)
        self.assets = get_assets(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../assets"))
        self.fps_max = 60
        self.fps_real = None
        self.step_count = 0
        self.font = pygame.font.SysFont("monospace", 12)
        self.object_list = []
        self.key = pygame.key.get_pressed()
        self.camera = None

    def init(self):
        from lib.camera import Camera
        self.camera = Camera(self.display_size, 0, 0)

    def run(self):
        while True:
            self.step()

    def step(self):
        time_begin = time.time()

        self.application_surface.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        self.key = pygame.key.get_pressed()

        for i in self.object_list:
            i.step()

        self.draw_text("FPS_real: " + str(self.fps_real), 0, 0)

        pygame.display.update()

        self.step_count += 1

        t = time.time()
        time.sleep(max(time_begin + 1 / self.fps_max - t, 0))
        self.fps_real = int((max(t - time_begin, 10 ** -10)) ** -1)

    def rect_from_sprite(self, instance, sprite_index):
        return self.application_surface.blit(self.assets[sprite_index][0], (instance.rect.x, instance.rect.y))

    def draw_text(self, string, x, y):
        self.application_surface.blit(self.font.render(string, False, (255, 255, 255)),
                                      (x - self.camera.x, y - self.camera.y))

    def draw_sprite(self, sprite_index, image_index, x, y):
        self.application_surface.blit(self.assets[sprite_index][int(image_index)],
                                      (x - self.camera.x, y - self.camera.y))

    def draw_instance(self, instance):
        return self.draw_sprite(instance.sprite_index, instance.image_index, instance.rect.x, instance.rect.y)


game = Game()
