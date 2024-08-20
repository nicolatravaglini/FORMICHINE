import pygame
import random
from Constants import *
from Anthill import Anthill
from FoodSet import FoodSet
from Obstacle import Obstacle


def build_anthills():
	anthills = []
	for i in range(NUM_ANTHILLS):
		x, y = random.randint(0, SCREEN_WIDTH-ANT_SIZE), random.randint(0, SCREEN_HEIGHT-ANT_SIZE)
		anthills.append(Anthill(x, y, NUM_ANTS_IN_ANTHILL))
	return anthills


def build_foodsets():
	foodsets = []
	for i in range(NUM_FOODSETS):
		x, y = random.randint(0+FOODSET_RADIUS, SCREEN_WIDTH-FOODSET_RADIUS), random.randint(0+FOODSET_RADIUS, SCREEN_HEIGHT-FOODSET_RADIUS)
		foodsets.append(FoodSet(x, y, NUM_FOODS_IN_FOODSET))
	return foodsets


def build_obstacles():
	obstacles = []
	for i in range(NUM_OBSTACLES):
		x, y = random.randint(0, SCREEN_WIDTH-OBSTACLE_SIZE), random.randint(0, SCREEN_HEIGHT-OBSTACLE_SIZE)
		obstacles.append(Obstacle(x, y))
	return obstacles


def draw(screen, anthills, foodsets, obstacles):
	screen.fill(BACKGROUND_COLOR)
	for obstacle in obstacles:
		obstacle.draw(screen)
	for foodset in foodsets:
		foodset.draw(screen)
	for anthill in anthills:
		anthill.draw(screen)
	pygame.display.flip()


def update(screen, clock, anthills, foodsets, obstacles):
	dt = clock.tick(FPS) / 1000
	for anthill in anthills:
		anthill.update(dt, foodsets)
	for foodset in foodsets:
		foodset.update(dt)


def main():
	# Pygame configuration
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('Formichiamo')
	clock = pygame.time.Clock()

	# Simulation configuration
	# TODO: handle collisions
	# TODO: make the classes handle the random spawn
	anthills = build_anthills()
	foodsets = build_foodsets()
	obstacles = build_obstacles()

	# Loop
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		update(screen, clock, anthills, foodsets, obstacles)
		draw(screen, anthills, foodsets, obstacles)

	pygame.quit()


if __name__ == "__main__":
	main()
