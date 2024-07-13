import pygame as pg
class Enemy:
  rect_box = pg.Rect(50,50,50,50)
  color = "blue"
  '''
  Heath,position, speed, size, sprites, damage value
  Need to know how to move 

  Speed⚡/Damage➖/Health❤️ are different for each enemy/different sprite

  '''
  def __init__(self):
         self.health = 100
  def prop(self):
   print("HI ENEMY")

