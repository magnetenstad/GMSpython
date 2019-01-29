from lib.classes.object import Object
from lib.functions import instance_find_tag


class Camera(Object):
    def __init__(self, display_size, x, y):
        super().__init__(x, y)
        self.x = 0
        self.y = 0
        self.target_x = self.x
        self.target_y = self.y
        self.width = display_size[0]
        self.height = display_size[1]
        self.follow_tag = None
        self.follow_instance = None
        self.follow_search_interval = 30
        self.follow_search_counter = 0

    def follow(self, tag):
        self.follow_tag = tag
        self.search_for_target()

    def search_for_target(self):
        self.follow_search_counter = 0
        instances = instance_find_tag(self.follow_tag)
        self.follow_instance = instances[0] if instances else None

    def step(self):
        self.follow_search_counter += 1
        if self.follow_search_counter >= self.follow_search_interval:
            self.search_for_target()

        if not self.follow_instance is None:
            self.target_x = self.follow_instance.rect.x - self.width / 2
            self.target_y = self.follow_instance.rect.y - self.height / 2
            self.x += (self.target_x - self.x) / 10
            self.y += (self.target_y - self.y) / 10
