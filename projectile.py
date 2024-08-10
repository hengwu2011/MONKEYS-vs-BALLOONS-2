import pygame as pg
screen = pg.display.set_mode((1280, 720))
screen_x = 1280
screen_y = 720

        
class Projectiles:
    """Projecties needs to be able to :
    do damage
    show on the screen
    move"""
    def __init__(self,options):
        self.x = options["x"]
        self.y = options["y"]
        self.width = options["width"]
        self.height = options["height"]
        self.damage= options["damage"]
        self.xspeed = options["xspeed"]
        self.yspeed = options["yspeed"]
        self.sprite = options["sprite"]
        self.effects = options["effects"]
        self.scaled_sprite = pg.transform.scale(self.sprite, (self.width,self.height))  
        self.bounds = pg.Rect(0,0,self.width,self.height)

    def move(self, xspeed, yspeed):
        self.x+=xspeed
        self.y+=yspeed

    def show_sprite(self):
 
        screen.blit(self.scaled_sprite,(self.x,self.y),self.bounds)