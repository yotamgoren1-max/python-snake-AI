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

    def step(self, action):
        """
        Executes one step in the environment given an action.
        Updates the snake's direction, moves the snake, checks for collisions or food consumption,
        updates the display if rendering is active, and returns the step transition tuple.
        """
        self.steps += 1

        # Handle Pygame window events to prevent freezing
        if self.render_mode:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        # Translate relative action (0=straight, 1=right, 2=left) into a direction vector and move
        self.snake.direction = agent.get_next_direction(self.snake.direction, action)
        self.snake.move()

        reward = config.REWARD_STEP
        done = False

        # Check for terminal conditions: wall collision, self-collision, or step limit reached
        if (self.snake.check_wall_collision() or
                self.snake.check_self_collision() or
                self.steps > config.MAX_STEPS_PER_EPISODE):
            done = True
            reward = config.REWARD_GAME_OVER
            next_state = agent.get_state(self.snake, self.apple)
            return next_state, reward, done, self.score

        # Check if snake's head consumed the apple
        head = self.snake.body[0]
        if head.colliderect(self.apple.rect):
            self.score += 1
            reward = config.REWARD_EAT_APPLE
            self.snake.grow()
            self.apple.Random_Apple()
            self.steps = 0  # Reset starvation counter

        # Render current frame if rendering is enabled
        if self.render_mode:
            self.screen.blit(self.grid_surface, (0, 0))
            self.snake.draw(self.screen)
            self.apple.draw_apple(self.screen)
            score_text = self.score_font.render(f"Score: {self.score}", True, config.WHITE)
            self.screen.blit(score_text, (10, 10))
            pygame.display.flip()
            self.clock.tick(config.TRAIN_FPS)

        # Extract next state representation
        next_state = agent.get_state(self.snake, self.apple)

        return next_state, reward, done, self.score
