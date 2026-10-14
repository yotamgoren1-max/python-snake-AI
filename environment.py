"""
environment.py
Wraps the Snake game into a Reinforcement Learning environment.
Manages game state, physics, rewards, and rendering.
"""

import pygame
import config
import game_objects
import agent


class SnakeEnv:
    """
    Manages the game environment, handling resets, step execution, and display logic.
    """

    def __init__(self, render_mode=True):
        """
        Initializes game settings, tracking variables, and sets up Pygame if rendering is enabled.
        """
        self.render_mode = render_mode
        self.score = 0
        self.steps = 0
        self.snake = None
        self.apple = None

        if self.render_mode:
            pygame.init()  # starting the pygame Tools
            self.screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))  # creates the monitor
            pygame.display.set_caption("python-Snake-Game-AI")
            self.clock = pygame.time.Clock()  # creating the clock
            self.score_font = pygame.font.Font(None, 36)  # creating the basic class for a text
            self.grid_surface = pygame.Surface((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))  # creating the basic grid screen
            game_objects.basic_screen(self.grid_surface)
        else:
            self.screen = None
            self.clock = None
            self.score_font = None
            self.grid_surface = None

    def reset(self):
        """
        Resets the game state by creating a new snake and apple, and resetting scores.
        Returns the initial state tuple for the agent to start playing.
        """
        self.score = 0
        self.steps = 0
        self.snake = game_objects.Snake()
        self.apple = game_objects.Apple()
        curr_state = agent.get_state(self.snake, self.apple)
        return curr_state

    def render(self):
        """
        Draws the game state (grid, snake, apple, and score) onto the screen
        and regulates the frame rate using the clock.
        """
        if not self.render_mode:
            return
        else:
            self.screen.blit(self.grid_surface, (0, 0))
            self.snake.draw(self.screen)
            self.apple.draw_apple(self.screen)
            str_score = "score: " + str(self.score)
            score_surface = self.score_font.render(str_score, True, config.WHITE)
            self.screen.blit(score_surface, (20, 20))
            pygame.display.update()
            self.clock.tick(config.TRAIN_FPS)

    def step(self, action):
        """
        Executes one step in the environment based on the agent's action.
        Returns: (next_state, reward, done, score)
        """
        # 1. Track steps to prevent infinite loops
        self.steps += 1

        # 2. Allow graceful window exit if rendering is on
        if self.render_mode:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        # 3. Update snake direction based on the relative action
        self.snake.direction = agent.get_next_direction(self.snake.direction, action)

        # 4. Move the snake one step forward
        self.snake.move()

        # 5. Check for game-ending conditions (walls, self-collision, or timeout)
        hit_wall = self.snake.check_wall_collision()
        hit_body = self.snake.check_self_collision()
        timeout = self.steps > 100 * len(self.snake.body)

        if hit_wall or hit_body or timeout:
            done = True
            reward = config.REWARD_GAME_OVER
            next_state = agent.get_state(self.snake, self.apple)
            return next_state, reward, done, self.score

        # 6. Check for apple collision and handle eating
        if self.snake.check_apple_collision(self.apple):
            self.score += 1
            self.steps = 0
            reward = config.REWARD_EAT_APPLE
            self.snake.grow()
            self.apple.Random_Apple()
        else:
            reward = config.REWARD_STEP

        done = False

        # 7. Render frame if rendering mode is active
        self.render()

        # 8. Extract the new state after movement
        next_state = agent.get_state(self.snake, self.apple)

        return next_state, reward, done, self.score





















