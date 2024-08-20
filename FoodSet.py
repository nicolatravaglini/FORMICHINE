import random
from Food import Food
from Constants import *


class FoodSet:
	def __init__(self, x, y, num_foods):
		self.x = x
		self.y = y
		self.num_foods = num_foods
		self.foods = []
		self.__build()

	def __build(self):
		for i in range(self.num_foods):
			x, y = random.randint(self.x-FOODSET_RADIUS, self.x+FOODSET_RADIUS), random.randint(self.y-FOODSET_RADIUS, self.y+FOODSET_RADIUS)
			self.foods.append(Food(x, y))

	def __reset(self):
		self.x = random.randint(0+FOODSET_RADIUS, SCREEN_WIDTH-FOODSET_RADIUS)
		self.y = random.randint(0+FOODSET_RADIUS, SCREEN_WIDTH-FOODSET_RADIUS)
		self.__build()

	def update(self, dt):
		if len(self.foods) == 0:
			self.__reset()

	def draw(self, screen):
		for food in self.foods:
			food.draw(screen)
