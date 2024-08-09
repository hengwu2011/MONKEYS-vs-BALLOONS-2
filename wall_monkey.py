import pygame as pg

from tower import Tower
#wallnut from pvz
#does not attack
#does no damage
#takes a long time to destroy
#delays enemies movement, stops them in tracks
#extremely tanky


class Wall_monkey(Tower):
    def __init__(self, props):
        super().__init__(props)
        
        self.health = 500
        self.damage = 0
        self.attack_cooldown = 0
        self.sprite = pg.image.load("assets/monkey_village_wall.jpg").convert()
        self.scaled_sprite = pg.transform.scale(self.sprite, (self.width,self.height))