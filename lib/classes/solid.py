from lib.classes.physical import Physical


class Solid(Physical):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.add_tag('solid')
        self.gravity = 0
