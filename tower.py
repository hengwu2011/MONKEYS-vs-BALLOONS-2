import pygame as pg
screen = pg.display.set_mode((1280, 720))
screen_x = 1280
screen_y = 720

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
        self.sprite = pg.image.load("assets/dartMonkey.webp").convert()
        scaled_sprite = pg.transform.scale(self.sprite, (self.width,self.height))
        screen.blit(scaled_sprite,(self.x,self.y),pg.Rect(0,0,self.width,self.height))