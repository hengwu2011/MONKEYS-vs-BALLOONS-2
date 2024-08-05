"GOAl"#get towers to appear on grid upon click
"""ingredients: 
x and y of rect??, mou button  up event,function to draw rectangles"""
"""translation: 
x and y of rect??
if event.type == MOUSEBUTTONUP:
    pg.draw.rect(grid rect x, grid rect y,)
"""
#goal make towers shooot projetiles with a delay
#ingredints projectiles, delay, towers, shooting method

from tower import Tower
from projectile import Projectiles
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
projectile_list = []
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
            tower_list.append(Tower({"health":50,"damage":15,"attack_cooldown":2.5,"x":rect_x,"y":rect_y,"width":BLOCK_SIZE-BORDER,"height":BLOCK_SIZE-BORDER,"health_upgrade":50,"damage_upgrade":50,"attack_cooldown_upgrade":2.5}))
            projectile_list.append(Projectiles(rect_x,rect_y,50,20,15,50,0,0,0))
            rect = tower_list[-1].get_rect()
            pygame.draw.rect(screen, "black", pygame.Rect(rect["x"],rect["y"],rect["width"],rect["height"]))
        if event.type == pygame.QUIT:
            
            pygame.quit()


    
    clock.tick(50)
    pygame.display.update()