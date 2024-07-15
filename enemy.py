import pygame as pg
screen = pg.display.set_mode((1280, 720))
class Enemy:
  rect_box = pg.Rect(50,50,50,50)
  color = "blue"
  '''
  Heath,position, speed, size, sprites, damage value
  Need to know how to move 

  Speed⚡/Damage➖/Health❤️ are different for each enemy/different sprite

  '''
  def __init__(self,health,damage,x_speed,y_speed,sprite,hit_money,x_position,y_position,width,height):
         self.health = health
         self.damage = damage
         self.x_speed = x_speed
         self.y_speed = y_speed
         self.sprite = sprite
         self.x_position = x_position
         self.y_position = y_position
         self.hit_money = hit_money
         self.width = width
         self.height = height

  def move(self):
       self.x_position -= self.x_speed
       self.y_position -= self.y_speed

  def show(self):
       pg.draw.rect(screen,"red",(self.x_position,self.y_postion,self.width,self.height))


