import pygame as pg
"""on click creates a tower
towers should be able to have
health,
damage,
attack speed,
x , y
size
"""
"""tower actions
spawn projectiles
spawn currency 
"""
class Tower:
    

    def __init__(self,x,y,width,height, health, damage, attack_cooldown):
        self.health = health
        self.damage= damage
        self.attack_cooldown = attack_cooldown
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def upgrade(self):  
        self.health = self.health+15
        self.damage = self.damage+15
        self.attack_cooldown = self.attack_cooldown - 3

    def show(self):
        pg.draw.rect(self.x,self.y,self.width,self.height)

    def damage_recieved(self,damage_intake):
        self.health = self.health-damage_intake
