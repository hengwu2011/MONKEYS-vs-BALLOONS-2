import pygame as pg
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
  def __init__(self,health,damage,x_speed,y_speed,hit_money,x_position,y_position,width,height,attack_speed):
         self.health = health
         self.damage = damage
         self.x_speed = x_speed
         self.y_speed = y_speed
         self.x_position = x_position
         self.y_position = y_position
         self.hit_money = hit_money
         self.width = width
         self.height = height
         self.attack_speed = attack_speed
         self.sprite = pg.image.load("assets/redBalloon.jpeg").convert()
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