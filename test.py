import pygame as pg 
from enemy import Enemy 

# pg setup
pg.init()
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
running = True
num_of_enemies = 10
enemy_list = [


]
for e in range(num_of_enemies):
    enemy_list.append(Enemy(5,5,5,5,5,900,e*105,50,50))
rectangle_list = [
   
]

def show_boxes(box_list):
    for index,box in enumerate(box_list):
       color_of_box = box.health
       actual_rect = box.rect_box
       box.skin()
       box.movement()
       pg.draw.rect(screen, color_of_box, actual_rect)

while running:
    #show_boxes(rectangle_list)
   
    keys = pg.key.get_pressed()
    position_x =  pg.mouse.get_pos()[0]
    position_y =  pg.mouse.get_pos()[1]
    for x in enemy_list:
        x.show()
        x.movement()
    pg.display.flip()
    # poll for events
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONUP:
            #print(position_x,position_y)
            pass
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

    clock.tick(10)  # limits FPS to 60
 
pg.quit()