"""config.py
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
INITIAL_FPS = 8
MAX_FPS = 20
APPLES_PER_LEVEL = 5
SPEED_BOOST_PER_LEVEL = 3

# Movement directions by (X, Y)
UP = (0, -CELL_SIZE)
DOWN = (0, CELL_SIZE)
LEFT = (-CELL_SIZE, 0)
RIGHT = (CELL_SIZE, 0)

# ==========================================
# AI & Q-Learning Settings
# ==========================================

# Actions: up ,right or left, 3 possible actions  over all
NUM_ACTIONS = 3

# Episodes & Limits
NUM_EPISODES = 10000
MAX_STEPS_PER_EPISODE = 100

# Q-Learning Hyperparameters
LEARNING_RATE = 0.1  #  (Alpha)
DISCOUNT_RATE = 0.99  #  (Gamma)

# Exploration (Epsilon-Greedy)
EXPLORATION_RATE = 1.0
MAX_EXPLORATION_RATE = 1.0
MIN_EXPLORATION_RATE = 0.01
EXPLORATION_DECAY_RATE = 0.01

# Rewards
REWARD_EAT_APPLE = 10
REWARD_GAME_OVER = -10
REWARD_STEP = -0.1

TRAIN_FPS = 0