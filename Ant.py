import pygame
import numpy as np
import math
import random
from Constants import *
from Pheromone import Pheromone
from Trail import Trail


class Ant:
	def __init__(self, anthill, x, y):
		# Pos and mov
		self.anthill = anthill
		self.x = x
		self.y = y
		self.angle_dir = random.randint(0, 360)
		self.angle_acc = 0
		# Nature
		self.max_hp = ANT_LIFESPAN + random.randint(-ANT_RANGE_LIFESPAN, ANT_RANGE_LIFESPAN)
		self.hp = self.max_hp
		self.has_food = False
		self.trail = Trail()
		self.phrt = PHEROMONE_RELEASE_TIMESPAN

	def __loose_hp(self, dt):
		self.hp -= dt * 1
		if self.hp < 0:
			self.hp = 0

	def __release_pheromone(self, dt):
		self.phrt -= dt * 1
		if self.phrt <= 0:
			self.phrt = PHEROMONE_RELEASE_TIMESPAN
			self.trail.add_pheromone(self.x, self.y)

	def __move(self, dt, pheromones):
		# Change direction
		self.__change_direction(pheromones)
		# Move the ant
		dir_x = math.cos(self.angle_dir * math.pi / 180) * ANT_SPEED
		dir_y = math.sin(self.angle_dir * math.pi / 180) * ANT_SPEED
		self.x += dt * dir_x
		self.y += dt * dir_y
		# Check walls
		self.__check_walls()

	def __get_influenced(self, target_x, target_y, steering):
		a = np.array([target_x, target_y])
		b = np.array([self.x, self.y])
		vector = (a - b) / np.linalg.norm(a - b)
		target_angle = np.arctan2(vector[1], vector[0]) * 180 / math.pi
		delta = target_angle - self.angle_dir
		if delta > 180:
			delta -= 360
		elif delta < -180:
			delta += 360
		steering = abs(steering)
		if delta < 0:
			steering *= -1
		return steering

	def __find_nearest_pheromone(self, pheromones):
		nearest = pheromones[0]
		for pheromone in pheromones:
			dist1 = math.dist((self.x, self.y), (nearest.x, nearest.y))
			dist2 = math.dist((self.x, self.y), (pheromone.x, pheromone.y))
			if dist1 > dist2:
				nearest = pheromone
		return nearest

	def __change_direction(self, pheromones):
		steering = random.uniform(-STEERING_FACTOR, STEERING_FACTOR)
		steering *= random.choice([1] + [0 for _ in range(STEERING_RATE-1)])
		# Get influenced
		# TODO: get influenced by pheromones
		if self.has_food:
			steering = self.__get_influenced(self.anthill.x, self.anthill.y, steering)
		elif len(pheromones) > 0:
			nearest_ph = self.__find_nearest_pheromone(pheromones)
			steering = self.__get_influenced(nearest_ph.x, nearest_ph.y, steering)
		# Steering
		self.angle_acc += steering
		if self.angle_acc > STEERING_THRESHOLD:
			self.angle_acc = STEERING_THRESHOLD
		elif self.angle_acc < -STEERING_THRESHOLD:
			self.angle_acc = -STEERING_THRESHOLD
		self.angle_dir = (self.angle_dir + self.angle_acc) % 360

	def __check_walls(self):
		# Check x
		if self.x < 0:
			self.x = 0
		elif self.x+ANT_SIZE > SCREEN_WIDTH:
			self.x = SCREEN_WIDTH-ANT_SIZE
		# Check y
		if self.y < 0:
			self.y = 0
		elif self.y+ANT_SIZE > SCREEN_HEIGHT:
			self.y = SCREEN_HEIGHT-ANT_SIZE

	def __check_collision_with_food(self, foodsets):
		for foodset in foodsets:
			for food in foodset.foods:
				cent_x, cent_y = self.x + ANT_SIZE / 2, self.y + ANT_SIZE / 2
				dist = math.dist((cent_x, cent_y), (food.x, food.y))
				if dist <= FOOD_RADIUS:
					self.__eat()
					foodset.foods.remove(food)

	def __check_collision_with_anthill(self):
		cent_x, cent_y = self.x+ANT_SIZE/2, self.y+ANT_SIZE/2
		dist = math.dist((cent_x, cent_y), (self.anthill.x, self.anthill.y))
		if dist <= ANTHILL_RADIUS and self.has_food:
			self.anthill.spawn_ant()
			self.__detach()

	def __check_collision_with_pheromone(self, pheromones):
		for pheromone in pheromones:
			dist = math.dist((self.x, self.y), (pheromone.x, pheromone.y))
			if dist <= 1:
				pheromone.effect = 0

	def __eat(self):
		self.hp = self.max_hp
		self.trail.reset()
		self.has_food = True

	def __detach(self):
		self.has_food = False

	def update(self, dt, pheromones, foodsets):
		self.__move(dt, pheromones)
		self.__loose_hp(dt)
		self.__check_collision_with_food(foodsets)
		self.__check_collision_with_anthill()
		if self.has_food:
			self.__release_pheromone(dt)
		else:
			self.__check_collision_with_pheromone(pheromones)
		self.trail.update(dt)

	def draw(self, screen):
		# print(tuple(np.array(ANT_COLOR)*(self.hp/self.max_hp)))
		pygame.draw.rect(screen, tuple(np.array(ANT_COLOR)*(self.hp/self.max_hp)), (self.x, self.y, ANT_SIZE, ANT_SIZE))
		self.trail.draw(screen)
