import pygame as pg
from tower import Tower

screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()

box_list = []
def show_boxes(box_list):
    for index,box in enumerate(box_list):
       color_of_box = box["color"]
       actual_rect = box["rect_box"]
       pg.draw.rect(screen, color_of_box, actual_rect)
tower_list = []
num_tower = 6
for y in range(num_tower):
    y_2 = pg.display.get_window_size()[1]/num_tower
testtower = Tower(9,9,9,9,9,9,9,9,9,9)
print(testtower.health)
testtower.upgrade()
print(testtower.health)
running = True
while running:
    # poll for events
# Drawing Rectangle
    show_boxes(tower_list)
    pg.display.flip()

    position_x =  pg.mouse.get_pos()[0]
    position_y =  pg.mouse.get_pos()[1]
    
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
                running = False
        
            
        if event.type == pg.K_SPACE:
            pass


             
             
        
 
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    clock.tick(50)  # limits FPS to 60


# Create an object of MyClass

# Access the value of 'x' in the object
  # Output: 5