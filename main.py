"""
main.py
The main entry point for the Snake Game.
Handles the game loop, user input, collision logic, and screen rendering.
"""

import pygame
import config
import game_objects

# --- Initialization ---
pygame.init()  #starting the pygame Tools
screen=pygame.display.set_mode((config.WINDOW_WIDTH,config.WINDOW_HEIGHT)) #creates the monitor
pygame.display.set_caption("python-Snake-Game")
clock=pygame.time.Clock() #creating the clock
score_font=pygame.font.Font(None,36) #creating the basic class for a text

# --- Game Variables ---
running=True
game_started = False
curr_score=0 #number of apples

# Create the background grid surface once
grid_surface=pygame.Surface((config.WINDOW_WIDTH,config.WINDOW_HEIGHT)) #creating the basic grid screen
game_objects.basic_screen(grid_surface)

# Initialize game objects
my_snake=game_objects.Snake()
my_apple=game_objects.Apple()

# --- Main Game Loop ---
while running: #the main loop of the game
    for event in pygame.event.get(): #check for every event possible and gets the input from the user
        if event.type == pygame.QUIT:
            running = False # if the event is QUIT End the loop
        if event.type == pygame.KEYDOWN: #takes the most recent event from the user
            game_started = True #if the users input is "KEY DOWN"= some key is pressed start the game

            if event.key == pygame.K_UP and my_snake.direction != config.DOWN:
                my_snake.direction = config.UP

            elif event.key == pygame.K_DOWN and my_snake.direction != config.UP:
                my_snake.direction = config.DOWN

            elif event.key == pygame.K_LEFT and my_snake.direction != config.RIGHT:
                my_snake.direction = config.LEFT

            elif event.key == pygame.K_RIGHT and my_snake.direction != config.LEFT:
                my_snake.direction = config.RIGHT

    if game_started:
        my_snake.move() #move the snake after updating the curr input

        if my_snake.check_apple_collision(my_apple):
            my_snake.grow()
            my_apple.Random_Apple()
            curr_score+=1

        if my_snake.check_self_collision() or my_snake.check_wall_collision():
            running=False

    score_text="score: " + str(curr_score) #score tracker
    text_score_surface=score_font.render(score_text,True,config.WHITE)

    screen.blit(grid_surface,(0,0))
    my_snake.draw(screen)
    my_apple.draw_apple(screen)
    screen.blit(text_score_surface,(20,20))

    curr_level=(curr_score//5)+1 #start from level 1
    curr_fps=min(config.INITIAL_FPS+(curr_score//5 * config.SPEED_BOOST_PER_LEVEL),config.MAX_FPS)
    clock.tick(curr_fps)

    pygame.display.update() #update the screen for each event

pygame.quit() #end the pygame init func