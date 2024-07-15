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
    
    def show(self):
        pg.draw.rect(self.x,self.y,self.width,self.height)

    def damage_recieved(self,damage_intake):
        self.health = self.health-damage_intake
