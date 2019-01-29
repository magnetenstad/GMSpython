from lib.classes.object import Object
from lib.functions import instance_find_tag


class Camera(Object):
    def __init__(self, display_size, x, y):
        super().__init__(x, y)
        self.x = 0
        self.y = 0
        self.width = display_size[0]
        self.height = display_size[1]
        self.follow_instance = None

    def follow(self, instance):
        self.follow_instance = instance

    def step(self):
        if not self.follow_instance is None:
            target_x = self.follow_instance.rect.x - self.width / 2
            target_y = self.follow_instance.rect.y - self.height / 2
            self.x += (target_x - self.x) / 10
            self.y += (target_y - self.y) / 10
