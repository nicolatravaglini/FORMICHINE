from Ant import Ant
from Constants import *


class Anthill:
	def __init__(self, x, y, num_ants):
		self.x = x
		self.y = y
		self.num_ants = num_ants
		self.ants = []
		self.__build()

	def __build(self):
		for i in range(self.num_ants):
			self.spawn_ant()

	def spawn_ant(self):
		self.ants.append(Ant(self, self.x, self.y))

	def __check_hps(self):
		for ant in self.ants:
			if ant.hp <= 0:
				self.ants.remove(ant)

	def update(self, dt, foodsets):
		for ant in self.ants:
			ant.update(dt, foodsets)
		self.__check_hps()

	def draw(self, screen):
		pygame.draw.circle(screen, ANTHILL_COLOR, (self.x, self.y), ANTHILL_RADIUS)
		for ant in self.ants:
			ant.draw(screen)
