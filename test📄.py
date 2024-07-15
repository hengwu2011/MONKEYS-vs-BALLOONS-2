# Example file showing a basic pg "game loop"
import pygame as pg
from enemy import Enemy 

# pg setup
pg.init()
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
running = True
rectangle_list = [
   
]
def show_boxes(box_list):
    for index,box in enumerate(box_list):
       color_of_box = box.health
       actual_rect = box.rect_box
       pg.draw.rect(screen, color_of_box, actual_rect)
while running:
    show_boxes(rectangle_list)
    pg.display.flip()
    keys = pg.key.get_pressed()
    position_x =  pg.mouse.get_pos()[0]
    position_y =  pg.mouse.get_pos()[1]
    # poll for events
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONUP:
            fav_enemy = Enemy(5,5,5,5,5,5,5,5,5,5)
            rectangle_list.append(fav_enemy)
        if event.type == pg.K_SPACE:
          pass
        if keys[pg.K_t]:
           print(rectangle_list)
        if keys[pg.K_SPACE]:
          for index,box in enumerate(rectangle_list):
              box.move()
              print(box.x_position)
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen

    clock.tick(60)  # limits FPS to 60
 
pg.quit()