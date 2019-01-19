from lib.classes.physical import Physical
from lib.game import game


class Particle(Physical):
    def __init__(self, x, y, duration, speed_x, speed_y):
        super().__init__(x, y)
        self.duration = duration
        self.step_created = game.step_count
        self.sprite_index = "wall.png"

    def step(self):
        super().step()
        if game.step_count >= self.step_created + self.duration:
            self.destroy()
