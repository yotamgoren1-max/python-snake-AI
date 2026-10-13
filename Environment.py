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