"GOAl"#get towers to appear on grid upon click
"""ingredients: 
x and y of rect??, mouse button  up event,function to draw rectangles"""
"""translation: 
x and y of rect??
if event.type == MOUSEBUTTONUP:
    pg.draw.rect(grid rect x, grid rect y,)
"""

#!PROBLEM how to get x and y values of a rectangle on a grid?
from tower import Tower
import pygame
import math
def quantize(mouse_x_pos,grid_x_size,BORDER):
    return math.floor(mouse_x_pos/grid_x_size)*grid_x_size+BORDER/2
clock = pygame.time.Clock()
# Initialize pygame
pygame.init()


# Set window dimensions
WINDOW_HEIGHT = 800
window_width_rough = 1430
# Set block size (adjust as needed)
BLOCK_SIZE = math.floor(WINDOW_HEIGHT/5)
WINDOW_WIDTH =math.floor(quantize(window_width_rough,BLOCK_SIZE, 0))

BORDER = 50
# Colors
BLACK = (250, 250, 0)
WHITE = (175, 250, 0)
tower_list = []

def show_sprite(tower_list):
    for tower in tower_list:
        tower.show_sprite()
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
    draw_grid()
    show_sprite(tower_list)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            rect_x = quantize(pygame.mouse.get_pos()[0],BLOCK_SIZE,BORDER)
            rect_y = quantize(pygame.mouse.get_pos()[1],BLOCK_SIZE,BORDER)
            tower_list.append(Tower(rect_x,rect_y,BLOCK_SIZE-BORDER,BLOCK_SIZE-BORDER,50,50,2.5,15,15,1))
            
            rect = tower_list[-1].get_rect()
            pygame.draw.rect(screen, "black", pygame.Rect(rect["x"],rect["y"],rect["width"],rect["height"]))
        if event.type == pygame.QUIT:
            
            pygame.quit()


    
    clock.tick(50)
    pygame.display.update()