import pygame
import numpy as np
from Pheromone import Pheromone
from Constants import *


class Trail:
	def __init__(self):
		self.trail = []

	def add_pheromone(self, x, y):
		self.trail.append(Pheromone(x, y))

	def reset(self):
		self.trail = []

	def update(self, dt):
		for p in self.trail:
			p.loose_lifespan(dt)
			if p.effect <= 0:
				self.trail.remove(p)

	def draw(self, screen):
		for i in range(len(self.trail)-1):
			pygame.draw.line(screen, tuple(np.array(PHEROMONE_COLOR)*(self.trail[i+1].effect/PHEROMONE_LIFESPAN)), (self.trail[i].x, self.trail[i].y), (self.trail[i+1].x, self.trail[i+1].y))
