import pygame as pg
from enemy import Enemy 

class Necromancer_Enemy(Enemy):
  def __init__(self,props):
    super().__init__(props)
    self.width = 50
    self.height = 50
    self.health = 50
    self.x_speed = 5
    self.y_speed = 5
    self.hit_money = 100
    self.attack_speed = 10
    self.sprite = pg.image.load("assets/Enemies/necromancer_balloon.jpg").convert()
    self.sprite.set_colorkey("white")
    self.scaled_balloon = pg.transform.scale(self.sprite,(self.width,self.height))
