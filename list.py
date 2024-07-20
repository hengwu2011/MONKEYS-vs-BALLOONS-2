import pygame
import sys

# Initialize pygame
pygame.init()

# Set window dimensions
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# Set block size (adjust as needed)
BLOCK_SIZE = 150

# Colors
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)

# Create the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Rectangle Grid")

def draw_grid():
    for x in range(0, WINDOW_WIDTH, BLOCK_SIZE):
        for y in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)
    draw_grid()
    pygame.display.update()