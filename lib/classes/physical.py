from lib.classes.object import Object
from lib.functions import instance_place
from lib.game import game


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
		self.collide = True

	def step(self):
		super().step()

		self.speed_y += self.gravity

		if abs(self.speed_x) < self.acceleration:
			self.speed_x = 0

		self.speed_x *= self.damping
		
		if self.gravity == 0:
			self.speed_y *= self.damping

		if self.collide:
			meeting = instance_place(self, self.rect.x + round(self.speed_x), self.rect.y, game.solids)
			if meeting:
				if self.speed_x > 0:
					self.rect.right = meeting.rect.left
				elif self.speed_x < 0:
					self.rect.left = meeting.rect.right
				self.speed_x = 0
			else:
				self.rect.x += round(self.speed_x)

			meeting = instance_place(self, self.rect.x, self.rect.y + round(self.speed_y), game.solids)
			if meeting:
				if self.speed_y > 0:
					self.rect.bottom = meeting.rect.top
				elif self.speed_y < 0:
					self.rect.top = meeting.rect.bottom
				self.speed_y *= meeting.bounce
			else:
				self.rect.y += round(self.speed_y)
		else:
			self.rect.x += round(self.speed_x)
			self.rect.y += round(self.speed_y)
