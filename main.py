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
from enemy import Enemy 
import pygame as pg
import math
def quantize(mouse_x_pos,grid_x_size,BORDER):
    return math.floor(mouse_x_pos/grid_x_size)*grid_x_size+BORDER/2
clock = pg.time.Clock()
# Initialize pg
pg.init()


# Set window dimensions
num_of_enemies = 10
enemy_list = []
for e in range(num_of_enemies):
    enemy_list.append(Enemy(5,5,5,5,5,900 - e*50,e*105,50,50))
rectangle_list = [
   
]
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
screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Rectangle Grid")

def draw_grid():
    for x in range(0, WINDOW_WIDTH, BLOCK_SIZE):
        for y in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
            rect = pg.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pg.draw.rect(screen, WHITE, rect, 1)

while True:
    screen.fill("black")
    draw_grid()
    show_sprite(tower_list)
    for x in enemy_list:
        x.skin()
        x.movement()
        
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONUP:
            rect_x = quantize(pg.mouse.get_pos()[0],BLOCK_SIZE,BORDER)
            rect_y = quantize(pg.mouse.get_pos()[1],BLOCK_SIZE,BORDER)
            tower_list.append(Tower(rect_x,rect_y,BLOCK_SIZE-BORDER,BLOCK_SIZE-BORDER,50,50,2.5,15,15,1))
            
            rect = tower_list[-1].get_rect()
            pg.draw.rect(screen, "black", pg.Rect(rect["x"],rect["y"],rect["width"],rect["height"]))
        if event.type == pg.QUIT:
            
            pg.quit()


    
    clock.tick(60)
    pg.display.update()
   