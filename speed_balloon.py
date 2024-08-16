import pygame as pg
from enemy import Enemy 

class Speed_Enemy(Enemy):
  def __init__(self,props):
    super().__init__(props)
    self.width = 50
    self.height = 50
    self.health = 10
    self.x_speed = 10
    self.y_speed = 5
    self.hit_money = 10
    self.attack_speed = 100
    self.sprite = pg.image.load("assets/Enemies/speedyballoon.png").convert()
    self.sprite.set_colorkey("white")
    self.scaled_balloon = pg.transform.scale(self.sprite,(self.width,self.height))
#use inheritance to generate multiple kinds of enemies,towers,and projectiles