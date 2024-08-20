import pygame
from Constants import *


class Pheromone:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.effect = PHEROMONE_LIFESPAN

	def activate(self):
		self.effect = PHEROMONE_LIFESPAN

	def loose_lifespan(self, dt):
		self.effect -= dt * 1
