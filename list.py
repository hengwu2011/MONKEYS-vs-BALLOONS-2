"GOAl"#get towers to appear on grid upon click
"""ingredients: 
x and y of rect??, mouse button  up event,function to draw rectangles"""
"""translation: 
x and y of rect??
if event.type == MOUSEBUTTONUP:
    pg.draw.rect(grid rect x, grid rect y,)
"""
#!PROBLEM how to get x and y values of a rectangle on a grid?

import pygame
import math
def quantize(mouse_x_pos,grid_x_size):
    return math.floor(mouse_x_pos/grid_x_size)*grid_x_size + grid_x_size/2

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
        if event.type == pygame.MOUSEBUTTONUP:
            rect_x = quantize(pygame.mouse.get_pos()[0],100)
            rect_y = quantize(pygame.mouse.get_pos()[1],100)
            R = pygame.Rect(rect_x,rect_y,100,100)
            pygame.draw.rect(screen, "green", R)
        if event.type == pygame.QUIT:
            
            pygame.quit()


    
    
    pygame.display.update()