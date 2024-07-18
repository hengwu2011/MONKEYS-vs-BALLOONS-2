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
    

    def __init__(self,x,y,width,height, health, damage, attack_cooldown, health_upgrade,damage_upgrade,attack_cooldown_upgrade):
        self.health = health
        self.damage= damage
        self.attack_cooldown = attack_cooldown
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health_upgrade =  health_upgrade
        self.damage_upgrade =  damage_upgrade
        self.attack_cooldown_upgrade =  attack_cooldown_upgrade

    def upgrade(self):  
        health_upgrade = self.health_upgrade
        damage_upgrade = self.damage_upgrade
        attack_cooldown_upgrade = self.attack_cooldown_upgrade
        self.health += health_upgrade
        self.damage += damage_upgrade
        self.attack_cooldown -= attack_cooldown_upgrade

    def show(self):
        pg.draw.rect(self.x,self.y,self.width,self.height)

    def damage_recieved(self,damage_intake):
        self.health = self.health-damage_intake
