import pygame
import random
import time

pygame.init()
# to adjust the width and height for display screen
display_width = 600
display_height = 400

# Create the screen board
display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Snake Game")

# adding the clock
clocks = pygame.time.Clock()

# To adjust the size of the game
snake_block = 10

# To adjust the speed for the snake
snake_speed = 15

# Coloring
yellow = (255, 255, 102)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50,153, 213)
black = (0, 0, 0)
white = (255, 255, 255)

# To declare the font for score and message
FontStyle = pygame.font.SysFont("cambria", 25)
ScoreFont = pygame.font.SysFont("georgia", 35)

# Create score board
def YourScore(score):
    number = ScoreFont.render("Your Score " + str(score), True, red)
    display.blit(number, [0, 0])

# Define snake and for increasing the length
def Snake(snake_block, SnakeList):
    for x in SnakeList:
        pygame.draw.rect(display, black, [x[0], x[1], snake_block, snake_block])

# Define message for later
def Message(msg, color):
    message = FontStyle.render(msg, True, color)
    display.blit(message, [display_width / 6, display_height / 3])

# Create the loop
def GameLoop():
    GameOver = False # For closing the game
    GameClose = False # To show the quit or retry text if the snake hit edges

    x1 = display_width / 2
    y1 = display_height / 2

    # To add the length of snake later
    x1Change = 0
    y1Change = 0

    SnakeList = []
    SnakeLength = 1

    # Create food
    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    while not GameOver:
        while GameClose == True:
            display.fill(blue)
            Message("Too Bad! Press P to play again or Q to quit", yellow) #Text display if you lose
            YourScore(SnakeLength - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q: # Create key for quit the gmae
                        GameOver = True
                        GameClose = False
                    elif event.key == pygame.K_p: # Create retry button
                        GameLoop() # to play again
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameOver = True # Close the game
            elif event.type == pygame.KEYDOWN: # Create movements for the snake
                if event.key == pygame.K_LEFT:
                    x1Change = -snake_block
                    y1Change = 0
                elif event.key == pygame.K_RIGHT:
                    x1Change = snake_block
                    y1Change = 0
                elif event.key == pygame.K_UP:
                    x1Change = 0
                    y1Change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1Change = 0
                    y1Change = snake_block
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0: # if the snake hits the edge or accidently hit it's own body
            GameClose = True

        # Movement
        x1 += x1Change
        y1 += y1Change
        display.fill(blue)
        pygame.draw.rect(display, green, [foodx, foody, snake_block, snake_block])
        SnakeHead = []
        SnakeHead.append(x1)
        SnakeHead.append(y1)
        SnakeList.append(SnakeHead) # Direction
        if len(SnakeList) > SnakeLength:
            del SnakeList[0]
        # if it hits the body of the snake
        for x in SnakeList[:-1]:
            if x == SnakeHead:
                GameClose = True

        Snake(snake_block, SnakeList)
        YourScore(SnakeLength - 1)
        pygame.display.update()

        # Increase the length for snake
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            SnakeLength += 1
        clocks.tick(snake_speed)
    pygame.quit()
    quit()

# For running the loop
GameLoop()