# Example file showing a basic pg "game loop"
import pygame as pg
import random as rd
# pg setup
pg.init()
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
running = True

rectangle_list = [
     {"rect_box":pg.Rect(50,50,60,60),"color":"red","x_speed":5,"y_speed":9},
    {"rect_box":pg.Rect(100,100,60,60),"color":"blue","x_speed":5,"y_speed":4},
     {"rect_box":pg.Rect(868,3,60,60),"color":"blue","x_speed":5,"y_speed":4}
]

def invert_speed():
    for index,box in enumerate(rectangle_list):
     rectangle_list[index]["y_speed"] = box["y_speed"] * -1
     rectangle_list[index]["x_speed"] = box["x_speed"] * -1

def show_boxes(box_list):
    for index,box in enumerate(box_list):
       color_of_box = box["color"]
       actual_rect = box["rect_box"]
       pg.draw.rect(screen, color_of_box, actual_rect)

def move_boxes(box_list):
     for index,box in enumerate(box_list):
        x_speed = box["x_speed"]
        y_speed = box["y_speed"]
        box_list[index]["rect_box"] = box["rect_box"].move(x_speed,y_speed)
        if box["rect_box"].y > pg.display.get_window_size()[1] or box["rect_box"].y < 0:
            box_list[index]["y_speed"] = box["y_speed"] * -1
        if box["rect_box"].x > pg.display.get_window_size()[0] or box["rect_box"].x < 0:
            box_list[index]["x_speed"] = box["x_speed"] * -1
        

for x in range(100):
    random_number = rd.random()
    screen_width = pg.display.get_window_size()[0]
    rectangle_list.append({"rect_box":pg.Rect(rd.random() *screen_width ,rd.random()*888 ,rd.random() *100,rd.random()*30),"color":"blue","x_speed":rd.random()*10,"y_speed":rd.random()*5})    


while running:
    # poll for events
# Drawing Rectangle
    show_boxes(rectangle_list)
    move_boxes(rectangle_list)
    pg.display.flip()
    keys = pg.key.get_pressed()
    position_x =  pg.mouse.get_pos()[0]
    position_y =  pg.mouse.get_pos()[1]
    
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
                running = False
        if event.type == pg.MOUSEBUTTONUP:
    
            rectangle_list.append({"rect_box":pg.Rect(position_x,position_y,60,60),"color":"blue","x_speed":1,"y_speed":1})
        if event.type == pg.K_SPACE:
            pass
        if keys[pg.K_SPACE]:
            invert_speed()

             
             
        
 
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    clock.tick(50)  # limits FPS to 60

 
#Goal  Change the speed of rects on keyboard input
# Ingrident Need Xspeed and Yspeed, and rect, and keypress
