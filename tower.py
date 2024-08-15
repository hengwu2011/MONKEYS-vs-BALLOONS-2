import pygame as pg
screen = pg.display.set_mode((1280, 720))
screen_x = 1280
screen_y = 720
from projectile import Projectiles

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
"""#
#when creating each tower  pass in BLOOCK_SIZE-BORDEER as the sprite_size prop and use that to scale the images
class Tower:
    def __init__(self,options = {"health": 50,"damage": 15,"attack_cooldown": 1,"x": 0,"y": 0,"width": 100,"height": 100,"health_upgrade": 15,"damage_upgrade": 15,"attack_cooldown_upgrade": 0.2,}):
        self.health = options["health"]
        self.damage= options["damage"]
        self.sprite = pg.image.load("assets/Towers/dartMonkey.webp").convert()

        
        
        self.x = options["x"]
        
        
        self.y = options["y"]
        
        
        self.width = options["width"]
        
        
        self.height = options["height"]
        
        
        self.health_upgrade =  options["health_upgrade"]
        
        
        self.damage_upgrade =  options["damage_upgrade"]
        
        
        self.attack_cooldown_upgrade =  options["attack_cooldown_upgrade"]
        self.scaled_sprite = pg.transform.scale(self.sprite, (self.width,self.height))
        
        self.attack_cooldown = options["attack_cooldown"]
        
        self.projectile_list = []
        

    
    def get_rect(self):
        return {"x":self.x, "y":self.y,"width":self.width,"height":self.height}

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
    

    def show_sprite(self):
        
        screen.blit(self.scaled_sprite,(self.x,self.y),pg.Rect(0,0,self.width,self.height))
        
        "translation"
    
    def attack(self):
        Projectiles(self.x,self.y,50,20,self.damage,25,0,"dart",{})

        
            
                

