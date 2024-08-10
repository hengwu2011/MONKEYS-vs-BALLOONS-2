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
import pygame as pg
import math
import random as rd
from enemy import Enemy
from wall_monkey import Wall_monkey
def quantize(mouse_x_pos,grid_x_size,BORDER):
    return math.floor(mouse_x_pos/grid_x_size)*grid_x_size+BORDER/2
clock = pg.time.Clock()
# Initialize pg
pg.init()


# Set window dimensions
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
projectile_list = []
num_of_enemies = 10
enemy_list = []
for e in range(num_of_enemies):
    enemy_list.append(Enemy({"health":5,"damage":5,"x_speed":rd.random()*10,"y_speed":5,"x_position":WINDOW_WIDTH,"y_position":e*BLOCK_SIZE+BLOCK_SIZE/2 - 50/2,"hit_money":e*105,"width":50,"height":50,"attack_speed":50}))

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

    for proj in projectile_list:
        proj.move(5,0)

    show_sprite(projectile_list)
   
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            rect_x = quantize(pg.mouse.get_pos()[0],BLOCK_SIZE,BORDER)
            rect_y = quantize(pg.mouse.get_pos()[1],BLOCK_SIZE,BORDER)
            tower_list.append(Wall_monkey({"health": 50,"damage": 15,"attack_cooldown": 1,"x": rect_x,"y": rect_y,"width": BLOCK_SIZE-BORDER,"height": BLOCK_SIZE-BORDER,"health_upgrade": 15,"damage_upgrade": 15,"attack_cooldown_upgrade": .2,}))
            projectile_list.append(Projectiles({"x":rect_x,"y":rect_y,"width":35,"height":10,"damage":15,"xspeed":5,"yspeed":0,"sprite":pg.image.load("assets/redBalloon2.png").convert(),"effects":"none"}))
            
            
            
        if event.type == pg.QUIT:
            
            pg.quit()


    
    clock.tick(60)
    pg.display.update()
   