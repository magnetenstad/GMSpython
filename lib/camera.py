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

    def follow(self, tag):
        self.follow_tag = tag

    def step(self):
        if not self.follow_tag is None:
            instance = instance_find_tag(self.follow_tag)
            if instance:
                self.target_x = instance[0].rect.x - self.width / 2
                self.target_y = instance[0].rect.y - self.height / 2
                self.x += (self.target_x - self.x) / 10
                self.y += (self.target_y - self.y) / 10
