import pygame

# Pygame constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 120
BACKGROUND_COLOR = (0, 0, 0)
ANTHILL_COLOR = (255, 255, 120)
ANT_COLOR = (255, 0, 0)
FOOD_COLOR = (0, 255, 0)
OBSTACLE_COLOR = (0, 0, 255)
PHEROMONE_COLOR = (160, 32, 240)

# Simulation constants
NUM_ANTS_IN_ANTHILL = 200
NUM_ANTHILLS = 2
NUM_FOODS_IN_FOODSET = 50
NUM_FOODSETS = 10
NUM_OBSTACLES = 5

ANT_SIZE = 4
ANTHILL_RADIUS = 10
FOODSET_RADIUS = 80
FOOD_RADIUS = 4
OBSTACLE_SIZE = 50

ANT_SPEED = 20
STEERING_RATE = 4      # the ants will steer every STEERING_RATE frames
STEERING_FACTOR = 2
STEERING_THRESHOLD = 5

ANT_LIFESPAN = 30   # in seconds
ANT_RANGE_LIFESPAN = ANT_LIFESPAN/3

PHEROMONE_RELEASE_TIMESPAN = 0.1  # in seconds
PHEROMONE_LIFESPAN = 20     # in seconds
