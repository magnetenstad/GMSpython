from lib.classes.physical import Physical


class Solid(Physical):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.tag_add('solid')
		self.gravity = 0
