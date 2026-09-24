import pygame
import config
import random

"""Draws the main screen with a grid of lines based on CELL_SIZE."""
def basic_screen(surface):
    for x in range (0,config.WINDOW_WIDTH,config.CELL_SIZE):
        pygame.draw.line(surface,(40,40,40),(x,0),(x,config.WINDOW_HEIGHT))
    for y in range (0,config.WINDOW_HEIGHT,config.CELL_SIZE):
        pygame.draw.line(surface,(40,40,40),(0,y),(config.WINDOW_WIDTH,y))

class Apple:

    def __init__(self):
        self.x = random.randrange(0, config.WINDOW_WIDTH, config.CELL_SIZE) # Generate a random initial position aligned with the grid
        self.y = random.randrange(0, config.WINDOW_HEIGHT, config.CELL_SIZE)
        self.surface=pygame.Surface((config.CELL_SIZE,config.CELL_SIZE)) #create the surface of the apple and fill it with red
        self.surface.fill(config.RED)
        self.rect=pygame.Rect(self.x,self.y,config.CELL_SIZE,config.CELL_SIZE) # Create the Rect object for collision detection

    """Generates a new random location for the apple after it is eaten."""
    def Random_Apple(self):
        new_x= random.randrange(0,config.WINDOW_WIDTH, config.CELL_SIZE)
        new_y= random.randrange(0,config.WINDOW_HEIGHT, config.CELL_SIZE)
        self.x=new_x
        self.y=new_y
        self.rect.x=new_x #update the rect position
        self.rect.y=new_y

    """Draws the apple onto the main game surface."""
    def draw_apple(self,surface):
        surface.blit(self.surface, self.rect)

class Snake:

    def __init__(self):
        self.x = (config.WINDOW_WIDTH // 2 // config.CELL_SIZE) * config.CELL_SIZE  #start at the middle of the screen
        self.y = (config.WINDOW_HEIGHT // 2 // config.CELL_SIZE) * config.CELL_SIZE
        self.body=[] # The body is a list of Rects, where index 0 is the head
        head_po=pygame.Rect((self.x, self.y, config.CELL_SIZE, config.CELL_SIZE)) #head position
        body_po=pygame.Rect((self.x-config.CELL_SIZE, self.y, config.CELL_SIZE, config.CELL_SIZE))#body position
        self.body.append(head_po)
        self.body.append(body_po)
        self.surface = pygame.Surface((config.CELL_SIZE, config.CELL_SIZE))  # the surface of the head and fill it with green
        self.surface.fill(config.GREEN)
        self.direction = config.RIGHT# start the movement to the Right

    """Draws all the segments of the snake's body."""
    def draw(self,surface):
        for i in range (0,len(self.body)):
            surface.blit(self.surface, self.body[i])

    """Updates the position of the head based on direction and moves the body."""
    def move (self):
        new_x = self.body[0].x + self.direction[0]
        new_y = self.body[0].y + self.direction[1]
        new_head=pygame.Rect((new_x, new_y, config.CELL_SIZE, config.CELL_SIZE))
        self.body.insert(0,new_head)
        self.body.pop()

    """Calculates the direction of the tail and adds a new segment to it."""
    def grow (self):
        dir_x = self.body[-1].x - self.body[-2].x #calculate the direction for the new tail
        dir_y = self.body[-1].y - self.body[-2].y
        new_x = self.body[-1].x + dir_x #calculate the right position of the new tail
        new_y = self.body[-1].y + dir_y
        new_tail=pygame.Rect((new_x, new_y, config.CELL_SIZE, config.CELL_SIZE))
        self.body.append(new_tail)#add the new position

    def check_apple_collision(self,apple):
        return self.body[0].colliderect(apple.rect) #returns True or False

    def check_wall_collision(self):
        flag=False
        head=self.body[0]
        if head.x < 0 or head.x >= config.WINDOW_WIDTH or head.y < 0 or head.y >= config.WINDOW_HEIGHT:
            flag=True
        return flag

    def check_self_collision(self):
        head = self.body[0]
        for i in range(1,len(self.body)):
            if head.x== self.body[i].x and head.y== self.body[i].y:
                return True
        return False









