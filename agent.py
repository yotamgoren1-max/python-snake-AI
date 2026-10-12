import collections
import random
import config

"""
    Checks if moving one step in a given direction causes a collision with a wall or the snake's body.
    Returns True if the tile is dangerous, and False if it is safe.
    """
def check_danger(curr_head_po, curr_direction, snake):
    # Calculate the next head position based on the direction vector
    next_position = (
        curr_head_po[0] + curr_direction[0],
        curr_head_po[1] + curr_direction[1]
    )
    # Check if the next position is within screen boundaries
    if 0 <= next_position[0] < config.WINDOW_WIDTH and 0 <= next_position[1] < config.WINDOW_HEIGHT:
        # Check if the next position collides with any body segment
        for rect in snake.body:
            if next_position[0] == rect[0] and next_position[1] == rect[1]:
                return True
    else:
        # Hitting a wall is considered a danger
        return True

    return False

"""
    Extracts the current state of the game and returns it as an immutable 11-element tuple.
    The state represents 3 danger checks, 4 movement directions, and 4 relative apple positions.
    """
def get_state(snake, apple):
    curr_state = [0] * 11
    curr_head_po = snake.body[0]
    # List of all directions ordered clockwise
    direction_list = [config.UP, config.RIGHT, config.DOWN, config.LEFT]
    # Check dangers relative to current heading (straight, right, left)
    for i in range(len(direction_list)):
        if snake.direction == direction_list[i]:
            # Danger straight ahead
            if check_danger(curr_head_po, direction_list[i], snake):
                curr_state[0] = 1
            # Danger turning right (next clockwise index)
            if check_danger(curr_head_po, direction_list[(i + 1) % 4], snake):
                curr_state[1] = 1
            # Danger turning left (previous counter-clockwise index)
            if check_danger(curr_head_po, direction_list[(i - 1) % 4], snake):
                curr_state[2] = 1
    # Mark current movement direction (indices 3 to 6)
    for i in range(len(direction_list)):
        if direction_list[i] == snake.direction:
            curr_state[i + 3] = 1
    # Extract coordinates for relative apple positioning
    x_apple = apple.rect[0]
    y_apple = apple.rect[1]
    x_snake = curr_head_po[0]
    y_snake = curr_head_po[1]
    # Check relative position of the apple to the head (indices 7 to 10)
    if y_snake < y_apple:  # Apple is below
        curr_state[7] = 1
    if x_snake < x_apple:  # Apple is to the right
        curr_state[8] = 1
    if y_snake > y_apple:  # Apple is above
        curr_state[9] = 1
    if x_snake > x_apple:  # Apple is to the left
        curr_state[10] = 1
    # Return as tuple so it can be hashed as a dictionary key
    return tuple(curr_state)

"""
    Represents the Q-Learning AI agent handling decision-making and memory (Q-Table).
    """
class Agent:
    """
    Initializes an empty Q-Table and the starting exploration parameters.
    """
    def __init__(self):
        # Automatically creates a [0.0, 0.0, 0.0] entry for any unseen state
        self.Q_table = collections.defaultdict(lambda: [0.0, 0.0, 0.0])
        self.epsilon = config.EXPLORATION_RATE
    """
    Chooses an action (0=straight, 1=right, 2=left) using an epsilon-greedy strategy.
    Balances exploration (random moves) with exploitation (best known moves).
    """
    def choose_action(self, state):
        num = random.random()
        # Exploration: pick a random action to discover new paths
        if num < self.epsilon:
            return random.randint(0, 2)
        else:
            # Exploitation: break ties randomly if all actions have zero reward
            if self.Q_table[state] == [0.0, 0.0, 0.0]:
                return random.randint(0, 2)
            else:
                # Pick the action index with the highest Q-value
                q_values = self.Q_table[state]
                return q_values.index(max(q_values))