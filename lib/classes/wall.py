from lib.classes.solid import Solid
from lib.game import game


class Wall(Solid):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite_index = "wall.png"
        self.rect = game.rect_from_sprite(self, "wall.png")
