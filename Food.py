import pygame
from Constants import *


class Food:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def draw(self, screen):
		pygame.draw.circle(screen, FOOD_COLOR, (self.x, self.y), FOOD_RADIUS)
