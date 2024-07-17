#goal - create a grid of rectangles that fills the screen
#ingredients rectangle, a loop, 
#translation 
#function
def grid(x_num,y_num,w,h):
    for x in range(x_num):
        for y in range(y_num):
            pg.draw.rect(screen,"green",pg.rect(x,y,w,h))
import pygame as pg
pg.init()
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
running = False
while running:
    # poll for events
# Drawing Rectangle
    
    pg.display.flip()

    position_x =  pg.mouse.get_pos()[0]
    position_y =  pg.mouse.get_pos()[1]
    
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
                running = False
        if event.type == pg.MOUSEBUTTONUP:
            tower_list.append()
        if event.type == pg.K_SPACE:
            pass


             
             
        
 
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("brown")
    clock.tick(50)  # limits FPS to 60


# Create an object of MyClass

# Access the value of 'x' in the object
  # Output: 5