import pygame as pg
from enemy import Enemy 

class Tank_Enemy(Enemy):
  def __init__(self,props):
    super().__init__(props)
    self.width = 200
    self.height = 200
    self.health = 500
    self.x_speed = 1
    self.sprite = pg.image.load("assets/Enemies/angryballoonboy.jpg").convert()
    self.sprite.set_colorkey("white")
    self.scaled_balloon = pg.transform.scale(self.sprite,(self.width,self.height))
#use inheritance to generate multiple kinds of enemies,towers,and projectiles