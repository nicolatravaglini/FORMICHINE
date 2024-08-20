import pygame.draw
from Constants import *


class Obstacle:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def draw(self, screen):
		pygame.draw.rect(screen, OBSTACLE_COLOR, (self.x, self.y, OBSTACLE_SIZE, OBSTACLE_SIZE))
