import pygame as pg
from enemy import Enemy 

class Tank_Enemy(Enemy):
  def __init__(self,props):
    super().__init__(props)
    self.width = 100
    self.height = 100
    self.health = 100
    self.x_speed = 1
    self.y_speed = 5
    self.hit_money = 100
    self.attack_speed = 2
    self.sprite = pg.image.load("assets/Enemies/tankballoon.jpg").convert()
    self.sprite.set_colorkey("white")
    self.scaled_balloon = pg.transform.scale(self.sprite,(self.width,self.height))
#use inheritance to generate multiple kinds of enemies,towers,and projectiles