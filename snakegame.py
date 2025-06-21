# example of creating games in python
'''import pygame
import sys

 Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game")

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic

    # Clear the screen
    screen.fill((0, 0, 0))  # Fill screen with black

    # Draw objects
    # Example: Draw a red rectangle (replace with your game graphics)
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(100, 100, 50, 50))

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()'''





import pygame
import sys
import random

# initialize Pygame
pygame.init()

# constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Game Variables
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_direction = RIGHT
snake_speed = 8
snake_new_head = (0, 0)

apple = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Pygame setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

# Function to draw snake and apple
def draw_objects():
    screen.fill(BLACK)  # Clear screen
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(screen, RED, (apple[0] * GRID_SIZE, apple[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    pygame.display.update()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != DOWN:
                snake_direction = UP
            elif event.key == pygame.K_DOWN and snake_direction != UP:
                snake_direction = DOWN
            elif event.key == pygame.K_LEFT and snake_direction != RIGHT:
                snake_direction = LEFT
            elif event.key == pygame.K_RIGHT and snake_direction != LEFT:
                snake_direction = RIGHT

    # Move snake
    snake_new_head = (snake[-1][0] + snake_direction[0], snake[-1][1] + snake_direction[1])

    # Check if snake hits the wall
    if snake_new_head[0] < 0 or snake_new_head[0] >= GRID_WIDTH or snake_new_head[1] < 0 or snake_new_head[1] >= GRID_HEIGHT:
        pygame.quit()
        sys.exit()

    # Check if snake hits itself
    if snake_new_head in snake[:-1]:
        pygame.quit()
        sys.exit()

    # Check if snake eats the apple
    if snake_new_head == apple:
        snake.append(apple)
        apple = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        snake.pop(0)  # Remove the tail segment
        snake.append(snake_new_head)  # Add new head

    # Draw objects
    draw_objects()

    # Cap the frame rate
    clock.tick(snake_speed)
