"""
config.py
Contains all the constant variables and settings for the Snake Game.
Separating these values makes the game easy to balance and modify.
"""

# Colors settings (RGB)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Screen settings
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
CELL_SIZE = 20  # Set the pixel size for each grid cell

# Clock and difficulty settings
# For every APPLES_PER_LEVEL eaten, the game speed increases by SPEED_BOOST_PER_LEVEL
INITIAL_FPS = 8
MAX_FPS = 20
APPLES_PER_LEVEL = 5
SPEED_BOOST_PER_LEVEL = 3

# Movement directions by (X, Y)
UP = (0, -CELL_SIZE)
DOWN = (0, CELL_SIZE)
LEFT = (-CELL_SIZE, 0)
RIGHT = (CELL_SIZE, 0)