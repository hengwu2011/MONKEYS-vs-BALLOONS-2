import pygame as pg
import random as rd
screen = pg.display.set_mode((1280, 720))
screen_x = 1280
screen_y = 720
class Enemy:
  rect_box = pg.Rect(50,50,50,50)
  color = "blue"
  '''
  Heath,position, speed, size, sprites, damage value
  Need to know how to move 

  Speed⚡/Damage➖/Health❤️ are different for each enemy/different sprite

  '''

  def __init__(self, options = {"health":5,"damage":5,"x_speed":rd.random()*10,"y_speed":5,"x_position":0,"y_position":0,"hit_money":0,"width":50,"height":50,"attack_speed":5}):
         self.health = options["health"]
         self.damage = options["damage"]
         self.x_speed = options["x_speed"]
         self.y_speed = options["y_speed"]
         self.x_position = options["x_position"]
         self.y_position = options["y_position"]
         self.hit_money = options["hit_money"]
         self.width = options["width"]
         self.height = options["height"]
         self.attack_speed = options["attack_speed"]
         self.sprite = pg.image.load("assets/Enemies/redballoon.jpeg").convert()
         self.sprite.set_colorkey("white")
         self.scaled_balloon = pg.transform.scale(self.sprite,(self.width,self.height))
         

  def move(self):
       self.x_position -= self.x_speed
       self.y_position -= self.y_speed

  def show(self):
       pg.draw.rect(screen,"red",(self.x_position,self.y_position,self.width,self.height))
 
  def lose_health(self,lost_health):
     self.health -= lost_health

  def skin(self):
   screen.blit(self.scaled_balloon,(self.x_position,self.y_position),pg.Rect(0,0,self.width,self.height))

  def movement(self):
          self.x_position -= self.x_speed

  def attacking(self):                
     return self.damage
  #Goal make the enemy attack do a certain amount of damage 
  #Ingridents need attack speed, damage , attack animation, 
  # Translate self.attack_speed
  